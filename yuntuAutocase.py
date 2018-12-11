# -*- coding=utf-8 -*-
import sys,utils,unittest,runner,log,time,HTMLTestRunner
from test_case import Test_case
from selenium import webdriver
from appium import webdriver
to_list = ["18782019436@163.com"]
obj_log = log.get_logger()
log_file = "E:\yuntu_App\log\yuntu.log"
fp = open(log_file,'w')
configfile = 'config.ini'
class Yuntu_case(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['device'] = 'android'
		desired_caps['platformName'] = 'Android'
		desired_caps['browserName'] = ''
		# desired_caps['version'] = '5.5.1'
		desired_caps['version'] = '6.0.1'
		desired_caps['deviceName'] = '8ded651f'
		# desired_caps['deviceName'] = '074a3332211576bb'
		desired_caps['noReset'] = 'True'
		desired_caps['app'] = r'C:\Users\Administrator\Desktop\APP\wanxiangwuyu.apk'
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'
		desired_caps['automationName'] = 'Uiautomator2'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)
		self.obj_utils = utils.Tools(self.driver)
		self.all_config = self.obj_utils.init_allconfig(configfile)
		self.obj_test_case = Test_case(self.all_config, self.driver)

	def advanced_search_library(self):
		obj_log.info('Advanced search of library start................')
		self.assertEqual(self.obj_test_case.library_advanced_search(), True)
	def books_borrow(self):
		obj_log.info('Borrow books test start................')
		self.assertEqual(self.obj_test_case.borrow_books(), True)
	def tearDown(self):
		self.driver.quit()
		# pass
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Yuntu_case("advanced_search_library"))
	# suite.addTest(yuntu_case("tearDown"))

	return suite

if __name__ == '__main__':
	# configfile = sys.argv[1]

	# print(all_config)
	unitrunner = unittest.TextTestRunner(fp)
	# now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
	# filename = "E:\\yuntu_performance\\Report\\" + now_time + "testReport.html"
	# fp = open(filename, 'wb')
	# unitrunner = HTMLTestRunner.HTMLTestRunner(
	# 	stream=fp,
	# 	title=u'云图测试报告',
	# 	description=u'测试用例详细信息'
	# )
	test_suite = suite()
	rtn1 = unitrunner.run(test_suite)
	fp.close()
	html_report = fp.name
	# sendmail = obj_utils.send_mail(to_list,html_report)
	print('Test Result:', rtn1)
