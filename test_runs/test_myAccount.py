from DOMs.myAccountPage import MyAccount

def test_CheckOrders(login_Set_up):
    myacc = MyAccount(login_Set_up)
    myacc.checkOrders()
