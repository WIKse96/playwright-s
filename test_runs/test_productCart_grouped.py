from DOMs.productcard import ProductCard


def test_addToCart_G(set_up) -> None:
    page = set_up
    productObj = ProductCard(page)

    productObj.asserions_productGrouped()
    productObj.productAssertions()
    productObj.addtocart_Grouped()
