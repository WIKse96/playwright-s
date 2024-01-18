import requests


# test czy zapytanie do strony zwraca kod 200
def website_is_up(url):
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()  # Sprawdzenie kodu statusu odpowiedzi
        assert response.status_code == 200
    except requests.Timeout:
        print("Przekroczono czas oczekiwania na odpowiedź")
    except requests.RequestException as e:
        print(f"Błąd zapytania: {e}")
