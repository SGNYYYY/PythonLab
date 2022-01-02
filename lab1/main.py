from tkinter import *
from PIL import Image, ImageTk
import getData


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)  # supper()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        root.label01 = Label(root, text="城市", bg='Skyblue')
        v1 = StringVar()
        root.entry01 = Entry(root, textvariable=v1)
        v1.set("北京")
        msg = []

        def Query():
            LocationID = getData.getLocationID(str(root.entry01.get()))
            msg = getData.getNowAQI(LocationID, str(root.entry01.get()))
            if msg[0] == "查无此市":
                root.labelAQI = Label(root, text="{}{}".format(msg[0],msg[1]), width=40, height=10, relief='groove',
                                  justify='center', bg='Lightblue', font=("微软雅黑", 11, 'bold'))
            else:
                root.labelAQI = Label(root, text="{}今日的空气质量指数为 {} , {}".format(msg[0], msg[1], msg[2]), width=40, height=10, relief='groove',
                                        justify='center', bg='Lightblue', font=("微软雅黑", 11, 'bold'))
                
            root.labelPM25 = Label(root, text="PM2.5 : {}(ug/m3)".format(msg[3]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))
            root.labelPM10 = Label(root, text="PM10  : {}(ug/m3)".format(msg[4]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))
            root.labelCO = Label(root, text="CO  : {}(ug/m3)".format(msg[5]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))
            root.labelNO2 = Label(root, text="NO2  : {}(ug/m3)".format(msg[6]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))
            root.labelSO2 = Label(root, text="SO2  : {}(ug/m3)".format(msg[7]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))
            root.labelO3 = Label(root, text="O3  : {}(ug/m3)".format(msg[8]), width=30, height=10, relief='groove',
                                    justify='center', bg='Lightblue', font=("微软雅黑", 10))

            root.labelAQI.place(x=155, y=160, width=300, height=30)
            root.labelAQI.place(x=155, y=160, width=300, height=30)
            root.labelPM25.place(x=100, y=230, width=130, height=30)
            root.labelPM10.place(x=235, y=230, width=130, height=30)
            root.labelCO.place(x=370, y=230, width=130, height=30)
            root.labelNO2.place(x=100, y=260, width=130, height=30)
            root.labelSO2.place(x=235, y=260, width=130, height=30)
            root.labelO3.place(x=370, y=260, width=130, height=30)

        def Query7day():
            LocationID = getData.getLocationID(root.entry01.get())
            msg = getData.getWeekAQI(LocationID, root.entry01.get())
            if msg[0] == "查无此市":
                root.labelAQI = Label(root, text="{}{}".format(msg[0],msg[1]), width=40, height=10, relief='groove',
                                  justify='center', bg='Lightblue', font=("微软雅黑", 11, 'bold'))
                root.labelAQI.place(x=155, y=160, width=300, height=30)

        root.btnQuery = Button(root, text="查询", command=Query)
        root.btnQuery7day = Button(root, text="查询历史7天空气质量指数", command=Query7day)
        root.btnQuit = Button(root, text="退出", command=root.destroy)

        root.label01.place(x=170, y=50, width=50, height=30)
        root.entry01.place(x=230, y=50, width=50, height=30)
        root.btnQuery.place(x=210, y=100, width=50, height=30)
        root.btnQuery7day.place(x=270, y=100, width=150, height=30)
        root.btnQuit.place(x=540, y=360, width=50, height=30)


if __name__ == '__main__':
    root = Tk()
    root.canvas_root = Canvas(root, width=600, height=400)
    im_root = get_image('.\\weather_icon\\IMG_9320.png', 600, 400)
    root.canvas_root.create_image(300, 200, image=im_root)
    root.canvas_root.pack()
    root.geometry("600x400+350+150")
    root.title("空气质量查询1.0")
    rootImage = PhotoImage(file='.\\weather_icon\\103.png')
    root.iconphoto(False, rootImage)
    app = Application(root)
    root.resizable(False, False)
    root.mainloop()  # 调用组件的mainloop()方法，进入事件循环
