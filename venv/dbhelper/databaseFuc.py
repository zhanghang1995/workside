#定义数据库的连接相关操作
import pymysql

class DataConnect(object):
    #数据库连接操作
    def connect(self,host,port,username,password,dbname,charset):
        conn = pymysql.connect(host=host,port=port,user=username,password=password,db=dbname,charset=charset)
        return conn
