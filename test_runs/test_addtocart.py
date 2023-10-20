import time

import pytest

from DOMs.productcard import ProductCard
from DOMs.checkoutPage import CheckoutPage


@pytest.mark.parametrize('name, email, zipcode, deliveryM, paymentM, comment, ch1,ch2,ch3',[
    ('Wiktor', 'wiktotest@seart.pl', '55-888', 'k', 'p24', 'komentarzĆŹŻŻĆŹółćżśą!@#', True,True,True)])
def test_buy(set_up, name, email, zipcode, deliveryM, paymentM, comment, ch1,ch2,ch3):
    page = set_up

    productCardObj = ProductCard(page)
    checkoutPageObj = CheckoutPage(page)

    productCardObj.run_productsimple()
    productCardObj.addtocartSimple()

    checkoutPageObj.fillOutForm(name, email, zipcode, deliveryM, paymentM, comment, ch1, ch2, ch3)
    time.sleep(3)
