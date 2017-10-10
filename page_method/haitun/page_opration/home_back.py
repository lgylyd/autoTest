# coding=utf-8
#import sys
#sys.path.append("G:\\python\\new_haitun\\frame_method")
import selenium_pack as sepack
from selenium import webdriver
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\home_back.conf"
rc=sepack.rc
rc.read(dir_path)
url = rc.get("home_page","url")
elements=[]
for i in rc.items("home_page")[1:]:
    elements.append(i[1].split(">"))
def entryPurchaseOrders(driver):
    sepack.get(driver,url)
    sepack.elementBy(driver,elements[0][0],elements[0][1],"click")
    time.sleep(2)
    sepack.elementBy(driver,elements[1][0],elements[1][1],"click")



if __name__=="__main__":
    import login_back,time
    brower = webdriver.Firefox()
    brower.maximize_window()
    login_back.login(brower,"admin","test123")
    time.sleep(1)
    entryPurchaseOrders(brower)
    brower.close()
