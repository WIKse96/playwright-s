import time

from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = 'https://www.seart.pl/customer/account/login/'
        self.forgottenPass_btn = page.get_by_role("link", name="Nie pamiętasz hasła?")
        self.submit_btn = page.get_by_role("button", name="Logowanie")
        self.pass_input = page.locator("//input[@id='pass']")
        self.login_input = page.get_by_placeholder("*Adres e-mail")
        self.account_btn = page.get_by_role("link", name="Moje konto")
        self.outlogin_btn = page.get_by_title("Wyloguj")
        self.alertEmail_p = page.locator("xpath=//div[@id='advice-required-entry-email']")
        self.alertPassw_p = page.locator("xpath=//div[@id='advice-required-entry-pass']")
    def logipage_run(self):
        self.page.goto(self.url)

    def login(self,email,password):
        self.login_input.fill(email)
        self.pass_input.fill(password)
        self.submit_btn.click()


    def restorepassword(self):
        self.forgottenPass_btn.click()

    def assertLogged(self):
        expect(self.alertEmail_p).to_be_hidden()
        expect(self.alertPassw_p).to_be_hidden()
        expect(self.account_btn).to_be_visible()
        expect(self.outlogin_btn).to_be_visible()

    def logOut(self):
        self.outlogin_btn.click()

