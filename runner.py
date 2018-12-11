# -*- coding=utf-8 -*-
import utils,time,log,re,sys,json,simplejson,random,get_allElement
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import *
from appium import webdriver
from bs4 import BeautifulSoup
# from utils import Tools as Config
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as ui
all_elementConfig = get_allElement.init_allElementConfig()
print(all_elementConfig)
obj_log = log.get_logger()
class Runner:
	def __init__(self, all_config, driver):
		self.driver = driver
		self.obj_utils = utils.Tools(self.driver)
		self.hallCode = all_config['protocol_first_hallCode']
		self.hallCode_second = all_config['protocol_second_hallCode']

		self.user = all_config['protocol_first_username']
		self.pwd = all_config['protocol_first_pwd']
		self.reader_one_username = all_config['reader_one_username']
		self.reader_one_pwd = all_config['reader_one_pwd']

		# self.driver.implicitly_wait(10)

	def isElementExist_by_xpath(self,element):
			flag=True
			try:
				self.driver.find_element_by_xpath(element)
				obj_log.info('Find element {0} successfully!'.format(element))
				return flag
			except:
				flag=False
				obj_log.info('Find element {0} failed!'.format(element))
				return flag



