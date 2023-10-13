import requests

# test czy zapytanie do strony zwraca kod 200
def test_website_is_up(url):
    response = requests.get(url)
    assert response.status_code == 200
