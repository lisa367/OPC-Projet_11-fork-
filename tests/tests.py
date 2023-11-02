import pytest
from .conftest import client
from server import loadClubs, loadCompetitions, saveClubs, saveCompetitions


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_login_with_right_email(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.com"})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.com" in response.data


def purchase_places_in_future_competition(client):
    response = client.get("/book/Summer Classic/She Lifts")
    assert b"Booking for Summer Classic || GUDLFT" in response.data
    assert b"Places available: 18" in response.data


def test_points_display(client):
    response = client.get("/pointsDisplay")
    assert b"Clubs Points" in response.data


def test_logout(client):
    # url de redirection, donc code 302
    response = client.get("/logout")
    assert response.status_code == 302
    # assert b"Welcome to the GUDLFT Registration Portal!" in response.data



### Tests des bugs ###

# Bug 1
def test_login_with_wrong_email(client):
    """Test for bug #1
    Checks that a wrong email address doesn't raise an error
    """
    response = client.post("/showSummary", data={"email": "fake.email@test.com"})
    assert b"Mail not found" in response.data
    assert response.status_code == 200


# Bug 2
def test_buy_more_places_than_points(client):
    """Test for bug #2
    Checks that the club has enough points to make a purchase
    """
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": ["Winter Competition"],
            "club": ["Iron Temple"],
            "places": 6,
        },
    )
    assert b"You do not have enough points for this purchase" in response.data


# Bug 3
def test_buy_more_than_12_places(client):
    """Test for bug #3
    Checks that the club cannot buy more than 12 places by competition
    """
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": ["Winter Competition"],
            "club": ["Simply Lift"],
            "places": 13,
        },
    )
    assert b"You cannot purchase more than 12 places per competition" in response.data


# Bug 4
def test_purchase_places_past_competition(client):
    """Test for bug #4
    Checks that a there is no link to book a place in a past competition
    """
    # response = client.post("/book", data={"competition": "Summer Classic", "club": "Simply Lift"})
    response = client.get("/book/Spring Festival/Simply Lift")
    assert response.status_code == 200
    assert b"You cannot book places from a past competition" in response.data


# Bug 5
def test_points_deduction(client):
    """Test for bug #5
    Checks that the points used to purchase places are deducted from the total in the database
    """
    response_1 = client.post("/showSummary", data={"email": "kate@shelifts.co.uk"})
    response_2 = client.post(
        "/purchasePlaces",
        data={"competition": ["Summer Classic"], "club": ["She Lifts"], "places": 2},
    )
    assert b"Points available: 8" in response_1.data
    assert b"Points available: 6" in response_2.data



### Test des fonctions pour les fichiers JSON ###

def test_loadClubs():
    clubs = loadClubs()
    assert clubs[2]["name"] == "She Lifts"
    assert clubs[2]["email"] == "kate@shelifts.co.uk"


def test_loadCompetitions():
    competitions = loadCompetitions()
    assert competitions[0]["name"] == "Spring Festival"
    assert competitions[0]["date"] == "2020-03-27 10:00:00"


