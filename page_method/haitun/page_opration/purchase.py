# coding=utf-8
import selenium_pack as sepack
from selenium import webdriver
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\purchase.conf"
rc=sepack.rc
rc.read(dir_path)
url = rc.get("create_purchase_page","url")
elements=[]
for i in rc.items("create_purchase_page")[1:]:
    elements.append(i[1].split(">"))

def addCart(driver,sku):
    for key in sku:
        sepack.get(driver, url)
        sepack.elementBy(driver,elements[0][0],elements[0][1],"%s"%key)
        sepack.elementBy(driver,elements[1][0],elements[1][1],"click")
        sepack.elementBy(driver,elements[2][0],elements[2][1],"%s"%sku[key])
        sepack.elementBy(driver,elements[3][0],elements[3][1],"click")
        sepack.elementBy(driver,elements[4][0],elements[4][1],"click")

def purchaseOrders(driver,**kwargs):
    addCart(driver,kwargs["sku"])
    sepack.elementBy(driver,elements[5][0],elements[5][1],"click")
    sepack.elementBy(driver,elements[6][0],elements[6][1],"click")
    sepack.elementBy(driver,elements[7][0],elements[7][1],"click")
    return sepack.elementBy(driver,elements[8][0],elements[8][1],"read")

if __name__ == "__main__":
    import login
    brower = webdriver.Chrome()
    brower.maximize_window()
    login.login(brower, "cs_zq1", "yks12345")
    parameter={"sku":{"HK_DEAP002":"20","HK_DEAP001":"20"}}
    print purchaseOrders(brower,**parameter)
    brower.close()