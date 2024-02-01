import os
from pathlib import Path
from slugify import slugify
import pytest
import pytest_html
from utils.secret_config import PASSWORD, EMAIL
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

    # Tutaj dać kod do wylogowania użytkownika po zakończeniu testu
    myacc.logOut()
    page_login.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    fixtures = ["set_up", "login_Set_up"]

    for fixture in fixtures:
        if fixture in item.funcargs:
            xfail = hasattr(report, "wasxfail")
            if report.when == "call" and (report.failed or xfail and fixture == "set_up"):
                page = item.funcargs[fixture]
                katalog_zrzutu = Path("screenshots")
                katalog_zrzutu.mkdir(exist_ok=True)
                screen_file = str(katalog_zrzutu / f"{slugify(item.nodeid)}.png")
                page.screenshot(path=screen_file)

            if (report.skipped and xfail) or (report.failed and not xfail):
                # dodaj zrzuty ekranu do raportu html
                extra.append(pytest_html.extras.png(screen_file))
            report.extra = extra
            break
