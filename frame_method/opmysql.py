# coding:utf-8
"""
@author:LYD
@version:v1.0
"""

import MySQLdb

class mysql():
    """
    提供了两个方法:
    1.queryData 查询数据u
    2.oprationData 操作数据
    """

    def __init__(self,url,username,password,database):
        """
        参数初始化
        :param url: 数据所在服务器地址
        :param username: 用户名
        :param password: 登录密码
        :param database: 要访问的数据库
        """
        self.url=url
        self.database=database
        self.username=username
        self.password=password

    def __connect(self):
        url=self.url
        database=self.database
        username=self.username
        password=self.password
        try:
            # 打开数据库连接
            db=MySQLdb.connect(url,username,password,database,charset="utf8")
        except:
            print u"连接数据库失败"
        return db
        
    def queryData(self,sql):
        """
        查询数据
        :param sql: select sql语句
        :return: 还回查询到的select数据
        """
        db=self.__connect()
        cursor=db.cursor()
        cursor.execute(sql)
        try:
            read=cursor.fetchall()
        except:
            print u"查询数据失败"
        db.close()
        return read

    def oprationData(self,sql):
        """
        对数据库中的数据进行操作：
        :param sql: sql语句
        :return: 无还回值
        """
        db=self.__connect()
        # 使用cursor()方法获取操作游标
        cursor=db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交数据库执行
            db.commit()
        except Exception,e:
            print u"执行sql失败:%s"%e
            # 发生错误时回滚
            db.rollback()
        db.close()

        
        
if __name__=="__main__":
    help(mysql)
    a=mysql("192.168.8.51","root","EC52F^71107$7d4","newerp")
    sql2='''select * from report_sku limit 1'''
    sql='''select sku,min_purchase_quantity,pretax_price,price from goods where sku like "DEAP001X%" or sku="DEAP001"'''
    read=a.queryData(sql2)
    for i in read:
        print i[:]
