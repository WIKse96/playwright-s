from DOMs.productcard import ProductCard
from DOMs.checkoutPage import CheckoutPage
from website_is_up import website_is_up
from DOMs.checkoutPage import CheckoutPage
from DOMs.loginpage import LoginPage
from utils.secret_config import PASSWORD, EMAIL




# funkcja dokonania zakupu pologowaniu
def test_category_logged(login_Set_up):
    page = login_Set_up
    # dodanie do koszyka produkt grupowany
    productGObj = ProductCard(page)
    checkoutObj = CheckoutPage(page)

    productGObj.run_productGrouped()
    productGObj.productAssertions()
    productGObj.addtocartGrouped()
    # przejście do checkout
    #odkomenować gdy chcemy złożyć zamówienie
    # checkoutObj.payment_delivery_Comment(deliveryM="k", paymentM="p24", comment="test", ch1=True, ch2=True, ch3=True)
