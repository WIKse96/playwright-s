class ProductCard:
    def __init__(self, page):
        self.page = page
        self.urlSimple = 'https://www.seart.pl/lustro-sosnowe-rustyk-pion-poziom-18393.html'
        self.urlGroupedWithAdds = 'https://www.seart.pl/lozko-sosnowe-rustyk-ostrowit-ii-140.html'
        self.urlGrouped = 'https://www.seart.pl/lozko-sosnowe-rustyk-ostrowit-ii-140.html'
        self.h1 = page.get_by_role("heading", name="Lustro drewniane wiszące Rustyk")
        self.opineo = page.get_by_role("link", name="Opineo")
        self.technicalS = page.get_by_text("Specyfikacja techniczna")
        self.faq = page.get_by_role("link", name="FAQ")
        self.askCA = page.get_by_role("link", name="Zapytaj o produkt")
        self.descr = page.get_by_role("link", name="Opis")
        self.ask_name = page.get_by_label("Nazwa*")
        self.ask_email = page.get_by_label("E-mail*")
        self.ask_message = page.get_by_label("Treść pytania*")
        self.ask_submit = page.get_by_role("button", name="Wyślij pytanie")
        self.search = page.locator("#search").nth(1)
        self.logo = page.get_by_role("link", name="Drewniane meble sosnowe, bukowe i dębowe - Seart.pl - producent mebli drewnianych")
        self.opinions = page.frame_locator("iframe[title=\"Produktowy 06\\.2023\"]").get_by_text("Zobacz, co Klienci mówią o naszych produktach:")
        self.addtocart_btn = page.get_by_role("button", name="Do koszyka")
        self.cartOnProductCart = page.locator("xpath=//a[@href='https://www.seart.pl/checkout/cart/']//strong[contains(text(),'Koszyk')]")
        self.gotocheckou_btn = page.get_by_role("button", name="Zamówienie")

    def run_productsimple(self):
        self.page.goto(self.urlSimple)
    def productSimpleAssertions(self):
        assert self.h1
        assert self.opineo
        assert self.technicalS
        assert self.faq
        assert self.askCA
    def addtocartSimple(self):
        self.addtocart_btn.click()
        self.cartOnProductCart.hover()
        self.gotocheckou_btn.click()
