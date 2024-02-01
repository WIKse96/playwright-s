import time
import re
from playwright.sync_api import expect


class ProductCard:
    # inicjacja elementów
    def __init__(self, page):
        self.page = page
        self.urlSimple = 'https://www.seart.pl/lustro-sosnowe-rustyk-pion-poziom-18393.html'
        self.urlGroupedWithAdds = 'https://www.seart.pl/lozko-sosnowe-rustyk-ostrowit-ii-140.html'
        self.urlGrouped = 'https://www.seart.pl/lozko-sosnowe-rustyk-ostrowit-ii-140.html'
        self.urlSimple_indywidualOpts = 'https://www.seart.pl/materac-estrella-180.html'
        self.heading = page.get_by_role("heading")
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
        self.logo = page.get_by_role("link",
                                     name="Drewniane meble sosnowe, bukowe i dębowe - Seart.pl - producent mebli drewnianych")
        self.opinions = page.frame_locator("iframe[title=\"Produktowy 06\\.2023\"]").get_by_text(
            "Zobacz, co Klienci mówią o naszych produktach:")
        self.addtocart_btn = page.get_by_role("button", name="Do koszyka")
        self.cartOnProductCart = page.locator(
            "xpath=//a[@href='https://www.seart.pl/checkout/cart/']//strong[contains(text(),'Koszyk')]")
        self.gotocheckou_btn = page.get_by_role("button", name="Zamówienie")
        self.qty_input = page.locator("xpath=//input[@class='input-text qty']").first
        self.qtyUp_btn = page.locator("xpath=//a[@class='button-up']").first

        self.qtyUp_G_btn = page.locator("//a[@id='button_up_group_3203']")
        self.qty_G_input = page.locator("//input[@id='super_group_3203']")

        self.items_in_cart = page.locator("//span[@class='items']")

        # Produkt z opcjami
        self.option_alergik = page.locator("//img[@title='Alergik']")
        self.option_lato = page.locator("//img[@title='Lato / Zima - +136,00 zł']")
        self.option_aloevera = page.locator("//img[@title='Aloe Vera - +157,00 zł']")
        self.span_with_price = page.locator("//span[@id='span_swatch_185']")

    # otwarcie produktu prostego
    def run_productsimple(self) -> None:
        self.page.goto(self.urlSimple)

    # otwarcie produktu grupowanego
    def run_productGrouped(self) -> None:
        self.page.goto(self.urlGrouped)

    def run_simple_with_opts(self) -> None:
        self.page.goto(self.urlSimple_indywidualOpts)

    # asercje czy wszystkie elementy na karcie są ok
    def asserions_productGrouped(self) -> None:
        pass
        # asercje czy wszystkie elementy na karcie są ok

    def productAssertions(self) -> None:
        expect(self.technicalS).to_be_visible()
        expect(self.askCA).to_be_visible()
        expect(self.faq).to_be_visible()

        # pętla sprawdzajaca czy na stronie znajdują się headery
        for i in self.heading.all():
            expect(i).to_be_visible()
        expect(self.descr).to_be_visible()
        # klik w zapytaj o produkt
        self.askCA.click()
        expect(self.ask_name).to_be_visible()
        expect(self.ask_email).to_be_visible()

    # dodanie do koszyka
    def addtocart_simple(self) -> None:
        self.addtocart_btn.click()
        self.cartOnProductCart.hover()
        self.gotocheckou_btn.click()

    # dodani do koszyka
    def addtocartGrouped(self) -> None:
        expect(self.qty_G_input).to_have_value(re.compile(r"[0]"))

        self.qtyUp_G_btn.click()
        expect(self.qty_G_input).to_have_value(re.compile(r"[1]"))
        self.qtyUp_G_btn.click()
        expect(self.qty_G_input).to_have_value(re.compile(r"[2]"))
        self.addtocart_btn.click()
        # asercja czy w koszyku znajdują sie produkty
        # assert self.items_in_cart.text_content() == '2 produktów(y)'
        self.cartOnProductCart.hover()
        self.gotocheckou_btn.click()

    # testy produktu prostego z opcjami indywidualnymi
    def choose_opt(self) -> None:
        # sprawdzenie czy nie wyświetla się cena opcji indywidualnej
        expect(self.span_with_price).not_to_be_visible()
        # sprawdzenie czy wybrane są opcje indywidualne
        expect(self.option_alergik).not_to_have_class(re.compile(r"swatch-selected"))
        expect(self.option_lato).not_to_have_class(re.compile(r"swatch-selected"))
        expect(self.option_aloevera).not_to_have_class(re.compile(r"swatch-selected"))
        # klkanie w opcje
        self.option_alergik.click()
        expect(self.span_with_price).to_be_visible()
        expect(self.option_alergik).to_have_class(re.compile(r"swatch-selected"))
        self.option_lato.click()
        expect(self.option_lato).to_have_class(re.compile(r"swatch-selected"))
