# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 11:30
import MySQLdb
from public.publicYaml import PublicGetYaml
def publicSql(sql):
    '''
    jcp数据库
    :param sql:
    :return:
    '''
    path = "../config/sql.yaml"
    db=MySQLdb.connect(
        host=PublicGetYaml(path).get_Yaml()['sqlinfo']['host'],
        user=PublicGetYaml(path).get_Yaml()['sqlinfo']['user'],
        passwd=PublicGetYaml(path).get_Yaml()['sqlinfo']['passwd'],
        db=PublicGetYaml(path).get_Yaml()['sqlinfo']['db'],
        port=PublicGetYaml(path).get_Yaml()['sqlinfo']['port'],
        charset=PublicGetYaml(path).get_Yaml()['sqlinfo']['charset']
    )
    cursor = db.cursor()
    cursor.execute(sql)
    result_sql= cursor.fetchone()
    return result_sql

def publicSqlAll(sql):
    '''
    jcp数据库
    :param sql:
    :return:
    '''
    path = "../config/sql.yaml"
    db=MySQLdb.connect(
        host=PublicGetYaml(path).get_Yaml()['sqlinfo']['host'],
        user=PublicGetYaml(path).get_Yaml()['sqlinfo']['user'],
        passwd=PublicGetYaml(path).get_Yaml()['sqlinfo']['passwd'],
        db=PublicGetYaml(path).get_Yaml()['sqlinfo']['db'],
        port=PublicGetYaml(path).get_Yaml()['sqlinfo']['port'],
        charset=PublicGetYaml(path).get_Yaml()['sqlinfo']['charset']
    )
    cursor = db.cursor()
    cursor.execute(sql)
    result_sql= cursor.fetchall()
    return result_sql

def publicSqlHouseAll(sql):
    '''
    房屋数据库
    :param sql:
    :return:
    '''
    path = "../config/sql.yaml"
    db=MySQLdb.connect(
        host=PublicGetYaml(path).get_Yaml()['sqlhouse']['host'],
        user=PublicGetYaml(path).get_Yaml()['sqlhouse']['user'],
        passwd=PublicGetYaml(path).get_Yaml()['sqlhouse']['passwd'],
        db=PublicGetYaml(path).get_Yaml()['sqlhouse']['db'],
        port=PublicGetYaml(path).get_Yaml()['sqlhouse']['port'],
        charset=PublicGetYaml(path).get_Yaml()['sqlhouse']['charset']
    )
    cursor = db.cursor()
    cursor.execute(sql)
    result_sql= cursor.fetchall()
    return result_sql


def publicSqlLocust(sql):
    '''
    性能数据
    :param sql:
    :return:
    '''
    path = "../config/sql.yaml"
    db=MySQLdb.connect(
        host=PublicGetYaml(path).get_Yaml()['sqllocust']['host'],
        user=PublicGetYaml(path).get_Yaml()['sqllocust']['user'],
        passwd=PublicGetYaml(path).get_Yaml()['sqllocust']['passwd'],
        db=PublicGetYaml(path).get_Yaml()['sqllocust']['db'],
        port=PublicGetYaml(path).get_Yaml()['sqllocust']['port'],
        charset=PublicGetYaml(path).get_Yaml()['sqllocust']['charset']
    )
    cursor = db.cursor()
    cursor.execute(sql)
    result_sql= cursor.fetchall()
    return result_sql
# sql="select * from app_base  "
# print len(publicSqlLocust(sql))

def publicSqlInsertLocust(sql):
    '''
    性能数据
    :param sql:
    :return:
    '''
    path = "../config/sql.yaml"
    db=MySQLdb.connect(
        host=PublicGetYaml(path).get_Yaml()['sqllocust']['host'],
        user=PublicGetYaml(path).get_Yaml()['sqllocust']['user'],
        passwd=PublicGetYaml(path).get_Yaml()['sqllocust']['passwd'],
        db=PublicGetYaml(path).get_Yaml()['sqllocust']['db'],
        port=PublicGetYaml(path).get_Yaml()['sqllocust']['port'],
        charset=PublicGetYaml(path).get_Yaml()['sqllocust']['charset']
    )
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()



# a= publicSqlAll("SELECT DISTINCT(d.id_),d.name_  from  jcp_core_sys_org_extension a  LEFT JOIN jcp_core_sys_org_extension b on a.parent_id_ = b.id_ LEFT JOIN jcp_core_sys_org_extension c on b.parent_id_ = c.id_ LEFT JOIN jcp_core_sys_org_extension d on c.parent_id_ = d.id_;")
# for i in a:
#     print i



# d_id = []   #区域的id
# for i in a:
#     if i[0] == None:
#         continue
#     d_id.append(i[0])
# print(d_id)



