# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/5/31 14:46
"""
导入xlrd库,作用:去读excel文件
导入xlutils,作用:写入excel文件
作用点:获取的行和列是数出来的
       写入填写的行和列是索引填写的
"""
import xlrd
from xlutils.copy import copy
from public.publicLogs import PublicLogs
log=PublicLogs()
class PublicExcel:
    def __init__(self,file_path):
        self.file_path=file_path

    #excel文件
    @property
    def get_excel(self):
        # xlrd.Book.encoding="utf-8"
        table=xlrd.open_workbook(self.file_path)
        return table

    #获取excel的总sheet数
    def mumber_sheet(self):
        mumber=len(self.get_excel.sheets())
        return mumber

    #需要使用的excel的第几个sheet,索引获取i
    def get_sheet(self,i):
        if i<=self.mumber_sheet():
            return self.get_excel.sheets()[i]
        else:
            log.error(u"输入的页数错误")

    #获取行数
    def get_lines(self,i):
        if i<=self.mumber_sheet():
           return self.get_sheet(i).nrows
        else:
            log.error(u"输入的页数错误")

    #获取列数
    def get_ncols(self,i):
        if i<=self.mumber_sheet():
           return self.get_sheet(i).ncols
        else:
            log.error( u"输入的页数错误")
    #通过行列获取值,填写的norw和ncol都是通过索引填写
    def get_value(self,i,norw,ncol):
        return self.get_sheet(i).cell(norw,ncol).value

    def write_excel(self,i,norw,ncol,data):
        tables=self.get_excel
        wb=copy(tables)
        ws=wb.get_sheet(i)
        ws.write(norw,ncol,data)
        wb.save(self.file_path)


if __name__ =='__main__':
    excel=PublicExcel('../report/excel.xls')
    # print excel.mumber_sheet()
    print(excel.get_value(0,0,0))
    # excel.write_excel(0,13,2,u"com.hxdsw.brc")
    excel.write_excel(0,1,1,"test")



