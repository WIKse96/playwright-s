from playwright.sync_api import expect
import unittest

class Beds_cat:
    def __init__(self, page):
        self.page = page
        self.url = 'https://www.seart.pl/lozka-drewniane-c-4.html#page=1'
        self.rystykalne_link = page.get_by_role("link", name="Łóżka rustykalne drewniane")
        self.bukowe_link = page.get_by_text("Łóżka bukowe")
        self.debowe_link = page.get_by_title("Łóżka dębowe")
        self.sosnowe_link = page.get_by_title("Łóżka sosnowe")
        self.firstProduct_link = page.locator("xpath=//ul[contains(@class, 'products-grid')]/li[contains(@class, "
                                              "'item')][1]/div/div/h2/a").text()

    # odpal strone kategorię z łóżkami
    def run_beds(self) -> None:
        self.page.goto(self.url)

    # asercje czy odpowiednie elementy znajdują się na stronie
    def beds_assertions(self) -> None:
        expect(self.bukowe_link).to_be_visible()
        expect(self.debowe_link).to_be_visible()
        expect(self.sosnowe_link).to_be_visible()
        print(self.firstProduct_link)

