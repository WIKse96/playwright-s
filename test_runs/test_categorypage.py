from DOMs.categorypage import CategoryPage


def test_catpage(set_up):
    page = set_up
    url = 'https://www.seart.pl/meble.html'
    categoryObj = CategoryPage(page)
    categoryObj.categorypage_run(url)
    categoryObj.display_is_grid()
    categoryObj.assert_category()
    categoryObj.open_first_prod()
