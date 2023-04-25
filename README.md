## Project Description
I am Sujata Sahu and as the chief data scientist for a hotel chain known for its delicious food, I was given the task of improving menu profits by helping the staff with menu planning and preparation. To accomplish this, I decided to cluster the large master list of all possible dishes by their ingredients, which would allow us to change foods while keeping the ingredients constant. After clustering the ingredients, I trained a classifier to predict the cuisine type of a new food based on its ingredients. This approach would allow the hotel staff to better understand the large menu set and make informed decisions about menu planning. To make the cuisine predictor accessible to the hotel staff, I created a small interface that prompts the user to supply a list of ingredients and returns the predicted cuisine type. By providing the Executive Chef with a tool that predicts cuisine types based on ingredients, I hope to assist the hotel staff in making better menu planning decisions and improving menu profits.
## Packages used
To do the above I first imported the following packages :
1. os
2. json
3. argparse
4. numpyencoder
5. sklearn.feature_extraction.text
6. sklearn.metrics.pairwise
7. sklearn.neighbors
8. sklearn.pipeline
9. sklearn.model_selection
## process to install package
The installation of above packages was done using pip install. Below is the complete explanation of installation process:

1. Having Python and pip installed on your system prior is required.
2. Create a new directory for the project using the mkdir command and change to that directory using cd.
3. Change to the project0 directory using cd.
4. Install the pipenv package by running the command pip install pipenv.
5. Install all the dependencies listed in the requirements.txt file by running the command pipenv install -r requirements.txt.
6. To run the  tests for the project, use the command pipenv run python -m pytest.
7. To run the redactor.py file, use the command pipenv run python project2.py --N 5 --ingredient paprika  --ingredient banana --ingredient "rice krispies" 
 
## Functions and its definations

The following are the 10 functions I created to carry out the required operation:
1. load_json_file()
2. data_processing()
3. fresult()

### load_json_file()- 
This function attempts to load a JSON file from the given file path using the pandas library's read_json() method. If the file is successfully loaded, it returns the resulting data as a pandas DataFrame object. If there is an error in loading the file, the function catches the exception and prints an error message containing the exception message. It then returns None to indicate that the file could not be loaded.

### data_processing() - 
This function performs some processing on a pandas DataFrame object data and returns the processed DataFrame. The function first extracts the 'ingredients' column from the input DataFrame data and converts it to a pandas Series object. Then, it applies a lambda function that converts each list of ingredients into a comma-separated string of ingredient names. The resulting Series object is then assigned back to the 'ingredients' column of the DataFrame data, with any leading/trailing whitespace removed. Next, the function selects only the 'id', 'cuisine', and 'ingredients' columns from the DataFrame, discarding any other columns. Finally, the function checks if there are any missing values in the DataFrame using the isnull() method. If any missing values are found, it prints a warning message indicating that missing data was found. The overall effect of this function is to convert the list of ingredients for each recipe into a comma-separated string, and then to select only the 'id', 'cuisine', and 'ingredients' columns for further analysis.

### fresult()
This function takes as input a list of ingredients, an integer N, and a pandas DataFrame object data. It uses machine learning techniques to predict the cuisine of the recipe containing the input ingredients and finds the N recipes from the training data that are most similar to the input recipe. The function first checks that the input DataFrame data contains at least 2 rows, and returns an error message if it does not.
Next, the function splits the input DataFrame data into training and test datasets using the train_test_split() method from the sklearn library. It then sets up a machine learning pipeline consisting of a CountVectorizer, a TfidfTransformer, and a KNeighborsClassifier. The pipeline is fitted to the training data using the fit() method. The function then predicts the cuisine of the recipe containing the input ingredients using the predict() method of the machine learning pipeline. It selects only the training and test data for the predicted cuisine using boolean indexing. Next, the function calculates the Euclidean distance between the input recipe and each recipe in the training dataset using the euclidean_distances() method from the sklearn library. It then selects the N recipes from the training dataset that are closest to the input recipe based on Euclidean distance.
The function returns a dictionary containing the predicted cuisine, the similarity score of the closest recipe, and a list of the N closest recipes, sorted by similarity score. The dictionary is also printed in JSON format using the json.dumps() method. Overall, the function performs a recipe classification and retrieval task based on a given list of ingredients and a training dataset of recipes with known cuisines.

## Test Files
## test_load_json_file()
The purpose of this test function is to ensure that load_json_file() is correctly loading a JSON file and returning a pandas DataFrame object. The test function has two parts. In the first part, it creates a temporary JSON file using pd.DataFrame().to_json(). This file contains a list of two dictionaries, each with two key-value pairs. The function then calls load_json_file() with the file path of the temporary file and assigns the return value to the variable result. In the second part of the function, the test asserts that result is a pandas DataFrame object and that it has the expected shape of (2, 2). Overall, the test_load_json_file() function is used to ensure that the load_json_file() function is correctly loading JSON files and returning a pandas DataFrame object.

## test_data_processing_length()
The purpose of this test function is to ensure that data_processing() is correctly processing input data and returning a DataFrame object with the expected number of rows. The test function creates a dictionary data containing the data for a single recipe with id, cuisine, and ingredients. It then creates a pandas DataFrame object data_df from the dictionary and passes it to the data_processing() function. The test asserts that the length of the processed data DataFrame object is equal to the expected length of 1 row. If the data_processing() function correctly processes the input data and returns a DataFrame object with one row, the test will pass. Overall, the test_data_processing_length() function is used to ensure that the data_processing() function is correctly processing input data and returning a DataFrame object with the expected number of rows.

## test_resultf()
The purpose of this test function is to ensure that fresult() is correctly processing input data and returning a dictionary object with the expected keys and values.The test function first creates a dictionary data containing the data for a single recipe with id, cuisine, and ingredients. It then creates a pandas DataFrame object data_df from the dictionary and passes it to the data_processing() function to obtain the processed data DataFrame object. The test function then calls fresult() with an input list of ingredients ['garlic','olive'], a value of 2 for the number of closest points to return, and the processed data DataFrame object. The return value of fresult() is assigned to the variable x. In the final part of the test, the test function asserts that the length of the dictionary x returned by fresult() is equal to the expected length of 1. If the fresult() function correctly processes the input data and returns a dictionary object with one key-value pair, the test will pass.
Overall, the test_resultf() function is used to ensure that the fresult() function is correctly processing input data and returning a dictionary object with the expected keys and values.

## Bugs 
1. The name_redaction() function at some lines just redacting half names like only the first name is blocked and the last name is visible. Most of the places its redacting the whole name
2. The phone_redaction() redacting all the phone numbers but also if it is finding any 10 numbers continously it is blocking them.

## Steps to run the project
1. Clone the project directory 
2. Run below command to install pip  
   pip install pipenv
3. Navigate to directory that we cloned from git and run the command to install dependencies pipenv install
4. Then run the below command
pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --output 'files/' \
                    --stats stderr

5. Then run the below command to test the testcases.
pipenv run python -m pytest
 
## Video my code executing, using the pipenv run command and pipenv run python -m pytest is below
https://user-images.githubusercontent.com/120352925/229947906-0e81b338-c7fb-405a-9add-44110cb17311.mp4

