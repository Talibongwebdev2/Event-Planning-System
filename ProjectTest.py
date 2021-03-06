from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class PageTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()

	def test_browser_title(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Owner's Registration",self.browser.title)

	def check_for_rows_in_list_table(self,row_text):
	    table = self.browser.find_element_by_id('listTable')
	    rows = table.find_elements_by_tag_name('tr')
	    self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Owner's Registration",self.browser.title)

	    header_Text = self.browser.find_element_by_tag_name('h1')
	    self.assertIn("Owner's Registration", header_Text)
	 
	 
	    

	    inputowner = self.browser.find_element_by_id('owner')
	    self.assertEqual(inputowner.get_attribute('placeholder'), "owner")
	    inputowner.click()
	    inputowner.send_keys('Leonalyn Maglines')
	    time.sleep(1)
	    
	    
	    inputaddress = self.browser.find_element_by_id('address')
	    inputaddress.click()
	    inputaddress.send_keys('Blk 13 lot 10 brgy Dimawari')
	    time.sleep(1)
	  
	    inputpet = self.browser.find_element_by_id('pet')
	    inputpet.click()
	    inputpet.send_keys('Shana')
	    time.sleep(1)
	 
	    inputbreed = self.browser.find_element_by_id('breed')
	    inputbreed.click()
	    inputbreed.send_keys('Puspin')
	    time.sleep(1)
	 
	    inputday = self.browser.find_element_by_id('birthday')
	    inputday.click()
	    inputday.send_keys('08/22/2013')
	    time.sleep(1)
	 
	    btnContinue = self.browser.find_element_by_id('btnContinue')
	    btnContinue.click()
	    time.sleep(2)
	 


	
if __name__=='__main__':
	 	unittest.main()

''''	#this page should update and show two types of id on the list
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('Kuma')
	 time.sleep(1)
	 Breed = self.browser.find_element_by_id('breed')
	 Breed.click()
	 time.sleep(1)
	 Breed.send_keys('Pomeranian')
	 time.sleep(1)
	 Day = self.browser.find_element_by_id('birthday')
	 Day.click()
	 time.sleep(1)
	 Day.send_keys('05/25/2012')
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 #self.assertIn('1: Shana Puspin born on 08/22/2013',[row.text for row in rows])
	 #self.assertIn('1: Kuma Pomeranian born on 05/25/2012',[row.text for row in rows])
	 self.check_for_rows_in_list_table('1: Shana Puspin born on 08/22/2013')
	 self.check_for_rows_in_list_table("1: Kuma Pomeranian born on 05/25/2012")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')
''''
