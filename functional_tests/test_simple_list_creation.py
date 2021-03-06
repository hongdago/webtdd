#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:test_simple_list_creation.py
DESC: Beging TDD
"""
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

class NewVistorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪丝听说有一个很酷的在线待办事项应用
        #她去看了这个应用的首页
        self.browser.get(self.server_url)

        #她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do' ,self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #应用邀请她输入一个待办事项
        inputbox=self.get_item_input_box()
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item')
        
        #她在文本输入框中输入“Buy peacock feathers”
        #伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后，页面更新了,被带到一个新的URL
        #待办事项表格中显示了:"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1) 


        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        
        #页面中又显示了一个文本框，可以输入其他的待办事项
        #她输入了"Use peacock feathers to make a fly"
        #伊迪丝做事很有条理
        inputbox=self.get_item_input_box()
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
                
        
        #页面再次更新，她的清单上显示了这两个待办事项
        time.sleep(2) 

        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        #现在有一个叫做弗朗西斯的新用户访问网站
        ##我们使用一个新的浏览器会话
        ##确保伊迪丝的信息不会从cookie中泄漏出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #弗朗西斯访问首页
        #页面中看不到伊迪丝的清单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #弗朗西斯输入一个新待办事项，新建一个清单
        inputbox=self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #弗朗西斯获得他的唯一URL
        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)


        #这个页面还是没有伊迪丝的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)
        
        
        #伊迪丝想知道这个网站是否会记住她的清单
        
        
        #她看到网站为她生成了唯一的URL
        #而且页面中有一些文字解说这个功能
        
        #她访问那个URL，发现她的待办事项列表还在
        
        #她很满意，去睡觉了
        #两人都很满意，去睡觉了
