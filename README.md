# Python编程与数据分析实验
## 东北大学计算机学院python课实验
## 实验题目1: 空气质量查询程序
实验内容: 
1. 实现一个GUI界面，用户可以输入城市名，程序需要获取此城市当前的空气质量数据，以图文并茂的方式展示在GUI界面中，空气质量数据至少包括AQI（空气质量指数），PM2.5，PM10三个数据。（可选择性展示CO，NO2，SO2，O3等浓度数据）。
2. 查询该城市的至少过去七天的AQI(空气质量指数)，并将数据画成折线图。

### lab1/getData.py 
> 获取数据文件 

**需要替换两个参数才可运行👇**

天气数据获取 -> [和风天气开发平台](https://dev.qweather.com/) 

需要在[控制台](https://console.qweather.com/#/console)->[应用管理](https://console.qweather.com/#/apps)->创建应用获得key

免费开发版的key可以获取当前的空气质量数据, 
要获取历史数据需要商业共享版的key

```python
# 查询参数, 用于查询当前空气质量数据
parameter = {'location': "北京", 'key': '换上你的key(免费开发版即可)'}
```
```python
# 查询参数, 用于查询历史空气质量数据
historical = {'location': locationid, 'date': date, 'key': '换上你的key(需要商业共享版key)'}
```

### lab1/main.py 
> 界面编写，点击可运行

## 实验题目2: 美国总统大选数据分析
实验内容:
现有一份美国大选捐款的统计数据，根据给出的数据，分析数据并实现以下要求:
1. 统计各个州的捐款总额，并在美国地图上画出各州捐款总额的热度图（heatmap），颜色越深的州代表捐款额越多，要求图表美观易懂。
2. 统计获得捐赠额最多的三位候选人的捐赠额变化趋势，使用折线图展示，横轴表示时间，纵轴表示捐赠额，要求图表美观易懂。
3. 分析出获得捐款额最多的候选人，然后将此候选人的捐赠者的姓名画成词云图。

### lab2/USAMap.py
> 对应第一小题，生成热力图

![各州捐款总额的热度图](https://github.com/SGNYYYY/PythonLab/blob/main/lab2/%E7%83%AD%E5%8A%9B%E5%9B%BE.png)
### lab2/Candidate_3.py
> 对应第二小题，生成折线图

![获得捐赠额最多的三位候选人的捐赠额变化趋势折线图](https://github.com/SGNYYYY/PythonLab/blob/main/lab2/%E8%8E%B7%E5%BE%97%E6%8D%90%E8%B5%A0%E9%A2%9D%E6%9C%80%E5%A4%9A%E7%9A%84%E4%B8%89%E4%BD%8D%E5%80%99%E9%80%89%E4%BA%BA%E7%9A%84%E6%8D%90%E8%B5%A0%E9%A2%9D%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png)
### lab2/toWordCloud.py
> 对应第三小题，生成词云图

![词云图](https://github.com/SGNYYYY/PythonLab/blob/main/lab2/%E8%AF%8D%E4%BA%91%E5%9B%BE.png)
### lab2/main.py
> 点击可运行，生成所有图
