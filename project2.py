import numpy as np
import pandas as pd
import json
import argparse
import os
from numpyencoder import NumpyEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


def load_json_file(file_path):
    try:
        data = pd.read_json(file_path)
        return data
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        return None

def data_processing(data):
    ingredients_series = pd.Series(data['ingredients'])
    ingredients_series = ingredients_series.apply(lambda l: ','.join(map(str, l)))
    data['ingredients'] = ingredients_series.str.strip()
    data = data[['id', 'cuisine', 'ingredients']]
    if data.isnull().values.any():
        print("Warning: missing data found in data!")
    return data

def fresult(ingredients, N, data):
    if len(data) < 2:
        return {"error": "Input data must contain at least 2 rows"}

    x = data.ingredients
    y = data.cuisine
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=100)
    vect = CountVectorizer()
    tfidf = TfidfTransformer()
    knn = KNeighborsClassifier(n_neighbors=5)

    knn_pipeline = Pipeline([
        ('vect', vect),
        ('tfidf', tfidf),
        ('knn', knn)
    ])

    knn_pipeline.fit(train_data['ingredients'], train_data['cuisine'])
    y_pred = knn_pipeline.predict(ingredients)
    train_data = train_data[train_data['cuisine'] == y_pred[0]]
    test_data = test_data[test_data['cuisine'] == y_pred[0]]
    distances = euclidean_distances(knn_pipeline["tfidf"].transform(knn_pipeline["vect"].transform(train_data['ingredients'])), knn_pipeline["tfidf"].transform(knn_pipeline["vect"].transform(ingredients)))
    closest_points = [{"id": index, "score": round(distances[index][0], 3)} for index in np.argsort(distances.flatten())[:int(N)]]

    result = {"Cuisine": y_pred[0],
              "score": closest_points[0]["score"],
              "closest": closest_points}

    temp = json.dumps(result, indent=4, sort_keys=False,
                      separators=(", ", ": "), ensure_ascii=False, cls=NumpyEncoder)
    print(temp)
    return result

DEFAULT_INPUT_FILE = os.path.join(os.getcwd(), "yummly.json")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True, help="Number of closest meals")
    parser.add_argument("--input_file", type=str, default=DEFAULT_INPUT_FILE, help="Path to the input file")
    parser.add_argument("--ingredients", type=str, required=True, nargs='*', help="Ingredients")
    args = parser.parse_args()
    data = load_json_file(args.input_file)
    data = data_processing(data)
    result = fresult(args.ingredients, args.N, data)
