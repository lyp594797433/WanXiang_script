# -*- coding=utf-8 -*-
import utils,runner,log,time,json,simplejson
# from selenium import webdriver
# from appium import webdriver
obj_log = log.get_logger()

isbn_list = {'A': '9787308156417', 'B': '9787516143261', 'C': '9787509745816', 'D': '9787040213607', 'E': '9787509755280', 'F': '9787516410790', 'G': '9787561466584',
			 'H': '9787561460207', 'I': '9787108032911', 'J': '9787561460232', 'K': '9787509748985','N': '9787030334282', 'O': '9787513535663', 'P': '9787500672012',
			 'Q': '9787502554774', 'R': '9787200008715', 'S': '9787030323859', 'T': '9787121212437', 'U': '9787111465300', 'V': '9787515901701', 'X': '9787511107633',
			 'Z': '9787500086062', 'Test_null': '123456789'}
class Test_case(runner.Runner):
	def __init__(self, all_config, driver):
		runner.Runner.__init__(self, all_config, driver)
		
	def library_advanced_search(self):
		page = self._library_advanced_search()
		if page:
			obj_log.info('The advanced search of library was done!')
			return True
		else:
			obj_log.info('The advanced search of library was failed')
			return False
	def borrow_books(self):
		page = self._borrow_books()
		if page:
			obj_log.info('The borrow books was done!')
			return True
		else:
			obj_log.info('The borrow books was failed')
			return False

