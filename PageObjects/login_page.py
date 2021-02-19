from airtest.core.api import *

from Common.basepage import BasePage
from PageLocators.loginpage_loc import LoginPageLocator


class LoginPage(BasePage):

    def login(self, username, password):
        BasePage.poco(name=LoginPageLocator.login_avator_loc).click()
        sleep(1.0)
        BasePage.poco(name=LoginPageLocator.user_loc).click()
        text(username)
        BasePage.poco(name=LoginPageLocator.passwd_loc).click()
        text(password)
        BasePage.poco(name=LoginPageLocator.loginButton_loc)
