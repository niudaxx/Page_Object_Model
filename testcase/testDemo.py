# @Time:2021/4/14 11:15
# @Author:testDa
# @File:testDemo.py
# @Reason:


from public.models import driver,myunit
from time import sleep
from selenium.webdriver.support.ui import Select
from public.models import screenshot
class TestDemo(myunit.my_unit):


    def test_case1(self):
        chromeDriver = self.driver
        chromeDriver.get('http://localhost:8080/sisqp-web/')
        sleep(1)
        chromeDriver.find_element_by_id('userName').send_keys('hudan')
        chromeDriver.find_element_by_id('j_password').send_keys('f')
        chromeDriver.find_element_by_id('submit').click()
        sleep(1)
        chromeDriver.find_element_by_class_name('icon_dms').click()
        sleep(1)
        chromeDriver.get('http://localhost:8080/sisqp-web/dms-fd/editInput.action')
        sleep(2)
        chromeDriver.find_element_by_xpath('//*[@id="applyTableId"]/tbody/tr[1]/td[11]/a').click()
        sleep(1)
        Select(chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[1]/select')).select_by_index(1)
        sleep(1)
        chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[2]/input[1]').send_keys('啦啦啦啦啦')
        Select(chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[3]/select')).select_by_index(2)
        chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[4]/input[2]').send_keys('哈哈哈哈哈')
        Select(chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[5]/div/select[2]')).select_by_index(1)
        sleep(1)
        Select(chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[5]/div/select[3]')).select_by_index(1)
        sleep(1)
        Select(chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[5]/div/select[4]')).select_by_index(1)
        sleep(1)
        chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[7]/table/tbody/tr[1]/td/a').click()
        sleep(1)
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/a').click()
        Select(chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/select')).select_by_index(1)
        sleep(1)
        Select(chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/select')).select_by_index(1)
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/a').click()
        chromeDriver.find_element_by_xpath('/html/body/div[12]/form/div[2]/div[6]/div[2]/table[2]/tbody[1]/tr[3]/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[8]/textarea').send_keys('abc')
        chromeDriver.find_element_by_xpath('//*[@id="SUBMIT"]/button').click()
        sleep(1)
        screenshot.insert_img(chromeDriver,'截图.png')
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div[3]/a').click()
        chromeDriver.find_element_by_id('S_01_01_RELEVANT_EVALUATION').send_keys('bcd')
        chromeDriver.find_element_by_xpath('//*[@id="SUBMIT"]/button').click()
        sleep(1)
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div[2]/fieldset/table/tbody/tr[1]/td[2]/textarea').send_keys('哈哈哈哈哈')
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div[2]/fieldset/table/tbody/tr[3]/td[2]/input[2]').send_keys('hudan')
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div[2]/fieldset/table/tbody/tr[4]/td[2]/input').send_keys('f')
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/p/label/input').click()
        chromeDriver.find_element_by_xpath('/html/body/div[13]/div/table/tbody/tr[2]/td[2]/div[2]/div/div[3]/p/input').click()
        sleep(5)