import pandas as pd
import matplotlib.pyplot as plt
from pylab import *  # 支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


def importData():
    # 导入数据
    CCL = pd.read_csv('.\\data\\ccl.txt', usecols=[0, 3], sep='|')
    ITCont = pd.read_csv('.\\data\\itcont_2020_20200722_20200820.txt', usecols=[0, 13, 14], sep='|')
    webAll = pd.read_csv('.\\data\\weball20.txt', usecols=[0, 1], sep='|')
    ITCont = ITCont[ITCont['TRANSACTION_AMT'] >= 0]
    # 合并表格
    webAll_ITCont = pd.merge(pd.merge(webAll, CCL), ITCont)
    # 求每个候选人获得捐款总额
    TotalCon = webAll_ITCont.groupby('CAND_ID')['TRANSACTION_AMT'].sum().reset_index()
    TotalCon = TotalCon.sort_values(by='TRANSACTION_AMT', ascending=False)
    CANDID_3 = list(TotalCon[0:3]['CAND_ID'])
    # print(CANDID_3)

    CAND_1 = webAll_ITCont[webAll_ITCont['CAND_ID'] == CANDID_3[0]].sort_values(by='TRANSACTION_DT')
    CAND_2 = webAll_ITCont[webAll_ITCont['CAND_ID'] == CANDID_3[1]].sort_values(by='TRANSACTION_DT')
    CAND_3 = webAll_ITCont[webAll_ITCont['CAND_ID'] == CANDID_3[2]].sort_values(by='TRANSACTION_DT')
    CAND_1 = CAND_1.groupby(['CAND_NAME', 'TRANSACTION_DT'])['TRANSACTION_AMT'].sum().reset_index()
    CAND_2 = CAND_2.groupby(['CAND_NAME', 'TRANSACTION_DT'])['TRANSACTION_AMT'].sum().reset_index()
    CAND_3 = CAND_3.groupby(['CAND_NAME', 'TRANSACTION_DT'])['TRANSACTION_AMT'].sum().reset_index()
    DATE = list(CAND_1['TRANSACTION_DT'])
    CAND1 = list(CAND_1['TRANSACTION_AMT'])
    CAND2 = list(CAND_2['TRANSACTION_AMT'])
    CAND3 = list(CAND_3['TRANSACTION_AMT'])
    name1 = list(CAND_1[0:1]['CAND_NAME'])
    name2 = list(CAND_2[0:1]['CAND_NAME'])
    name3 = list(CAND_3[0:1]['CAND_NAME'])
    return DATE, CAND1, CAND2, CAND3, name1, name2, name3


def DateFormat(DATE):
    # 格式化日期 yyyy-mm-dd
    date = []
    for i in DATE:
        date.append(str(i)[3:7]+'-'+'0'+str(i)[0:1]+'-'+str(i)[1:3])

    return date


def sumAMT(CAND):
    CAND_sumed = []
    y = 0
    for i in CAND:
        y += i
        CAND_sumed.append(y)
    return CAND_sumed


def printPlt(Date, CAND1, CAND2, CAND3, name1, name2, name3):
    x = range(len(Date))
    plt.figure(figsize=(18, 5))
    plt.plot(x, CAND1, marker='o', label=name1[0])
    plt.plot(x, CAND2, marker='*', label=name2[0])
    plt.plot(x, CAND3, marker='.', label=name3[0])
    plt.ylim(-5000000, 7*1e7+1000000)
    plt.xlim(-1, 30)
    plt.legend()  # 让图例生效
    plt.xticks(x, Date, rotation=25)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"日期")  # X轴标签
    plt.ylabel("捐赠额")  # Y轴标签
    plt.title("获得捐赠额最多的三位候选人的捐赠额变化趋势")  # 标题
    plt.savefig('获得捐赠额最多的三位候选人的捐赠额变化趋势.png')
    # plt.show()  # 需要单独运行此文件时取消该注释


def main():
    DATE, CAND1, CAND2, CAND3, name1, name2, name3 = importData()
    CAND1 = sumAMT(CAND1)
    CAND2 = sumAMT(CAND2)
    CAND3 = sumAMT(CAND3)
    DATE = DateFormat(DATE)
    printPlt(DATE, CAND1, CAND2, CAND3, name1, name2, name3)


if __name__ == '__main__':
    main()
