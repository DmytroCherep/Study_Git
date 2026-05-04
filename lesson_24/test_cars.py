import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"


# --- логер ---
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("lesson_24/test_search.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

logger.addHandler(file_handler)


# --- fixture ---
@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    token = response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

    return session


# --- тести ---
@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 4),
    ("brand", 2),
    ("price", 10),
    ("year", 1),
])
def test_search_cars(auth_session, sort_by, limit):

    response = auth_session.get(
        f"{BASE_URL}/cars",
        params={
            "sort_by": sort_by,
            "limit": limit
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) <= limit

    logger.info(f"sort_by={sort_by}, limit={limit}, data={data}")

    print(f"\nsort_by={sort_by}, limit={limit}")
    print(data)