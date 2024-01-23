from DOMs.productcard import ProductCard


def test_addToCart_G(set_up) -> None:
    page = set_up
    productObj = ProductCard(page)
    productObj.run_productGrouped()
    productObj.asserions_productGrouped()

    productObj.addtocartGrouped()
