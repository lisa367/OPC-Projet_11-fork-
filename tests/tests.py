import pytest
# from server import competitionDateFilter
from .conftest import client, getClubs, getCompetitions


""" clubs = getClubs()
competitions = getCompetitions() """

def test_index_page(client):
    """
    Tests access to the website
    """
    response = client.get("/")
    assert response.status_code == 200


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
    response = client.post("/purchasePlaces", data={"competition": ["Winter Competition"], "club": ["Iron Temple"], "places": 6})
    assert b"You do not have enough points for this purchase" in response.data


# Bug 3
def test_buy_more_than_12_places(client):
    """Test for bug #3
    Checks that the club cannot buy more than 12 places by competition
    """
    response = client.post("/purchasePlaces", data={"competition": ["Winter Competition"], "club": ["Simply Lift"], "places": 13})
    assert b"You cannot purchase more than 12 places per competition" in response.data


# Bug 4
def test_purchase_places_past_competition(client):
    """Test for bug #4
    Checks that a there is no link to book a place in a past competition
    """
    # response = client.post("/book", data={"competition": "Summer Classic", "club": "Simply Lift"})
    response = client.get("/book/Spring Festival/Simply Lift")
    # print(response.data)

    assert response.status_code == 200
    assert b"You cannot book places from a past competition" in response.data


# Bug 5
def test_points_deduction(client):
    """Test for bug #5
    Checks that the points used to purchase places are deducted from the total in the database
    """
    response_1 = client.post("/showSummary", data={"email": "kate@shelifts.co.uk"})
    response_2 = client.post("/purchasePlaces", data={"competition": ["Summer Classic"], "club": ["She Lifts"], "places": 2})


    assert b"Points available: 8" in response_1.data
    assert b"Points available: 6" in response_2.data



'''
clubs = getClubs()
competitions = getCompetitions()

# Bug 5
def test_points_deduction(client):
    """Test for bug #5
    Checks that the points used to purchase places are deducted from the total in the database
    """
    points_before_transaction = int(clubs[2]["points"])
    response = client.post("/purchasePlaces", data={"competition": ["Summer Classic"], "club": ["She Lifts"], "places": 2})
    points_after_transaction = int(clubs[2]["points"]) 
    places_purchased = response.data[2]
    assert points_after_transaction == points_before_transaction - places_purchased


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

'''



""" def test_competitionDateFilter(client):
    assert competitionDateFilter("2000-01-01") == False
    assert competitionDateFilter("2050-01-01") == True
    response = client.get()
    assert 1 == 1


def test_book():
    pass """



# test du bug 4 pour tester l'affichage du template
""" def test_valid_competion():
    pass
 """

'''
def test_login_with_wrong_email(client):
    """Test for bug #1
    Checks that a wrong email address doesn't raise an error

    Args:
        client (_type_): _description_
    """
    response = client.post("/showSummary", data={"email": "fake.email@test.com"})
    assert response.status_code == 200
'''