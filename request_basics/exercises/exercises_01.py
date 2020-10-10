import requests
import pytest


@pytest.fixture()
def BASE_URL():
    """
    Pytest fixture to set BASE_URL for all tests

    :return: BASE_URL - string  
    """
    BASE_URL = "http://api.zippopotam.us/"
    return BASE_URL


@pytest.fixture()
def COUNTRY_CODE():
    """
    Pytest fixture to set COUNTRY_CODE for all tests

    :return: COUNTRY_CODE - string  
    """
    COUNTRY_CODE = "us/90210"
    return COUNTRY_CODE

# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210


def test_response_is_200(BASE_URL, COUNTRY_CODE):
    """
    test that response from BASE_URL to COUNTRY_CODE is 200

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert result.status_code == 200


# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_response_header(BASE_URL, COUNTRY_CODE):
    """
    test that response header from BASE_URL/COUNTRY_CODE is 'application/json'

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert result.headers['Content-Type'] == 'application/json'


# Exercise 1.3
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body encoding is not set (equal to None)
def test_response_body_encoding(BASE_URL, COUNTRY_CODE):
    """
    test that response body encoding from BASE_URL/COUNTRY_CODE is not set

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert result.encoding is None


# Exercise 1.4
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'country' has a value equal to 'United States'
def test_response_body_element(BASE_URL, COUNTRY_CODE):
    """
    test that response body element from BASE_URL/COUNTRY_CODE is USA

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert result.json()['country'] == 'United States'


# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places
# has a value equal to 'Beverly Hills'
def test_response_body_element_in_a_list(BASE_URL, COUNTRY_CODE):
    """
    test that response body element in a list from BASE_URL/COUNTRY_CODE is 'Beverly Hills'

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert result.json()['places'][0]['place name'] == 'Beverly Hills'


# Exercise 1.6
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)
def test_response_body_places_array_length(BASE_URL, COUNTRY_CODE):
    """
    test that the length of the places array is 1

    :param: BASE_URL - string
    :param: COUNTRY_CODE - string
    :return: None
    """
    # make request
    result = requests.get(f'{BASE_URL}{COUNTRY_CODE}')
    assert len(result.json()['places']) == 1
