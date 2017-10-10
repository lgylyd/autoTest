# coding=utf-8
import selenium_pack as sepack
from selenium import webdriver
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR+"\\element_config\\b2b_orders.conf"
rc=sepack.rc
rc.read(dir_path)

url = rc.get("create_orders_page","url")
elements=[]
for i in rc.items("create_orders_page")[1:]:
    elements.append(i[1].split(">"))

def BbSellOrder(driver,**kwargs):
    sepack.get(driver,url)
    sepack.elementBy(driver,elements[0][0],elements[0][1],kwargs["orders"])
    sepack.elementBy(driver, elements[1][0], elements[1][1],kwargs["amount"])
    sepack.elementBy(driver, elements[2][0], elements[2][1],kwargs["consignee"].decode("utf-8"))
    sepack.elementBy(driver, elements[3][0], elements[3][1],kwargs["telphone"])
    sepack.elementBy(driver, elements[4][0], elements[4][1]%kwargs["province"], "click")
    sepack.elementBy(driver, elements[5][0], elements[5][1]%kwargs["city"], "click")
    sepack.elementBy(driver, elements[6][0], elements[6][1]%kwargs["district"], "click")
    sepack.elementBy(driver, elements[7][0], elements[7][1], kwargs["address"].decode("utf-8"))
    sepack.elementBy(driver, elements[8][0], elements[8][1], kwargs["identification"])
    addSellOrder(driver, kwargs["sku"],kwargs["price"])
    sepack.elementBy(driver, elements[9][0], elements[9][1], "click")
    sepack.elementBy(driver, elements[10][0], elements[10][1], "click")
    sepack.elementBy(driver, elements[11][0], elements[11][1], "click")
def addSellOrder(driver,sku,price):
    counts = 1
    for key in sku:
        product_number = key
        count = int(sku[key])
        if len(sku) > 1 and counts != 1:
            sepack.elementBy(driver, elements[12][0], elements[12][1], "click")
        sepack.elementBy(driver, elements[13][0], elements[13][1]%counts, "%s"%product_number)
        sepack.elementBy(driver, elements[14][0], elements[14][1]%counts, "%s"%count)
        sepack.elementBy(driver, elements[15][0], elements[15][1]%counts, price)
        counts+=1



if __name__ == "__main__":
    import login
    brower = webdriver.Chrome()
    brower.maximize_window()
    login.login(brower,"cs_zq1","yks12345")
    orders = "test%s"%time.strftime("%Y-%m-%d_%H:%M:%S")
    amount = "99"
    consignee = "谢鹏"
    telphone = "13988889999"
    province = "安徽省"
    city = "安庆市"
    district = "迎江区"
    address = "平湖区华南城一号交易广场六楼A区"
    identification = "430721198904237331"
    price = "0.02"
    sku = {"HK_DEAP001":"3","HK_DEAP002":"3"}
    #sku={"FE_JPME001":"3"}
    parameter = {"sku":sku,
                 "orders":orders,
                 "amount":amount,
                 "consignee":consignee,
                 "telphone":telphone,
                 "province":province,
                 "city":city,
                 "district":district,
                 "address":address,
                 "identification":identification,
                 "price":price}
    for i in range(30):
        parameter["orders"]="test%s" % time.strftime("%Y-%m-%d_%H:%M:%S")
        BbSellOrder(brower,**parameter)