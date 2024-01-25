from playwright.sync_api import expect


class Beds_cat:
    def __init__(self, page):
        self.page = page
        self.url = 'https://www.seart.pl/lozka-drewniane-c-4.html#page=1'
        self.rystykalne_link = page.get_by_role("link", name="Łóżka rustykalne drewniane")
        self.bukowe_link = page.get_by_text("Łóżka bukowe", exact=True)
        self.debowe_link = page.get_by_title("Łóżka dębowe")
        self.sosnowe_link = page.get_by_title("Łóżka sosnowe")
        self.product_name_h2 = page.locator("//h2[@class='product-name']").all()
        self.filter200 = page.locator(
            "//a[@class='amshopby-attr' and @href='https://www.seart.pl/lozka-drewniane-c-4/200x200-cm.html']")

    # Funkcja do sprawdzenia czy na listingu znajdują się produkty, które są podane w argumencie strToFind
    def checkListing(self, strToFind):
        for i in self.product_name_h2:
            if strToFind in i.text_content().lower():
                return True
            else:
                return False

    # odpal strone kategorię z łóżkami
    def run_beds(self) -> None:
        self.page.goto(self.url)

    # asercje czy odpowiednie elementy znajdują się na stronie
    def beds_assertions(self) -> None:
        expect(self.bukowe_link).to_be_visible()
        expect(self.debowe_link).to_be_visible()
        expect(self.sosnowe_link).to_be_visible()
        self.page.pause()
        # asercja czy na listingu znajdują się produkty z tytułem "łóżko"
        assert Beds_cat(self.page).checkListing("łóżko")

    def size_filter(self):
        self.filter200.click()
        assert Beds_cat(self.page).checkListing("łóżko")
        assert Beds_cat(self.page).checkListing("200")
