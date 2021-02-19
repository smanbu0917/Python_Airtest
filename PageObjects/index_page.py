
from airtest.core.api import *

from Common.basepage import BasePage
from PageLocators.indexpage_loc import IndexPageLocator


class IndexPage(BasePage):

    def click_nav_my(self):
        BasePage.poco(name=IndexPageLocator.my_nav_loc).click()
        sleep()
