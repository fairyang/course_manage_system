from tkinter import *
from tkinter import messagebox
from view2 import *
'''import pymssql

#连接数据库
db = pymssql.connect(host='127.0.0.1',port = '1433', user='sa', password='012345678900000', database='class')
#db = pymssql.connect(host, port, user, password, database, charset)
#获取游标
cursor = db.cursor()'''

class Xiugaimima(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.xiugaimima = StringVar()
        self.name1= StringVar()
        self.createPage()
        # 对修改密码界面的进行编辑

    #def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        #Label(self, show='*', text='新密码: ').grid(row=1, stick=W, pady=10)
       # Entry(self, textvariable=self.xiugaimima).grid(row=1, column=1, stick=E)
        #Label(self, show='*', text='新密码: ').grid(row=2, stick=W, pady=10)
        #Entry(self, textvariable=self.xiugaimima2).grid(row=2, column=1, stick=E)
        #Label(self, text='姓名：').grid(row=3, stick=W, pady=10)
       # Entry(self, textvariable=self.name).grid(row=3, column=1, stick=E)
       # Button(self, text='确认', command=self.xiugai).grid(row=6, column=1, stick=E, pady=10)
    #对修改密码界面的进行编辑
    def createPage(self):

        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='新密码: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.xiugaimima).grid(row=1, column=1, stick=E)
        Label(self, text='姓名：').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.name1).grid(row=3, column=1, stick=E)
        #xiugaimima = self.xiugaimima.get()
        Button(self, text='确认',command=self.xiugai).grid(row=6, column=1, stick=E, pady=10)

    def xiugai(self):
        name = self.name1.get()
        newpass=self.xiugaimima.get()
        # if self.xiugaimima != self.xiugaimima2:
        #   messagebox.showerror(title='错误', message='两次密码不一致，请重新输入')
        # else:
        '''sql = "update A登陆 set 密码="+newpass+" where id="+name
        cursor.execute(sql)
        db.commit()
        sql = "select 密码 from A登陆 where id='02'"
        cursor.execute(sql)
        results = cursor.fetchall()
        # if cursor: print("连接成功!")'''
        messagebox.showinfo(title='成功', message='你已经成功的修改了密码'+name+'\n'+newpass)


class Shenhe(Frame):  # 继承Frame类
    # 初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.tiao1 = StringVar()
        self.tiao2 = StringVar()
        self.tiao3 = StringVar()
        self.tiao4 = StringVar()
        self.tiao5 = StringVar()
        self.tiao6 = StringVar()
        self.tiao7 = StringVar()
        self.createPage()

    # 对审核界面的进行编辑
    def createPage(self):
        Label(self, text='课程号: ').grid(row=1,stick=W, pady=10)
        Entry(self, textvariable=self.tiao1).grid(row=1, column=1, stick=E)
        Label(self, text='开课学院: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.tiao2).grid(row=2, column=1, stick=E)
        Label(self, text='班级: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.tiao3).grid(row=3, column=1, stick=E)
        Label(self, text='教室号: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.tiao4).grid(row=4, column=1, stick=E)
        Label(self, text='周: ').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.tiao5).grid(row=5, column=1, stick=E)
        Label(self, text='星期: ').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.tiao6).grid(row=6, column=1, stick=E)
        Label(self, text='节: ').grid(row=7, stick=W, pady=10)
        Entry(self, textvariable=self.tiao7).grid(row=7, column=1, stick=E)
        Button(self, text='同意').grid(row=8, column=1, stick=W, pady=10)
        Button(self, text='不同意').grid(row=8, column=3, stick=E, pady=10)
