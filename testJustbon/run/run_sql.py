# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/7/3 10:57
from public.publicSql import *
from public.publicExcel import PublicExcel
class run:
    def __init__(self):
        self.excel = PublicExcel("../report/locust.xls")

    def insert_app_base(self):
        sql = "select * from app_base"
        len_id = len(publicSqlLocust(sql))+1
        data_list = []
        for i in range(8):
            data = self.excel.get_value(0,i,1)
            data_list.append(data)
        insert_sql = "insert into app_base VALUES(%d,'%s','%s','%s','2019/7/3',%d,%d,%d,%d)"%(len_id,data_list[0],data_list[1],data_list[2],data_list[4],data_list[5],data_list[6],data_list[7])
        publicSqlInsertLocust(insert_sql)

    def insert_phone_base(self):
        sql = "select * from app_base"
        len_id = len(publicSqlLocust(sql))
        data_list = []
        for i in range(17):
            data = self.excel.get_value(0,i+8,1)
            data_list.append(data)
        insert_sql = "insert into phone_base VALUES (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d)"%(len_id,data_list[0],data_list[1],data_list[2],data_list[3],data_list[4],data_list[5],data_list[6],"%.0f%%" % (data_list[7] * 100),"%.0f%%" % (data_list[8] * 100),data_list[9],data_list[10],data_list[11],data_list[12],data_list[13],data_list[14],"%.0f%%" % (data_list[15] * 100),"%.0f%%" % (data_list[16] * 100),len_id)
        publicSqlInsertLocust(insert_sql)

    def insert_phone_locust(self):
        sql = "select * from app_base"
        phone_base_id = len(publicSqlLocust(sql))
        for i in range(1,51):
            sql = "select * from phone_locust"
            len_id = len(publicSqlLocust(sql))+1
            data_time = self.excel.get_value(1,i,0)
            data_cpu = self.excel.get_value(1,i,5)
            data_fps = self.excel.get_value(1,i,4)
            data_memory = self.excel.get_value(1,i,3)
            insert_sql = "insert into phone_locust VALUES (%d,'%s','%s','%s','%s',%d)"%(len_id,data_cpu,data_fps,data_memory,data_time,phone_base_id)
            publicSqlInsertLocust(insert_sql)

    def run_data(self):
        self.insert_app_base()
        self.insert_phone_base()
        self.insert_phone_locust()
if __name__ == '__main__':
    r = run()
    # r.insert_app_base()
    # r.insert_phone_base()
    # r.insert_phone_locust()
    r.run_data()