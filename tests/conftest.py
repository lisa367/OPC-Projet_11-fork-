import pytest
import pytest_flask
from ..server import create_app


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