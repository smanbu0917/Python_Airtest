# -*- encoding=utf8 -*-
import unittest
from Common.basepage import BasePage, text, sleep, assert_not_equal
from PageLocators.indexpage_loc import IndexPageLocator
from PageLocators.loginpage_loc import LoginPageLocator
from PageLocators.userpage_loc import UserPageLoc
from TestDatas import Common_Datas


class TestLogin:

    def test_01_login_success(self):
        BasePage.poco("柠檬班").click()
        BasePage.poco(IndexPageLocator.my_nav_loc).click()
        BasePage.poco(LoginPageLocator.avatar_title_loc).click()
        BasePage.poco(LoginPageLocator.user_loc).click()
        text(Common_Datas.c_user)
        BasePage.poco(LoginPageLocator.passwd_loc).click()
        text(Common_Datas.c_passwd)
        BasePage.poco(LoginPageLocator.loginButton_loc).click()
        sleep(3)
        value = BasePage.poco("com.lemon.lemonban:id/fragment_my_lemon_avatar_title").attr("text")
        assert_not_equal(value, "点击11111头像登录", "断言登录成功")

        # BasePage.poco(UserPageLoc.set_button).click()
        # BasePage.poco(UserPageLoc.logout_button).click()
        # sleep()
        # BasePage.poco(UserPageLoc.tv_sure_button).click()
        # BasePage.poco(IndexPageLocator.index_nav_loc).click()
