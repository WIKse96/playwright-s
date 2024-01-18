import os
from utils.secret_config import PASSWORD, EMAIL
import pytest
from playwright.sync_api import Playwright
from website_is_up import website_is_up
from DOMs.myAccountPage import MyAccount

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD
#konfiguracja playwright żeby można było go używać przy klasach
@pytest.fixture()
def set_up(playwright: Playwright):
    main_page = "https://www.seart.pl/"

    #twardo okodowane informacje, zakomentować i puszczać z konsolii
    browser = playwright.chromium.launch(headless=False)
    contex = browser.new_context()
    page = contex.new_page()
    # test czy strona odpowiada
    website_is_up(main_page)

    #otwarcie strony głównej
    page.goto(main_page)

    yield page
    page.close()

#drugie utworzenie obiektu dla zalogowanego usera.
@pytest.fixture(scope='function')
def login_Set_up(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page_login = context.new_page()
    # Logowanie użytkownika
    myacc = MyAccount(page_login)
    url = 'https://www.seart.pl/customer/account/'
    myacc.loginpage_run(url)
    myacc.login(EMAIL, PASSWORD)

    # Upewnienie się, że użytkownik jest zalogowany
    myacc.assertLogged()

    yield page_login

    # Tutaj możesz ewentualnie dodać kod do wylogowania użytkownika po zakończeniu testu
    myacc.logOut()
    page_login.close()



