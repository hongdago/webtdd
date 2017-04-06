#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:test_list_item_validation.py
DESC: Beging TDD
"""
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        #伊迪斯访问首页，不小心提交了一个空待办事项
        #输入框中没有内容，她就按了回车键
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        time.sleep(1)


        #首页刷新了，显示一个错误消息
        #提示代办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,'You can\'t have an empty list item')

        #她输入一些文字，然后再次提交，这次没有问题
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk'+Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')
        time.sleep(1)
        
        #她有点儿调皮，又提交了一个空待办事项
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        time.sleep(1)
        
        #在列表页面她看到一个类似的错误
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,'You can\'t have an empty list item')
        
        #输入文字之后就没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea'+Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
