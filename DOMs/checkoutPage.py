import time

from playwright.sync_api import expect
import re


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.url = 'https://www.seart.pl/onepagecheckout/'
        self.noncompany_combi = self.page.get_by_text("Osoba prywatna")
        self.company_combi = self.page.get_by_text("Firma").first
        # dane do wysyłki
        self.name_input = self.page.get_by_role("textbox", name="* Imię")
        self.lastname_input = self.page.get_by_role("textbox", name="* Nazwisko")
        self.email_input = self.page.get_by_placeholder("nazwa@domena.pl")
        self.phone_input = self.page.get_by_label("* Telefon")
        self.address_input = self.page.get_by_placeholder("Ulica")
        self.buildNo_input = self.page.get_by_role("textbox", name="* Nr domu Nr mieszkania")
        self.floor_input = self.page.get_by_role("textbox", name="Piętro")
        self.zipcode_input = self.page.get_by_label("*Kod pocztowy")
        self.city_input = self.page.get_by_label("* Miasto")
        self.deliveryMethod_kurier_combi = self.page.get_by_label("Kurier 38,90 zł")
        self.deliveryMethod_osobisty_combi = self.page.get_by_label("Odbiór osobisty 0,00 zł")
        self.paymentMethod_P24_combi = self.page.locator("xpath=//input[@id='p_method_dialcom_przelewy']")
        self.orderComment_input = self.page.locator("#order-comment")
        self.banktransfer_combi = self.page.get_by_label("Przelew tradycyjny")
        self.paypal_combli = self.page.locator('id=p_method_paypal_express')
        self.payinAdvance_combi = self.page.get_by_label("30% przedpłaty + 70% przy odbiorze")
        self.agree_checkbox = self.page.get_by_label("Zgadzam się na powyższe warunki")
        self.agree2_checkbox = self.page.get_by_label("Zgadzam się", exact=True)
        self.newsletter_checkbox = self.page.get_by_label("Zapisz do newslettera")
        self.submit_btn = self.page.get_by_role("button", name="Potwierdzam zamówienie Zamówienie wiąze się z obowiązkiem zapłaty")

    def fillOutForm(self, name, email, zipcode, deliveryM, paymentM,comment, ch1,ch2,ch3):
        expect(self.page).to_have_url(re.compile(".*onepagecheckout"))
        self.noncompany_combi.click()
        self.name_input.fill(name)
        self.lastname_input.fill('Nazwisko')
        self.email_input.fill(email)
        self.phone_input.fill('555444333')
        self.address_input.fill('Ulicowa')
        self.buildNo_input.fill('24a')
        self.floor_input.fill('piętro 4')
        self.zipcode_input.fill(zipcode)
        self.city_input.fill('Busko Z')





        self.orderComment_input.fill(comment)

        if ch1:
            self.agree_checkbox.click()
        if ch2:
            self.agree2_checkbox.click()
        if ch3:
            self.newsletter_checkbox.click()

        # wybierz metodę dostawy. Jeśli podaję k to kurier. W innym wypadku odbiór osobisty
        if deliveryM == 'k':
            self.deliveryMethod_kurier_combi.click()
        else:
            self.deliveryMethod_osobisty_combi.click()
            # wybierz formę płatnośc (p24 - przelewy, p-przelew, pp-paypal,przedp - przetpłata 30%)
        if paymentM == 'p24':
            self.paymentMethod_P24_combi.click()
        elif paymentM == 'p':
            self.banktransfer_combi.click()
        elif paymentM == 'pp':
            self.paypal_combli.click()
        else:
            self.payinAdvance_combi.click()

        #submit, przejście do płatności
        self.submit_btn.click()


        # Sprawdzamy, czy URL zawiera 'go.przelewy24'
        time.sleep(4)


        expect(self.page).to_have_url(re.compile(".*go.przelewy24*"))


