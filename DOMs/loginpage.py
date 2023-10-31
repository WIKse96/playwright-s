import time

from playwright.sync_api import expect

from utils.secret_config import PASSWORD, EMAIL
class LoginPage:
    def __init__(self, page_login):
        self.page_login = page_login
        self.url = 'https://www.seart.pl/customer/account/login/'
        self.forgottenPass_btn = page_login.get_by_role("link", name="Nie pamiętasz hasła?")
        self.submit_btn = page_login.get_by_role("button", name="Logowanie")
        self.pass_input = page_login.get_by_placeholder("*Hasło")
        self.login_input = page_login.get_by_placeholder("*Adres e-mail")
        self.account_btn = page_login.get_by_role("link", name="Moje konto")
        self.outlogin_btn = page_login.get_by_title("Wyloguj")

    def logipage_run(self):
        self.page_login.goto(self.url)

    def login(self):
        self.login_input.fill(EMAIL)
        self.pass_input.fill(PASSWORD)
        self.submit_btn.click()

    def restorepassword(self):
        self.forgottenPass_btn.click()

    def assertLogged(self):
        time.sleep(2)
        expect(self.account_btn).to_be_visible()
        expect(self.outlogin_btn).to_be_visible()
