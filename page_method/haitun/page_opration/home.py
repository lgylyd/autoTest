# coding=utf-8
#import sys
#sys.path.append("G:\\python\\new_haitun\\frame_method")
import selenium_pack as sepack
from selenium import webdriver
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\home.conf"
rc=sepack.rc
rc.read(dir_path)
url = rc.get("home_page","url")
elements=[]
for i in rc.items("home_page")[1:]:
    elements.append(i[1].split(">"))
    print elements

def entryPurchaseOrders(driver):
    sepack.get(driver,url)
    print sepack.elementBy(driver, elements[0][0], elements[0][1],"read")
    print sepack.elementBy(driver, elements[1][0], elements[1][1], "read")
    print sepack.elementBy(driver, elements[2][0], elements[2][1], "read")
    print sepack.elementBy(driver, elements[3][0], elements[3][1], "read")
    print sepack.elementBy(driver, elements[4][0], elements[4][1], "read")
    print sepack.elementBy(driver, elements[5][0], elements[5][1], "read")
    print sepack.elementBy(driver, elements[6][0], elements[6][1], "read")
    print sepack.elementBy(driver, elements[7][0], elements[7][1], "read")
    print sepack.elementBy(driver, elements[8][0], elements[8][1], "read")
    print sepack.elementBy(driver, elements[9][0], elements[9][1], "read")
    print sepack.elementBy(driver, elements[10][0], elements[10][1], "read")
    print sepack.elementBy(driver, elements[11][0], elements[11][1], "read")
    print sepack.elementBy(driver, elements[12][0], elements[12][1], "read")






if __name__=="__main__":
    import login,time
    brower = webdriver.Firefox()
    brower.maximize_window()
    login.login(brower,"cs_zq1","yks12345")
    time.sleep(1)
    entryPurchaseOrders(brower)
    brower.close()
