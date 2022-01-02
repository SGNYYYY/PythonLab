# coding=utf-8
import requests
import datetime
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
import string
import json
# 获取城市ID
urlLocation01 = "https://geoapi.qweather.com/v2/city/lookup?"
urlLocation02 = "https://website-api.airvisual.com/v1/routes/china/"
# 获取当前位置AQI
urlNowAQI = "https://devapi.qweather.com/v7/air/now?"
# 获取历史七天AQI
urlHistAQI = "https://datasetapi.qweather.com/v7/historical/air?"

# 查询参数,用于查询当前空气质量数据
parameter = {'location': "北京", 'key': '换上你的key(免费开发版即可)'}


def getCityName(cityname="北京"):
    cityname = input("请输入要查询的城市: ")
    return cityname


def getLocationID(cityname):
    parameter['location'] = cityname
    locationdata_json = requests.get(urlLocation01, params=parameter).json()
    # LocationData = json.dumps(requests.get(urlLocation,params=Location).json(), sort_keys=True, indent=4, separators=(
    # ',', ': '),ensure_ascii=False) print(LocationData)
    try:
        locationid = locationdata_json["location"][0]["id"]
    except:
        locationid = "error"
        print("查无此市")
    finally:
        return locationid


def getNowAQI(locationid, cityname):
    # AQIData = json.dumps(requests.get(urlNowAQI,params=LocationID).json(), sort_keys=True, indent=4, separators=(',',
    # ': '),ensure_ascii=False) print(AQIData)
    if locationid == "error":
        return "查无此市","，请重新输入","","","","","","",""
    
    parameter['location'] = locationid
    global nowAQI_json
    nowAQI_json = requests.get(urlNowAQI, params=parameter).json()

    AQI = nowAQI_json["now"]["aqi"]
    Catagory = nowAQI_json["now"]["category"]
    PM2p5 = nowAQI_json["now"]["pm2p5"]
    PM10 = nowAQI_json["now"]["pm10"]
    CO = nowAQI_json["now"]["co"]
    NO2 = nowAQI_json["now"]["no2"]
    SO2 = nowAQI_json["now"]["so2"]
    O3 = nowAQI_json["now"]["o3"]

    text = """
    实时空气质量:
    亲爱的 {},您所在的地区为 {}
    空气质量为 {},{}
    PM2.5 {},PM10 {}
    CO {}, NO2 {}
    SO2 {}, O3 {} """.format("USER", cityname, AQI, Catagory, PM2p5, PM10, CO, NO2, SO2, O3)
    # print(text)
    return cityname, AQI, Catagory, PM2p5, PM10, CO, NO2, SO2, O3

# 获取前1天或N天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天
def getDate(beforeOfDay):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=-beforeOfDay)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime('%Y-%m-%d')
        return re_date


def getAvgAQI_day(aqi):
    return aqi/24.0


def getWeekAQI(locationid,cityname):
    #print("历史七天空气质量数据: \n")
    if locationid == "error":
        return "查无此市","，请重新输入"
    
    histAQI = []
    days_list = []
    for index in range(1, 8):
        date = getDate(8-index)
        days_list.append(date)
        date = date.replace("-", "")
        historical = {'location': locationid, 'date': date, 'key': '换上你的key(需要商业共享版key)'}
        histAQI_json = requests.get(urlHistAQI, params=historical).json()
        totalAQI = int(0)
        for i in range(0, 23):
            totalAQI += int(histAQI_json["airHourly"][i]["aqi"])
        histAQI.append(getAvgAQI_day(totalAQI))

    plt.plot(days_list, histAQI)
    plt.xlabel(u"日期")  # X轴标签
    plt.ylabel(u"空气质量指数")  # Y轴标签
    plt.title(u"{}历史7天空气质量指数(AQI)".format(cityname))  # 标题

    plt.show()
    return "查询成功"


if __name__ == '__main__':
    cityName = getCityName()
    LocationID = getLocationID(cityName)
    getNowAQI(LocationID, cityName)
    getWeekAQI(LocationID,cityName)
