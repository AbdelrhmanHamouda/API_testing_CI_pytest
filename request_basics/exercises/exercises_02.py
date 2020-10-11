import pytest
import requests
import csv


@pytest.fixture()
def BASE_URL():
    """
    Pytest fixture to set BASE_URL for all tests

    :return: BASE_URL - string
    """
    BASE_URL = "http://api.zippopotam.us/"
    return BASE_URL

# Exercise 2.1
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse


# List contain test data to be checked
test_data_zip = [
    ('us', '90210', 'Beverly Hills'),
    ('it', '50123', 'Firenze'),
    ('ca', 'Y1A', 'Whitehorse')
]


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
# and checks that the values for the 'place name' elements correspond
# to those that are specified in the test data object
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip)
def test_placeName_based_on_countryCode_and_zipCode(BASE_URL, country_code, zip_code, expected_place_name):
    response = requests.get(f'{BASE_URL}{country_code}/{zip_code}')
    actual_place_name = response.json()['places'][0]['place name']
    assert actual_place_name == expected_place_name


# Exercise 2.4

# Create the same test data as above, but now in a .csv file, for example:
# us,90210,Beverly Hills
# it,50123,Firenze
# ca,Y1A,Whitehorse
# Place this .csv file in the answers folder of the project

# Create a method read_data_from_csv() that reads the file from 2.3 line by line
# and creates and returns a test data object from the data in the .csv file


def read_data_from_csv():
    """
    Function to read CSV data and pass it to test functions.

    :return: test_data_zip - list
    """
    test_data_zip = []
    csv_file_path = '/Users/ahamouda/study_projects/API_testing_CI_pytest/request_basics/exercises/ex02_csv_test_date.csv'
    with open(csv_file_path, newline='') as csvFile:
        data = csv.reader(csvFile, delimiter=',')
        return [row for row in data]


# Exercise 2.5
# Change the data driven test from Exercise 2.2 so that it uses the test data
# from the .csv file instead of the test data that was hard coded in this file
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_data_from_csv())
def test_placeName_based_on_countryCode_and_zipCode_from_csv(BASE_URL, country_code, zip_code, expected_place_name):
    response = requests.get(f'{BASE_URL}{country_code}/{zip_code}')
    actual_place_name = response.json()['places'][0]['place name']
    assert actual_place_name == expected_place_name
