from tkinter import *
from view import *  # 菜单栏对应的各个子页面
from view2 import *


class Zhuyemian(object):
    # 初始化
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        #连接view里的几个frame
        self.xiugaimima = Xiugaimima(self.root)
        self.shenhe = Shenhe(self.root)
        self.jiaoshi = Jiaoshi(self.root)
        self.jiaoshi1 = Jiaoshi1(self.root)
        self.xuesheng = Xuesheng(self.root)
        self.banji = Banji(self.root)
        self.kecheng = Kecheng(self.root)
        self.teacher = Teacher(self.root)
        self.course = Course(self.root)
        self.classroom = Classroom(self.root)
        #以修改密码为显示界面
        self.xiugaimima.pack()
        #创建菜单和菜单名，并连接分别的frame
        caidan = Menu(self.root)
        caidan.add_command(label='修改密码', command=self.xgmm)
        caidan.add_command(label='审核', command=self.sh)
        # 创建一个File菜单项
        filemenu = Menu(caidan, tearoff=0)
        # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
        caidan.add_cascade(label='查询信息', menu=filemenu)
        filemenu.add_command(label='教室查询', command=self.js)
        filemenu.add_command(label='教师查询', command=self.js1)
        filemenu.add_command(label='学生查询', command=self.xs)
        filemenu.add_command(label='班级查询', command=self.bj)
        filemenu.add_command(label='课程查询', command=self.kc)
        # 创建一个File菜单项
        filemenu1 = Menu(caidan, tearoff=0)
        # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
        caidan.add_cascade(label='课程信息维护', menu=filemenu1)
        filemenu1.add_command(label='教师信息更新', command=self.tc)
        filemenu1.add_command(label='课程信息更新', command=self.cs)
        filemenu1.add_command(label='教室信息更新', command=self.cr)
        caidan.add_command(label='帮助', command=self.sh)
        self.root['menu'] = caidan  # 设置菜单栏

    #显示自己所对应的frame界面，下面几个同理
    def xgmm(self):
        self.xiugaimima.pack()
        self.shenhe.pack_forget()
        self.jiaoshi.pack_forget()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()

    def sh(self):
        self.xiugaimima.pack_forget()
        self.shenhe.pack()
        self.jiaoshi.pack_forget()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()

    def js(self):
        self.jiaoshi.pack()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.xiugaimima.pack_forget()
        self.shenhe.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()
    def js1(self):
        self.jiaoshi1.pack()
        self.jiaoshi.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.xiugaimima.pack_forget()
        self.shenhe.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()

    def xs(self):
        self.xuesheng.pack()
        self.jiaoshi1.pack_forget()
        self.jiaoshi.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.xiugaimima.pack_forget()
        self.shenhe.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()
    def bj(self):
        self.banji.pack()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.jiaoshi.pack_forget()
        self.kecheng.pack_forget()
        self.xiugaimima.pack_forget()
        self.shenhe.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()
    def kc(self):
        self.kecheng.pack()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.jiaoshi.pack_forget()
        self.xiugaimima.pack_forget()
        self.shenhe.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()

    def tc(self):
        self.teacher.pack()
        self.shenhe.pack_forget()
        self.jiaoshi.pack_forget()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.xiugaimima.pack_forget()
        self.course.pack_forget()
        self.classroom.pack_forget()

    def cs(self):
        self.course.pack()
        self.shenhe.pack_forget()
        self.jiaoshi.pack_forget()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.teacher.pack_forget()
        self.xiugaimima.pack_forget()
        self.classroom.pack_forget()

    def cr(self):
        self.classroom.pack()
        self.shenhe.pack_forget()
        self.jiaoshi.pack_forget()
        self.jiaoshi1.pack_forget()
        self.xuesheng.pack_forget()
        self.banji.pack_forget()
        self.kecheng.pack_forget()
        self.teacher.pack_forget()
        self.course.pack_forget()
        self.xiugaimima.pack_forget()