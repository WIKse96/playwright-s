from DOMs.homepage import HomePage


def test_homep(set_up) -> None:
    page = set_up
    hompageObj = HomePage(page)
    hompageObj.homepage_assertions()
    hompageObj.cookietest()
