import pytest
from DOMs.loginpage import LoginPage
from utils.secret_config import PASSWORD, EMAIL


@pytest.mark.parametrize('email,password', [(EMAIL, PASSWORD),
                                            pytest.param('email.email.ps','fakepasssword', marks=pytest.mark.xfail),
                                            pytest.param('SELECT * FROM users','fakepassss', marks=pytest.mark.xfail)])
def test_login(set_up,email,password):
    page = set_up
    loginpage = LoginPage(page)
    loginpage.logipage_run()
    loginpage.login(email,password)
    loginpage.assertLogged()
