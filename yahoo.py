#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Opens up web driver and goes to Google Images
driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
driver.get('https://in.images.search.yahoo.com/')

#adding Xpath to find where to write the required search term
box = driver.find_element_by_xpath('//*[@id="yschsp"]')

#adding search term and searching
box.send_keys('Mohanlal')
box.send_keys(Keys.ENTER)

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

#select images using xpath
for i in range(690,99999):
    try:
        driver.find_element_by_xpath('//*[@id="resitem-['+str(i)+']"]').screenshot('D:\Webscraped-Lalettan images\yahoo\Lalettan ('+str(i)+').png')
    except:
        pass

#//*[@id="yui_3_5_1_1_1621192818131_690"]

#//*[@id="yui_3_5_1_1_1621192818131_850"]

#//*[@id="yui_3_5_1_1_1621192818131_878"]

#//*[@id="yui_3_5_1_1_1621196885667_635"]
#//*[@id="yui_3_5_1_1_1621196885667_1148"]
#//*[@id="yui_3_5_1_1_1621197014889_700"]

#//*[@id="yui_3_5_1_1_1621197014889_637"]

#//*[@id="resitem-0"]

#//*[@id="resitem-1"]
