# -*- coding=utf-8 -*-
import time,configparser,os,log,sys,urllib,re,smtplib,traceback,requests,pymysql,codecs
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from progressbar import *
from email.mime.text import MIMEText
obj_log = log.get_logger()


class Tools:
	def __init__(self, base_url='', user='admin', pwd='123456'):
		self.base_url = base_url
		# self.hallCode = sys.argv[1]
		self.user = user
		self.pwd = pwd
		# self.login()
		# login_rtn = self.login_yt(self.base_url, hallCode, user, pwd)

	# 访问数据库
	def select_sql(self, statement):
		conn = pymysql.connect(
			host='192.168.28.10',
			port=3306,
			user='root',
			passwd='123456',
			charset='utf8',
			db='bookplatform',
		)
		try:
			obj_log.info("Get the data from MySql............")
			cur = conn.cursor(cursorclass=pymysql.cursors.DictCursor)
			a = cur.execute(statement)
		except Exception as e:
			print (e)
		info = cur.fetchmany(a)
		rtn = list(info)
		cur.close()
		conn.close()
		return rtn[0]

	def progressbar_k(self, sleep_time):
		widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')),' ', ETA()]
		pbar = ProgressBar(widgets=widgets, maxval=sleep_time).start()
		for i in range(sleep_time):
			pbar.update(1*i+1)
			time.sleep(1)
			pbar.finish()

	def init_allconfig(self, configfile):
		protocol_first_hallCode = self.get_config('protocol_first', 'hallCode', configfile)
		protocol_first_username = self.get_config('protocol_first', 'username', configfile)
		protocol_first_pwd = self.get_config('protocol_first', 'pwd', configfile)
		protocol_second_hallCode = self.get_config('protocol_second', 'hallCode', configfile)
		protocol_second_username = self.get_config('protocol_second', 'username', configfile)
		protocol_second_pwd = self.get_config('protocol_second', 'pwd', configfile)
		reader_one_username = self.get_config('reader_one','idcard', configfile )
		reader_one_pwd = self.get_config('reader_one','pwd', configfile )
		all_config = {}
		all_config['protocol_first_hallCode'] = protocol_first_hallCode
		all_config['protocol_first_username'] = protocol_first_username
		all_config['protocol_first_pwd'] = protocol_first_pwd
		all_config['protocol_second_hallCode'] = protocol_second_hallCode
		all_config['protocol_second_username'] = protocol_second_username
		all_config['protocol_second_pwd'] = protocol_second_pwd

		all_config['reader_one_username'] = reader_one_username
		all_config['reader_one_pwd'] = reader_one_pwd
		return all_config

	def get_config(self, section, key, configfile):
		config = configparser.ConfigParser()
		path = (os.path.split(os.path.realpath(__file__)))[0] + '\\' + configfile
		config.readfp(codecs.open(path, "r", "utf-8-sig"))
		# options = config.options(self.hallCode)
		# item = config.items(self.hallCode)
		rtn = config.get(section, key)
		return rtn

	def get_config_items(self, section, configfile):
		config = configparser.ConfigParser()
		path = (os.path.split(os.path.realpath(__file__)))[0] + '\\' + configfile
		config.readfp(codecs.open(path, "r", "utf-8-sig"))
		all_items = config.items(section)
		# options = config.options(self.hallCode)
		# item = config.items(self.hallCode)
		return all_items

	def get_config_sections(self, configfile):
		config = configparser.ConfigParser()
		path = (os.path.split(os.path.realpath(__file__)))[0] + '\\' + configfile
		config.readfp(codecs.open(path, "r", "utf-8-sig"))
		all_sections = config.sections()
		# options = config.options(self.hallCode)
		# item = config.items(self.hallCode)
		return all_sections


	def getSize(self):
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		return (x, y)


	def get_isbn(self):
		req_header = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}
		isbn_list = []
		for i in range(1, 11):
			url = "http://www.bookschina.com/24hour/ChangXiao.aspx"
			data = {"txtpage": i, "book_flh": '', "state": '1'}
			datacode = urllib.urlencode(data)
			req_timeout = 50
			url = '%s%s%s' % (url, '?', datacode)
			req = requests.get(url)
			# req.encoding = 'utf8'
			r = req.text
			res_value = r'</span>ISBN(.*?)<br>'

			m_tr = re.findall(res_value, r, re.S | re.M)
			temp = "".join(m_tr)
			p = temp.strip(u'\uff1a')
			p = p.split(u'\uff1a')
			isbn_list.extend(p)
		print (isbn_list)
		return isbn_list


	def send_mail(self,to_list,bodyFile="" ,sub='QA Report',MAIL_HOST="smtp.163.com",MAIL_USER="18782019436@163.com",MAIL_PWD="lyp594797433",MAILTO_FROM='18782019436@163.com'):
		if bodyFile != "":
			f = open(bodyFile, 'r')
			msg = MIMEText(f.read(), 'html', 'utf8')
			f.close()
		else:
			print('File is empty!')
		msg['Subject'] = sub
		msg['From'] = MAILTO_FROM
		msg['To'] = ";".join(to_list)
		try:
			server = smtplib.SMTP(MAIL_HOST)
			#server.connect(MAIL_HOST,MAIL_PORT)
			server.starttls()
			server.login(MAIL_USER, MAIL_PWD)
			server.sendmail(MAILTO_FROM, to_list, msg.as_string())
			server.close()
			return True
		except Exception as e:
			print (str(e))

	def getTextXpath(self, text):
		#appium 1.5版本取消 find_element_by_name,由xpath代替。
		XPATH_TEXT_FORMAT = "//*[@text='{}']".format(text)
		return XPATH_TEXT_FORMAT
