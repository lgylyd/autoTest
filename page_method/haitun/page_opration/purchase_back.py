# coding=utf-8
import selenium_pack as sepack
from selenium import webdriver
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\purchase_back.conf"
rc=sepack.rc
rc.read(dir_path)
url = rc.get("query_purchase_page","url").split(">")
elements=[]
for i in rc.items("query_purchase_page")[1:]:
    elements.append(i[1].split(">"))

def payment(driver,**kwargs):
    driver.switch_to_frame(driver.find_element_by_xpath(url[1]))
    sepack.elementBy(driver,elements[0][0],elements[0][1],kwargs["orders"])
    sepack.elementBy(driver,elements[1][0],elements[1][1],"click")
    sepack.elementBy(driver,elements[2][0],elements[2][1],"click",10)
    sepack.elementBy(driver,elements[3][0],elements[3][1],kwargs["remark"].decode("utf-8"))
    sepack.elementBy(driver,elements[4][0],elements[4][1],"click")


if __name__ == "__main__":
    import login_back,home_back,time
    brower1 = webdriver.Firefox()
    brower1.maximize_window()
    login_back.login(brower1, "admin", "test123")
    time.sleep(1)
    home_back.entryPurchaseOrders(brower1)
    parameter1 = {"remark":"测试"}

    import login, purchase
    brower2 = webdriver.Chrome()
    brower2.maximize_window()
    login.login(brower2, "cs_zq1", "yks12345")
    parameter2 = {"sku": {"HK_DEAP002": "20", "HK_DEAP001": "20"}}
    #parameter2 = {"sku":{"FE_JPME001":"10"}}
    parameter1["orders"]=purchase.purchaseOrders(brower2, **parameter2)
    brower2.close()

    payment(brower1,**parameter1)
    #brower1.close()