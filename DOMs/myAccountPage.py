from playwright.sync_api import expect


class MyAccount:
    def __init__(self, page_login):
        self.page_login = page_login
        self.login_input = page_login.get_by_placeholder("*Adres e-mail")
        self.submit_btn = page_login.get_by_role("button", name="Logowanie")
        self.pass_input = page_login.get_by_placeholder("*Hasło")
        self.outlogin_btn = page_login.get_by_title("Wyloguj")
        self.alertEmail_p = page_login.locator("xpath=//div[@id='advice-required-entry-email']")
        self.alertPassw_p = page_login.locator("xpath=//div[@id='advice-required-entry-pass']")
        self.myAccount_link = page_login.locator("xpath=//a[@title='Moje konto']")
        self.seeAllOrders_link = page_login.locator(
            "xpath=//a[@href='https://www.seart.pl/sales/order/history/'][normalize-space()='Zobacz wszystkie']")
        self.orderNr = page_login.locator("xpath=//td[normalize-space()='100018125']")

    def loginpage_run(self, url)->None:
        self.page_login.goto(url)

    def login(self, email, password)->None:
        self.login_input.fill(email)
        self.pass_input.fill(password)
        self.submit_btn.click()

    def assertLogged(self)->None:
        expect(self.alertEmail_p).to_be_hidden()
        expect(self.alertPassw_p).to_be_hidden()
        expect(self.outlogin_btn).to_be_visible()

    def checkOrders(self)->None:
        self.myAccount_link.click()
        self.seeAllOrders_link.click()
        expect(self.orderNr).to_be_visible()

    def logOut(self)->None:
        self.outlogin_btn.click()

