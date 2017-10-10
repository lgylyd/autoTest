# coding=utf-8
#import sys
#sys.path.append("G:\\python\\new_haitun\\frame_method")
import selenium_pack as sepack
from selenium import webdriver
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\login.conf"
rc=sepack.rc
rc.read(dir_path)
url = rc.get("page_login","url")
elements=[]
for i in rc.items("page_login")[1:]:
    elements.append(i[1].split(">"))


def login(driver,namevalues,passwordvalues):
    sepack.get(driver,url)
    sepack.elementBy(driver,elements[0][0],elements[0][1],namevalues)
    sepack.elementBy(driver,elements[1][0],elements[1][1],passwordvalues)
    sepack.elementBy(driver,elements[2][0],elements[2][1],"click")



if __name__=="__main__":
    brower = webdriver.Chrome()
    brower.maximize_window()
    login(brower,"cs_zq1","yks12345")
    login(brower, "cs_zq1", "yks12345s")
    login(brower, " ", " ")
    brower.close()
