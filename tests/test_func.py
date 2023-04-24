import sys
sys.path.append('..')
import pytest
from project2 import *
import pandas as pd
import unittest
import json


def test_load_json_file():
    # Test with valid file path
    valid_file_path = 'test_valid.json'
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    pd.DataFrame(data).to_json(valid_file_path)
    result = load_json_file(valid_file_path)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)


def test_data_processing_length():
    # Input
    data = {'id': 1, 'cuisine': 'italian', 'ingredients': ['garlic', 'olive oil', 'tomatoes']}
    expected_length = 1  
    data_df = pd.DataFrame.from_dict([data])
    processed_data = data_processing(data_df)
    actual_length = len(processed_data)
    assert actual_length == expected_length

def test_resultf():
    data = {'id': 1, 'cuisine': 'italian', 'ingredients': ['garlic', 'olive oil', 'tomatoes']}
    expected_length = 1  
    data_df = pd.DataFrame.from_dict([data])
    processed_data = data_processing(data_df)
    x= fresult(['garlic','olive'], 2, processed_data)
    actual_length = len(x)
    assert actual_length == expected_length
