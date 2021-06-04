from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	# self.browser.get('http://localhost:8000/')
	 self.browser.get(self.live_server_url)
	 self.assertIn('Warranty tracker',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn('Warranty tracker', header_text)
	 
	 
	 
	'''
	 inputnamen = self.browser.find_element_by_id('namen')
	 self.assertEqual(inputnamen.get_attribute('placeholder'),'Enter your fullname')
	 inputnamen.click()
	 time.sleep(1)
	 inputnamen.send_keys('Cesar Talibong')
	 
	 time.sleep(1)
	 
	 
	 inputnbirthdate = self.browser.find_element_by_id('nbirthdate')
	 self.assertEqual(inputnbirthdate.get_attribute('placeholder'),'Enter the date')
	 inputnbirthdate.click()
	 time.sleep(1)
	 inputnbirthdate.send_keys('02.24.2000')
	 time.sleep(1)
	 
	 
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 
'''

	
