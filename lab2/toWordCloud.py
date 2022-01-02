import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def importData():
    # 导入数据
    CCL = pd.read_csv('.\\data\\ccl.txt', usecols=[0, 3], sep='|')
    ITCont = pd.read_csv('.\\data\\itcont_2020_20200722_20200820.txt', usecols=[0, 7, 14], sep='|')
    webAll = pd.read_csv('.\\data\\weball20.txt', usecols=[0, 1], sep='|')
    ITCont = ITCont[ITCont['TRANSACTION_AMT'] >= 0]
    # 合并表格
    webAll_ITCont = pd.merge(pd.merge(webAll, CCL), ITCont)
    # 求每个候选人获得捐款总额
    TotalCon = webAll_ITCont.groupby('CAND_ID')['TRANSACTION_AMT'].sum().reset_index()
    TotalCon = TotalCon.sort_values(by='TRANSACTION_AMT', ascending=False)
    # print(TotalCon)
    CANDID = list(TotalCon[0:1]['CAND_ID'])

    webAll_ITCont = webAll_ITCont[webAll_ITCont['CAND_ID'] == CANDID[0]]

    # print(webAll_ITCont)

    Donor = list(webAll_ITCont['NAME'])
    return " ".join(Donor)


def show(Donor):
    path_img = "biden.jpg"
    background_image = np.array(Image.open(path_img))
    DonorWordCloud = WordCloud(   # 设置了背景，宽高
        background_color="white", width=1000, height=880,
        mask=background_image).generate(Donor)
    plt.figure()
    plt.imshow(DonorWordCloud)
    plt.axis("off")
    plt.savefig('词云图.png')
    plt.show()
    # print("运行完了")


def main():
    Donor = importData()
    show(Donor)


if __name__ == '__main__':
    main()
