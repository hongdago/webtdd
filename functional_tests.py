#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:functional_tests.py
DESC: Beging TDD
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000")
assert 'Django' in browser.title

