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

    def run_beds(self):
        self.page.goto(self.url)

