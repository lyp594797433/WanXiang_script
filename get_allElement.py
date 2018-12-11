# -*- coding=utf-8 -*-
import utils,time,log,re,sys,json,simplejson,random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from pymouse import PyMouse
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as ui

obj_log = log.get_logger()
obj_utils = utils.Tools()
def init_allElementConfig():
	element_config = 'element_config.ini'
	all_elementConfig = {}
	# all_config_items = obj_utils.get_config_items(configfile)
	all_config_section = obj_utils.get_config_sections(element_config)
	for section in all_config_section:
		all_config_items = obj_utils.get_config_items(section, element_config)
		for i in range(len(all_config_items)):
			all_elementConfig[all_config_items[i][0]] = all_config_items[i][1]
	return all_elementConfig

