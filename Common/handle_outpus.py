# -*- conding: utf-8 -*-
# @Time:2020/5/18 14:30
# @Author:lyc
# @File: handle_outpus.py
# @Software: PyCharm

import os
import shutil

from Common import dir_config


class HandleOutpus:
    @staticmethod
    def handle_allure_results():
        os.chdir(dir_config.outputs_path)
        try:
            shutil.rmtree("allureDir")
        except FileNotFoundError as e:
            print(f"allureDir目录不存在，详细信息如下：{e}")
        os.mkdir(os.path.join(os.path.abspath(dir_config.outputs_path), "allureDir"))
        os.chdir(dir_config.base_dir)

    @staticmethod
    def handle_screenshots():
        for i in os.listdir(dir_config.screenshot_dir):
            if "png" in i:
                os.unlink(os.path.join(dir_config.screenshot_dir, i))
        os.chdir(dir_config.base_dir)

    @staticmethod
    def handle_log():
        for i in os.listdir(dir_config.logs_dir):
            if "log" in i:
                os.unlink(os.path.join(dir_config.logs_dir, i))

        os.chdir(dir_config.outputs_path)


# handle_outputs = HandleOutpus()

if __name__ == '__main__':
    HandleOutpus.handle_log()
    # handle_outputs.handle_allure_results()
    # os.mkdir(os.path.join(os.path.abspath(dir_config.outputs_path), "allureDir"))
    HandleOutpus.handle_screenshots()
    HandleOutpus.handle_allure_results()
