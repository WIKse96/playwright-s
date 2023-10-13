import pytest
from playwright.sync_api import Playwright
from website_is_up import test_website_is_up

#konfiguracja playwright żeby można było go używać przy klasach
@pytest.fixture
def set_up(playwright: Playwright):
    main_page = "https://www.seart.pl/"

    #twardo okodowane informacje, zakomentować i puszczać z konsolii
    browser = playwright.chromium.launch(headless=False)
    contex = browser.new_context()
    page = contex.new_page()
    # test czy strona odpowiada
    test_website_is_up(main_page)

    #otwarcie strony głównej
    page.goto(main_page)

    yield page

