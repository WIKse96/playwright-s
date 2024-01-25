from DOMs.categorypage import CategoryPage
from DOMs.beds_categoryPage import Beds_cat


def test_catpage(set_up) -> None:
    page = set_up
    url = 'https://www.seart.pl/meble.html'
    categoryObj = CategoryPage(page)
    categoryObj.categorypage_run(url)
    categoryObj.display_is_grid()
    categoryObj.assert_category()
    categoryObj.open_first_prod()


def test_beds_cat(set_up) -> None:
    page = set_up
    bedsObj = Beds_cat(page)
    bedsObj.run_beds()
    bedsObj.beds_assertions()
    bedsObj.size_filter()
