import pytest
from server import create_app


def getClubs():
    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.com", "points": "15"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "8"},
    ]
    return clubs


def getCompetitions():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "24",
        },
        {
            "name": "Fall Classic", 
            "date": "2023-10-22 13:30:00",
            "numberOfPlaces": "11"
        },
        {
            "name": "Winter Competition",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "30",
        },
        {
            "name": "Spring Festival 2",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Summer Classic",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "18",
        },
    ]

    return competitions


def saveClubs():
    pass


def saveCompetitions():
    pass


@pytest.fixture
def client():
    clubs_data = getClubs()
    competitions_data = getCompetitions()
    app = create_app({"TESTING": True}, clubs_list=clubs_data, competitions_list=competitions_data)
    with app.test_client() as client:
        yield client
