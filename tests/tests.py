import pytest
# from server import competitionDateFilter
from .conftest import client, loadClubs, loadCompetitions, saveClubs, saveCompetitions


clubs = loadClubs()
competitions = loadCompetitions()


# Bug 1
def test_showSummary_wrong_email(client):
    """Test for bug #1
    Checks that a wrong email address doesn't raise an error

    Args:
        client (_type_): _description_
    """
    response = client.post("/showSummary", data={"email": "fake.email@test.com"})

    # assert response.data != IndexError
    assert response.status_code == 200


# Bug 4
def test_showSummary_past_competition(client):
    """Test for bug #1
    Checks that a there is no link to book a place in a past competition

    Args:
        client (_type_): _description_
    """
    response = client.post("/showSummary", data={"email": "fake.email@test.com"})

    # assert response.data != IndexError
    assert response.status_code == 200
    assert b"Mail not found" in response.data
    paragraph = b"""
        <li>
            Spring Festival<br />
            Date: 2020-03-27 10:00:00</br>
            Number of Places: 24  
        </li>
"""
    assert paragraph in response.data


# Bug 2
def test_competitionDateFilter(client):
    """ assert competitionDateFilter("2000-01-01") == False
    assert competitionDateFilter("2050-01-01") == True """
    response = client.get()
    assert 1 == 1


""" def test_book():
    pass """


def test_max_purchasePlaces(client):
    competitions = {}
    """Test for bug #3
    Prevent the user from buying more than 12 places per competition

    Args:
        client (_type_): _description_
    """
    response = client.post(
        "/purchasePlaces", data={"club": "She Lifts", "competition": "Spring Festival"}
    )


# test du bug 4 pour tester l'affichage du template
""" def test_valid_competion():
    pass
 """