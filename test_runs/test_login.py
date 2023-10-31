import pytest

from DOMs.loginpage import LoginPage


def test_login(login_Set_up):
    page = login_Set_up
    loginpage = LoginPage(page)
    loginpage.logipage_run()
    loginpage.login()
    loginpage.assertLogged()