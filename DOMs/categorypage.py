import time


class CategoryPage:
    def __init__(self, page):
        self.page = page
        self.url = 'https://www.seart.pl/meble.html'
        self.prods = page.locator("xpath=//div[@class ='item-area']")
        self.display_as_grid = page.locator("products-grid")

    def categorypage_run(self)->None:
        self.page.goto(self.url)

    def display_is_grid(self)-> None:
       classCount = self.display_as_grid.count()
       if classCount > 1:
           #dodać info do raportu, że display jest grid
           print('ok')
       else:
           print("nie ok")
           print(classCount)
           # dodać info do raportu, że display jest NIE JEST gr

    def open_first_prod(self) -> None:
        self.prods.first.click()
        time.sleep(3)