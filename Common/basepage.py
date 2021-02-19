from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class BasePage:

    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)
    auto_setup(__file__)