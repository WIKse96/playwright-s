class HomePage:
    def __init__(self, page):
        self.page = page
        self.logo = page.locator(
            'link[role="link"][name="Drewniane meble sosnowe, bukowe i dębowe - Seart.pl - producent mebli '
            'drewnianych"]')
        self.cookie_instrukcja = page.locator('link[role="link"][name="Tu znajdziesz instrukcję"]')
        self.cookie_politykaprywatnosci = page.locator('link[role="link"][name="Więcej w Polityce prywatności"]')
        self.cookie_allowbtn = page.get_by_text("Zgadzam się")

    def homepage_assertions(self):
        assert self.logo
        assert self.cookie_instrukcja
        assert self.cookie_politykaprywatnosci
        assert self.cookie_allowbtn

    def cookietest(self):
        self.cookie_allowbtn.click()
        # Znajdź element div
        self.div_element = self.page.locator('div.notice-text')

        # Sprawdź, czy element nie istnieje (liczba wystąpień elementu jest równa 0)

