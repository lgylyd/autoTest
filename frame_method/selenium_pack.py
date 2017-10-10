# coding=utf-8
#import sys
#sys.path.append("G:\\python\\autoTest\\")
import time
from selenium import webdriver
import ConfigParser
import logging_pack
import os
logging=logging_pack.logger
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
########################################################################################################################
#参数配置文件
rc = ConfigParser.SafeConfigParser()
rc.read(BASE_DIR+'\\frame_config\\selenium_pack.conf')
#设置日志默认保存的位置
log_paths=(BASE_DIR+rc.get("selenium","log_paths"))
#设置截图的默认保存位置
image_paths=(BASE_DIR+rc.get("selenium","image_paths"))
#设置默认响应时间
out_times = rc.getint("selenium","out_times")
#设置默认等待时间
waite_times = rc.getint("selenium","waite_times")

########################################################################################################################

def operationCheck(driver,faction,is_success):
    if(is_success):
        logging.info(u"faction【"+faction+u"】运行成功")
    else:
        image_name="image"+time.strftime('%Y-%m-%d_%H_%M_%S')+".jpg"
        image_path=image_paths+image_name
        logging.error(u"faction【"+faction+u"】运行失败,查看截图："+image_path)
        try:
            driver.get_screenshot_as_file(image_path)
            logging.info(u"保存截图成功，图片保存位置：" + image_path)
        except Exception,e:
            logging.error(u"保存截图失败：" + e)


def get(driver,url,out_time=out_times):
    is_success=False
    current_time=time.time()
    while (time.time()-current_time<=out_time):
        try:
            logging.info(u"开始执行get("+url+")")
            driver.get(url)
            driver.implicitly_wait(out_time)
            is_success=True
            break
        except Exception,e:
            logging.error(e)
            time.sleep(waite_times)
    operationCheck(driver,"get",is_success)

#id操作

def findId(driver,id,out_time=out_times):
    is_success = False
    current_time = time.time()
    while (time.time() - current_time <= out_time):
        try:
            logging.info(u"开始执行driver.find_element_by_id(" + id+ ")")
            driver = driver.find_element_by_id(id)
            is_success = True
            break
        except Exception,e:
            logging.error(e)
            time.sleep(waite_times)
    operationCheck(driver,"findId", is_success)
    return is_success,driver

def idKeys(driver,id,values,out_time=out_times):
    is_success = False
    current_time = time.time()
    if(findId(driver,id,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_id(" + id+ ").send_keys("+values+")")
                driver.find_element_by_id(id).clear()
                driver.find_element_by_id(id).send_keys(values)
                is_success = True
                break
            except Exception,e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"idKeys", is_success)

def idClick(driver,id,out_time=out_times):
    is_success = False
    current_time = time.time()
    if(findId(driver,id,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_id('" + id+ "').click()")
                driver.find_element_by_id(id).click()
                is_success = True
                break
            except Exception,e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"idClick", is_success)

def idRead(driver, id, out_time=out_times):
    is_success = False
    current_time = time.time()
    text = None
    if (findId(driver, id,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_id('" + id + "').text")
                text=driver.find_element_by_id(id).text
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver, "idClick", is_success)
        return text
#name操作

def findName(driver, name, out_time=out_times):
    is_success = False
    current_time = time.time()
    while (time.time() - current_time <= out_time):
        try:
            logging.info(u"开始执行driver.find_element_by_name('" + name + "')")
            driver = driver.find_element_by_name(name)
            is_success = True
            break
        except Exception, e:
            logging.error(e)
            time.sleep(waite_times)
    operationCheck(driver,"findName", is_success)
    return is_success,driver


def nameKeys(driver, name, values, out_time=out_times):
    is_success = False
    current_time = time.time()
    if (findName(driver,name,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_name('" + name + "').send_keys(" + values + ")")
                driver.find_element_by_name(name).clear()
                driver.find_element_by_name(name).send_keys(values)
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"nameKeys", is_success)


def nameClick(driver, name, out_time=out_times):
    is_success = False
    current_time = time.time()
    if (findName(driver,name,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_id('" + name + "').click()")
                driver.find_element_by_name(name).click()
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"nameClick", is_success)

def nameRead(driver, name, out_time=out_times):
    is_success = False
    current_time = time.time()
    text = None
    if (findName(driver, name, out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_id('" + name + "').click()")
                text = driver.find_element_by_name(name).click()
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver, "nameClick", is_success)
        return text

#xpath操作

def findXpath(driver, xpath, out_time=out_times):
    is_success = False
    current_time = time.time()
    while (time.time() - current_time <= out_time):
        try:
            logging.info(u"开始执行driver.find_element_by_xpath()")
            driver = driver.find_element_by_xpath(xpath)
            is_success = True
            break
        except Exception, e:
            logging.error(e)
            time.sleep(waite_times)
    operationCheck(driver,"findXpath", is_success)
    return is_success,driver


def xpathKeys(driver, xpath, values, out_time=out_times):
    is_success = False
    current_time = time.time()
    if (findXpath(driver,xpath,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_xpath("+").send_keys(" + values + ")")
                driver.find_element_by_xpath(xpath).clear()
                driver.find_element_by_xpath(xpath).send_keys(values)
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"xpathKeys", is_success)


def xpathClick(driver, xpath, out_time=out_times):
    is_success = False
    current_time = time.time()
    if (findXpath(driver,xpath,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                logging.info(u"开始执行driver.find_element_by_xpath('"+"').click()")
                driver.find_element_by_xpath(xpath).click()
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"xpathClick", is_success)

def xpathRead(driver, xpath, out_time=out_times):
    is_success = False
    current_time = time.time()
    text = None
    if (findXpath(driver,xpath,out_time)[0]):
        while (time.time() - current_time <= out_time):
            try:
                print xpath
                logging.info(u"开始执行driver.find_element_by_xpath('"+"').click()")
                text = driver.find_element_by_xpath(xpath).click()
                is_success = True
                break
            except Exception, e:
                logging.error(e)
                time.sleep(waite_times)
        operationCheck(driver,"xpathClick", is_success)
        return text

def elementBy(driver,element,location,opration,out_time=out_times):
    if element == "id":
        if opration == "click":
            idClick(driver, location,out_time)
        elif opration == "read":
            return idRead(driver, location,out_time)
        else:
            idKeys(driver, location, opration,out_time)
    elif element == "name":
        if opration == "click":
            nameClick(driver,location,out_time)
        elif opration == "read":
            return nameRead(driver, location, out_time)
        else:
            nameKeys(driver, location, opration,out_time)
    elif element == "xpath":
        if opration == "click":
            xpathClick(driver,location,out_time)
        elif opration == "read":
            return xpathRead(driver,location,out_time)
        else:
            xpathKeys(driver, location, opration,out_time)

if __name__ == "__main__":
    brower=webdriver.Chrome()
    brower.maximize_window()
    get(brower,"http://www.baidu.com")
    idKeys(brower,"kw","id")
    idClick(brower,"s")
    get(brower,"http://www.baidu.com")
    nameKeys(brower,"wd", "name")
    xpathKeys(brower,".//*[@id='kw']","xpath")
    findXpath(brower,".//*[@id='kw']",5)[1].send_keys("jks")
    xpathClick(brower,".//*[@id='su']")
    print findId(brower,"s_tab",5)[1].text
    brower.close()





