from DOMs.categorypage import CategoryPage


def test_catpage(set_up):
    page = set_up
    categoryObj = CategoryPage(page)
    categoryObj.categorypage_run()
    categoryObj.display_is_grid()
    categoryObj.open_first_prod()
