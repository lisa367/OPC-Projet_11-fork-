import pytest
from ..server import create_app, competitionDateFilter, book, purchasePlaces


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def clubs_data():
    clubs =  [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.com",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "8"
        }
    ]
    return clubs

@pytest.fixture
def competitions_data():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "24"
        },
        {
            "name": "Fall Classic",
            "date": "2023-10-22 13:30:00",
            "numberOfPlaces": "11"
        },
        {
            "name": "Winter Competition",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "30"
        },
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Summer Classic",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "18"
        }
    ]

    return competitions

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


