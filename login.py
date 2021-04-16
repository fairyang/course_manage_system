from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mainpage import *
from zhuce import *
from mainpage2 import *
from mainpage3 import *
from canshu import *
#from main import db, cursor
import pymysql


#连接数据库
'''db = pymssql.connect(host='127.0.0.1',port = '1433', user='sa', password='012345678900000', database='class')
#db = pymssql.connect(host, port, user, password, database, charset)
#获取游标
cursor = db.cursor()
if cursor: print("连接成功!")'''

class login(object) :
    #初始化
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.name = StringVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        self.p = Frame(self.root)  # 创建Frame
        self.p.pack()

        # 创建一个下拉列表
        self.identity = StringVar()
        ttk.Combobox(self.p,textvariable=self.identity,width=17,values=('学生','教师','管理员')).grid(row=1, column=1, stick=E)

        # 三个标签，用于提示用户
        Label(self.p, text="身份").grid(row=1, stick=W, pady=10)
        Label(self.p, text="账号").grid(row=2, stick=W, pady=10)
        Label(self.p, text="密码").grid(row=3, stick=W, pady=10)

        # 设定账号密码输入框

        Entry(self.p, textvariable=self.name).grid(row=2, column=1, stick=E)
        Entry(self.p, show='*', textvariable=self.password).grid(row=3, column=1, stick=E)

        # 创建并放置两个按钮分别触发两种情况
        Button(self.p, text='登录', command=self.yanzheng).grid(row=4, stick=W, pady=10)
        Button(self.p, text='注册',command=self.tiaozhuan).grid(row=4, column=1, stick=E)

    #跳转页面函数
    def tiaozhuan(self):
        self.p.destroy()
        zhuce(self.root)

    # 登录验证函数
    def yanzheng(self):
        uname = self.name.get()
        upassword = self.password.get()
        uidentity = self.identity.get()
        #获取信息
        '''if uidentity == "管理员":
            sql = "select 密码 from A登陆 where id="+uname
            #data = ""
        elif uidentity == "学生":
            sql = "select 密码 from S登陆 where id="+uname
            #data = ""
        elif uidentity == "教师":
            sql = "select 密码 from T登陆 where id="+uname
            #data = ""
        cursor.execute(sql)
        jieguo = cursor.fetchall()

        if upassword == jieguo[0][0] and uidentity == "管理员":
            self.p.destroy()
            db.close()
            Zhuyemian(self.root)
        elif upassword == jieguo[0][0] and uidentity == "学生":
            self.p.destroy()
            Zhuyemian2(self.root)
        elif upassword == jieguo[0][0] and uidentity == "教师":
            self.p.destroy()
            Zhuyemian3(self.root)
        else:
            messagebox.showinfo(title='错误', message='账号或密码错误！')'''

        if uname == '123' and upassword == '123' and uidentity == "管理员":
            self.p.destroy()
            Zhuyemian(self.root)
        elif uname == '1' and upassword == '1' and uidentity == "学生":
            self.p.destroy()
            Zhuyemian2(self.root)
        elif uname == '12' and upassword == '12' and uidentity == "教师":
            self.p.destroy()
            Zhuyemian3(self.root)
        else:
            messagebox.showinfo(title='错误', message='账号或密码错误！')
