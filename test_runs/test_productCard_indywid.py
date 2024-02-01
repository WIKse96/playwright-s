from DOMs.productcard import ProductCard

def test_simple_with_indywid(set_up) -> None:
    # inicjalizacja obiektu
    page = set_up
    prodObj = ProductCard(page)

    # testy właściwe
    prodObj.run_simple_with_opts()
    prodObj.choose_opt()
    prodObj.productAssertions()