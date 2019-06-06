#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : db.py
@Time       : 2019/6/5 下午5:00
@Version    : 1.0  
@Desc       : None
"""
import psycopg2


# 说明：
# 使用时直接调用saveAll方法，其他方法将被saveAll调用，你可以无视
# saveAll参数说明：
#   table 表名
#   datas 数据的数组 例 ：[{"key1":"value1","key2":"value2"},{"key1":"value1","key2":"value2"}] 建议数组大小不要超过一千。
#   searchKeys 用于确定唯一行的键的数组，如用户表的用户名，选课表的课程ID与学生ID等 例 ["user_id","class_id"]
#   ifIgnoreSearchKey 是否忽略searchKey 如果你的searchKeys 是自增长的ID 你肯定不希望插入的时候插入这个字段 "1"是，"0"否
#   ifNotUpdate 是否不做更新操作 如果这个设为 "0" ,datas中数据如果已在数据库中，将不会做更新操作
# getConnection 方法中的DB 是我从我的配置文件中导入的，你可以换成你的
def getConnection():
    conn = psycopg2.connect(database="postgres", user="postgres", password="admin123", host="127.0.0.1", port="5432")
    print("Opened database successfully", conn)
    return conn


def saveAll(table, datas, searchKeys, ifIgnoreSearchKey, ifNotUpdate):
    conn = getConnection()
    cursor = conn.cursor()
    where = []
    # 转义数据,避免sql发生错误
    for data in datas:
        for key in data:
            data[key] = MySQLdb.escape_string(str(data[key]))
    for searchKey in searchKeys:
        searchKeyDatas = []
        for data in datas:
            searchKeyDatas.append(data[searchKey])
        searchKeyDatasString = "`" + searchKey + "` in ('" + "','".join(searchKeyDatas) + "')"
        where.append(searchKeyDatasString)
    whereString = " AND ".join(where)
    selectSql = "SELECT `" + "`,`".join(searchKeys) + "` from " + table + " WHERE " + whereString
    cursor.execute(selectSql)
    conn.commit()
    results = cursor.fetchall()
    updateData = []
    insertData = []
    existKey = []
    for result in results:
        keyValue = []
        for value in result:
            keyValue.append(str(value))
        existKey.append(",".join(keyValue))
    for data in datas:
        keyValue = []
        for key in searchKeys:
            keyValue.append(data[key])
        currentKey = ",".join(keyValue)
        if currentKey in existKey:
            updateData.append(data)
        else:
            insertData.append(data)
    if ifNotUpdate == "0":
        updateAll(updateData, table, searchKeys)
    insertAll(insertData, table, searchKeys, ifIgnoreSearchKey)
    conn.close()
    pass


def updateAll(datas, table, searchKeys):
    # 同时更新多条数据
    if len(datas) == 0:
        return
    conn = getConnection()
    cursor = conn.cursor()
    sets = {}
    updateSql = "UPDATE `" + table + "` set "
    whereValues = []
    whereKey = "WHERE CONCAT(`" + "`,',',`".join(searchKeys) + "`) IN "
    for data in datas:
        whereValue = []
        for searchKey in searchKeys:
            whereValue.append(data[searchKey])
        whereValueString = ",".join(whereValue)
        whereValues.append(whereValueString)
        for key in data:
            if key in searchKeys:
                pass
            else:
                searchValue = []
                for searchKey in searchKeys:
                    searchValue.append(str(data[searchKey]))
                searchValueString = ",".join(searchValue)
                try:
                    sets[key][searchValueString] = data[key]
                except KeyError as e:
                    sets[key] = {}
                    sets[key][searchValueString] = data[key]
    searchKeysString = "(`" + "`,',',`".join(searchKeys) + "`)"
    whereValuesString = "('" + "','".join(whereValues) + "')"
    setStringArray = []
    for key1 in sets:
        setString = ""
        for key2 in sets[key1]:
            if setString == "":
                setString = "`" + key1 + "` = CASE WHEN (CONCAT" + searchKeysString + "='" + key2 + "') THEN '" + \
                            sets[key1][key2] + "'"
            else:
                setString = setString + " WHEN (CONCAT" + searchKeysString + "='" + key2 + "') THEN '" + sets[key1][
                    key2] + "'"
        setString += " END "
        setStringArray.append(setString)
    setStrings = ",".join(setStringArray)
    whereStrings = whereKey + whereValuesString
    updateSql += setStrings
    updateSql += whereStrings
    print(updateSql)
    try:
        cursor.execute(updateSql)
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        print(updateSql)
    conn.commit()
    conn.close()


def insertAll(datas, table, searchKeys, ifIgnoreSearchKey):
    # 多条数据同时添加
    if len(datas) == 0:
        return
    conn = getConnection()
    cursor = conn.cursor()
    keys = []
    for key in datas[0]:
        if key not in searchKeys or ifIgnoreSearchKey != "1":
            keys.append(key)
    insertSql = "INSERT INTO " + table + " (`" + "`,`".join(keys) + "`) VALUES "
    valueStrings = []
    for data in datas:
        value = []
        for key in keys:
            value.append(data[key])
        valueString = "('" + "','".join(value) + "')"
        valueStrings.append(valueString)
    insertSql += ",".join(valueStrings)
    print(insertSql)
    try:
        cursor.execute(insertSql)
        conn.commit()
        conn.close()
    except Exception as e:
        print(insertSql)
        print(e)
