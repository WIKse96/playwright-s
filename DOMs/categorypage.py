import time
from playwright.sync_api import expect


class CategoryPage:
    def __init__(self, page):
        self.page = page
        self.prods = page.locator("xpath=//div[@class ='item-area']")
        self.display_as_grid = page.locator("products-grid")
        self.cats_on_left_bar = page.locator(
            "//li[contains(@class,'cat-item')]//a[contains(text(),'Biurka drewniane')]")
        self.list = page.locator("//ul[@id='products-list']//li[@class='item even']").all()
        self.wooden_beds_img = page.locator("//img[@alt='Łóżka drewniane']")
        self.top_btn = page.locator("div").filter(has_text="back to top")
        self.list_filter = page.locator("#narrow-by-list").get_by_role("combobox")
        self.free_Delivery_btn = page.get_by_role("link", name="Darmowa dostawa z wniesieniem pow. 1000 zł")

    def categorypage_run(self, url) -> None:
        self.page.goto(url)

    def display_is_grid(self) -> None:
        if not self.list:
            # dodać info do raportu, że display jest grid
            print('--ok-- Lista produktów w formie GRIDA --ok--')
        else:
            print("Lista produktów w formie listy")

            # dodać info do raportu, że display jest NIE JEST gr

    def open_first_prod(self) -> None:
        self.prods.first.click()
        time.sleep(3)

    # sprawdz czy widoczny jest przycisk powrotu do góry
    def assert_top_btn(self) -> None:
        self.page.mouse.wheel(0, 80)
        expect(self.top_btn).to_be_visible()

    def assert_category(self) -> None:
        expect(self.cats_on_left_bar).to_be_visible()
        expect(self.wooden_beds_img).to_be_visible()

        category_page_instance = CategoryPage(self.page)
        category_page_instance.assert_top_btn()
        expect(self.list_filter).to_be_visible()
        expect(self.free_Delivery_btn)
