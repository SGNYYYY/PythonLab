import plotly.graph_objects as go
import pandas as pd


def importData():
    # 导入数据
    ITCont = pd.read_csv('.\\data\\itcont_2020_20200722_20200820.txt', usecols=[0,9, 14], sep='|')
    CCL = pd.read_csv('.\\data\\ccl.txt', usecols=[3], sep='|')
    ITCont = pd.merge(CCL, ITCont)  # 连接候选人委员会链接信息表和个人捐款信息表,筛选出有效捐款
    ITCont = ITCont[ITCont['TRANSACTION_AMT'] >= 0]
    STCont = ITCont.groupby('STATE')['TRANSACTION_AMT'].sum()
    STCont.to_csv("各个州的捐款总额.csv")
    STCont = STCont.reset_index()
    return STCont


def outputHTML(STCont):
    fig = go.Figure(data=go.Choropleth(
        locations=STCont['STATE'],  # 设置位置，各州的编号（缩写）
        z=STCont['TRANSACTION_AMT'].astype(int),  # 设置填充色数据
        locationmode='USA-states',  # 设置国家名称
        colorscale='Reds',  # 图例颜色
        colorbar_title='TRANSACTION_AMT',  # 图例标题
    ))

    fig.update_layout(
        title_text='美国各州捐款总额',  # 地图标题
        geo_scope='usa',  # 设置地图的范围为美国
    )

    # 将地图导出为html文件
    fig.write_html("STACont.html")


def main():
    outputHTML(importData())


if __name__ == '__main__':
    main()



