from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
'''import pymssql
#连接数据库
db = pymssql.connect(host='127.0.0.1',port = '1433', user='sa', password='012345678900000', database='class')
#db = pymssql.connect(host, port, user, password, database, charset)
#获取游标
cursor = db.cursor()'''

class Jiaoshi(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.chaxinxi = StringVar()
        self.chaxinxi2 = StringVar()
        self.createPage()
    #对查询界面的进行编辑
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='教室编号: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi).grid(row=1, column=1, stick=E)
        Label(self, text='教室条件: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi2).grid(row=2, column=1, stick=E)
        Button(self, text='搜索',command=self.search).grid(row=3, column=2, stick=E, pady=10)
    def search(self):
        id = self.chaxinxi.get()
        gongneng=self.chaxinxi2.get()
        '''sql = "select 地点 from 教室 where 教室号="+id+"and 教室功能="+gongneng
        cursor.execute(sql)
        jieguo = cursor.fetchall()
        messagebox = showinfo(title="结果", message="结果是"+jieguo[0][0])'''

class Jiaoshi1(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.chaxinxi = StringVar()
        self.chaxinxi2 = StringVar()
        self.createPage()
    #对查询界面的进行编辑
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='教师姓名: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi).grid(row=1, column=1, stick=E)
        Label(self, text='教师所在院系: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi2).grid(row=2, column=1, stick=E)
        Button(self, text='搜索',command=self.search).grid(row=3, column=2, stick=E, pady=10)
    def search(self):
        name = self.chaxinxi.get()
        #xi = self.chaxinxi2.get()
        '''sql = "select 联系方式 from 教师 where 教师姓名="+name
        cursor.execute(sql)
        jieguo = cursor.fetchall()
        messagebox = showinfo(title="结果", message="结果是"+jieguo[0][0])'''
class Xuesheng(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.chaxinxi = StringVar()
        self.chaxinxi2 = StringVar()
        self.createPage()
    #对查询界面的进行编辑
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='学生姓名: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi).grid(row=1, column=1, stick=E)
        Label(self, text='学生学号: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi2).grid(row=2, column=1, stick=E)
        Button(self, text='搜索', command=self.search).grid(row=3, column=2, stick=E, pady=10)

    def search(self):
        name = self.chaxinxi.get()
        id = self.chaxinxi2.get()
        '''sql = "select 班级 from 学生 where 学号="+id+"and 学生姓名="+name
        cursor.execute(sql)
        jieguo = cursor.fetchall()
        messagebox = showinfo(title="结果", message="结果是"+jieguo[0][0])'''

class Banji(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.chaxinxi = StringVar()
        self.createPage()
    #对查询界面的进行编辑
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='行政班级名称: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi).grid(row=1, column=1, stick=E)
        Button(self, text='搜索',command=self.search).grid(row=3, column=2, stick=E, pady=10)
    def search(self):
        name = self.chaxinxi.get()
        '''sql = "select 学院 from 班级 where 班级="+name
        cursor.execute(sql)
        jieguo = cursor.fetchall()
        messagebox = showinfo(title="结果", message="结果是"+jieguo[0][0])'''

class Kecheng(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.chaxinxi = StringVar()
        self.chaxinxi2 = StringVar()
        self.createPage()
    #对查询界面的进行编辑
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='课程名称: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi).grid(row=1, column=1, stick=E)
        Label(self, text='课程所在系: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.chaxinxi2).grid(row=2, column=1, stick=E)
        Button(self, text='搜索',command=self.search).grid(row=3, column=2, stick=E, pady=10)
    def search(self):
        id = self.chaxinxi.get()
        #xi =self.chaxinxi2.get()
        '''sql = "select 课程名 from 课程 where 课程号="+id
        cursor.execute(sql)
        jieguo = cursor.fetchall()
        messagebox = showinfo(title="结果", message="结果是"+jieguo[0][0])'''

class Tiaok(Frame):  # 继承Frame类
    #初始化
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
    #对调课界面的进行编辑
    def createPage(self):
        Label(self, text='课程号: ').grid(row=1, stick=W, pady=10)
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
        Button(self, text='确定').grid(row=8, column=2, stick=E, pady=10)

class Teacher(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.tiao1 = StringVar()
        self.tiao2 = StringVar()
        self.tiao3 = StringVar()
        self.tiao4 = StringVar()
        self.createPage()
    #对调课界面的进行编辑
    def createPage(self):
        Label(self, text='教师号: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.tiao1).grid(row=1, column=1, stick=E)
        Label(self, text='教师姓名: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.tiao2).grid(row=2, column=1, stick=E)
        Label(self, text='联系方式: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.tiao3).grid(row=3, column=1, stick=E)
        Label(self, text='教师职位: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.tiao4).grid(row=4, column=1, stick=E)
        Button(self, text='添加',command=self.add).grid(row=8, column=1, stick=E,pady=10)
        Button(self, text='修改',command=self.xiugai).grid(row=8, column=2,stick=E, pady=10)
        Button(self, text='删除',command=self.shanchu).grid(row=8, column=3, stick=E, pady=10)
    def add(self):
        id=self.tiao1.get()
        name=self.tiao1.get()
        phone=self.tiao3.get()
        pro=self.tiao4.get()
        '''sql="insert into 教师 values("+id+","+name+","+phone+","+pro+")"
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='添加成功', message='添加成功！')'''
    def xiugai(self):
        id = self.tiao1.get()
        name = self.tiao1.get()
        phone = self.tiao3.get()
        pro = self.tiao4.get()
        sql = "update 教师 set 教师姓名="+name+",联系方式="+phone+",教师职位="+pro+"where 教师号="+id
        '''cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='修改成功', message='修改成功！')'''
    def shanchu(self):
        id = self.tiao1.get()
        name = self.tiao1.get()
        phone = self.tiao3.get()
        pro = self.tiao4.get()
        '''sql = "delete from 教师 where 教师号="+id
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='删除成功', message='删除成功！')'''
class Course(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.tiao1 = StringVar()
        self.tiao2 = StringVar()
        self.createPage()
    #对调课界面的进行编辑
    def createPage(self):
        Label(self, text='课程号: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.tiao1).grid(row=1, column=1, stick=E)
        Label(self, text='课程名: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.tiao2).grid(row=2, column=1, stick=E)
        Button(self, text='添加',command=self.add).grid(row=8, column=1, stick=E, pady=10)
        Button(self, text='修改',command=self.xiugai).grid(row=8, column=2,stick=E, pady=10)
        Button(self, text='删除',command=self.shanchu).grid(row=8, column=3, stick=E, pady=10)

    def add(self):
        id=self.tiao1.get()
        name=self.tiao2.get()
        '''sql="insert into 课程 values("+id+","+name+")"
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='添加成功', message='添加成功！')'''
    def xiugai(self):
        id = self.tiao1.get()
        name = self.tiao2.get()
        '''sql = "update 课程 set 课程名="+name+"where 课程号="+id
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='删除成功', message='删除成功！')'''
    def shanchu(self):
        id = self.tiao1.get()
        name = self.tiao2.get()
        '''sql = "delete from 课程 where 课程号="+id+"and 课程名="+name
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='删除成功', message='删除成功！')'''

class Classroom(Frame):  # 继承Frame类
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.tiao1 = StringVar()
        self.tiao2 = StringVar()
        self.tiao3 = StringVar()
        self.createPage()
    #对调课界面的进行编辑
    def createPage(self):
        Label(self, text='教室号: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.tiao1).grid(row=1, column=1, stick=E)
        Label(self, text='地点: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.tiao2).grid(row=2, column=1, stick=E)
        Label(self, text='教室功能: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.tiao3).grid(row=3, column=1, stick=E)
        Button(self, text='添加',command=self.add).grid(row=8, column=1, stick=E, pady=10)
        Button(self, text='修改',command=self.xiugai).grid(row=8, column=2,stick=E, pady=10)
        Button(self, text='删除',command=self.shanchu).grid(row=8, column=3, stick=E, pady=10)
    def add(self):
        id=self.tiao1.get()
        place=self.tiao2.get()
        gongneng=self.tiao3.get()
        '''sql="insert into 教室 values("+id+","+place+","+gongneng+")"
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='添加成功', message='添加成功！')'''
    def xiugai(self):
        id = self.tiao1.get()
        place = self.tiao2.get()
        gongneng = self.tiao3.get()
        '''sql = "update 教室 set 地点="+place+","+"教室功能="+gongneng+"where 教室号="+id
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='修改成功', message='修改成功！')'''
    def shanchu(self):
        id = self.tiao1.get()
        place = self.tiao2.get()
        gongneng = self.tiao3.get()
        '''sql = "delete from 教室 where 教室号="+id
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo(title='删除成功', message='删除成功！')'''
