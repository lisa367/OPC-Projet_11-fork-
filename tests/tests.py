import pytest
from ..server import create_app, competitionDateFilter, book, purchasePlaces
from conftest import *


clubs = clubs_data()
competitions = competitions_data()

# Bug 1
def test_showSummary(client):
    """Test for bug #1
    Checks that a wrong email address doesn't raise an error

    Args:
        client (_type_): _description_
    """
    response = client.post("/showSummary", data={"email": "fake.email@test.com"})

    # assert response.data != IndexError
    assert response.status_code == 200
    assert b"Mail not found" in response.data


# Bug 2
def test_competitionDateFilter():
    assert competitionDateFilter("2000-01-01") == False
    assert competitionDateFilter("2050-01-01") == True

def test_book():
    pass

def test_max_purchasePlaces(client):
    competitions = {}
    """Test for bug #3
    Prevent the user from buying more than 12 places per competition

    Args:
        client (_type_): _description_
    """
    response = client.post("/purchasePlaces", data={"club": "She Lifts", "competition": 'Spring Festival'})


# test du bug 4 pour tester l'affichage du template
def test_valid_competion():
    pass


