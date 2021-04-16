from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

#连接数据库
'''db = pymssql.connect(host='127.0.0.1',port = '1433', user='sa', password='012345678900000', database='class')
#db = pymssql.connect(host, port, user, password, database, charset)
#获取游标
cursor = db.cursor()
if cursor: print("连接成功!")'''

class zhuce(object) :
    # 初始化
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.name = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.p1 = Frame(self.root)  # 创建Frame
        self.p1.pack()

        # 创建一个下拉列表
        self.identity = StringVar()
        ttk.Combobox(self.p1,textvariable=self.identity,width=17,values=('员工','经理','管理员')).grid(row=1, column=1, stick=E)

        # 三个标签，用于提示用户
        Label(self.p1, text="身份").grid(row=1, stick=W, pady=10)
        Label(self.p1, text="账号").grid(row=2, stick=W, pady=10)
        Label(self.p1, text="密码").grid(row=3, stick=W, pady=10)

        # 设定账号密码输入框

        Entry(self.p1, textvariable=self.name).grid(row=2, column=1, stick=E)
        Entry(self.p1,  textvariable=self.password).grid(row=3, column=1, stick=E)

        # 创建并放置按钮
        Button(self.p1, text='确认注册',command=self.tiaozhuan).grid(row=4, column=1, stick=E)

    #注册成功并关闭程序
    def tiaozhuan(self):
        uname = self.name.get()
        upassword = self.password.get()
        uidentity = self.identity.get()

        if uidentity == "管理员":
            sql = "insert into A登陆 values("+uname+","+upassword+")"
        elif uidentity == "员工":
            sql = "insert into S登陆 values("+uname+","+upassword+")"
        elif uidentity == "经理":
            sql = "insert into T登陆 values("+uname+","+upassword+")"
        '''cursor.execute(sql)
        db.commit()'''
        messagebox.showinfo(title='注册成功', message='注册成功！')
        self.root.destroy()



