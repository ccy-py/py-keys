import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import os
import cv2
import time
import numpy
from pynput import mouse
from pynput.mouse import Button, Controller
import random
import win32com.client
import tkinter
import tkinter.ttk
import json

yys = "F:\\pyWork\\quick-macro\\image\\ts\\yys.png"
yys_ts = "F:\\pyWork\\quick-macro\\image\\ts\\ts.png"
yys_ts1 = "F:\\pyWork\\quick-macro\\image\\ts\\ts1.png"
yys_ts_juexing = "F:\\pyWork\\quick-macro\\image\\ts\\juexing.png"
yys_ts_juexing_yehuo = "F:\\pyWork\\quick-macro\\image\\ts\\huo.png"
yys_ts_juexing_yefeng = "F:\\pyWork\\quick-macro\\image\\ts\\feng.png"
yys_ts_juexing_yeshui = "F:\\pyWork\\quick-macro\\image\\ts\\shui.png"
yys_ts_juexing_yelei = "F:\\pyWork\\quick-macro\\image\\ts\\lei.png"
yys_ts_juexing_yehuo_gundong = "F:\\pyWork\\quick-macro\\image\\ts\\gundong.png"
yys_ts_juexing_yehuo_gundong_lock = "F:\\pyWork\\quick-macro\\image\\ts\\lock.png"
yys_ts_juexing_yehuo_gundong_ks = "F:\\pyWork\\quick-macro\\image\\ts\\ks.png"
yys_ts_juexing_yehuo_gundong_zhunbei = "F:\\pyWork\\quick-macro\\image\\ts\\zhunbei.png"
yys_ts_juexing_yehuo_gundong_success = "F:\\pyWork\\quick-macro\\image\\ts\\success.png"
yys_ts_juexing_yehuo_gundong_back = "F:\\pyWork\\quick-macro\\image\\ts\\back.png"

# 御魂
yys_ts_yuhun = "F:\\pyWork\\quick-macro\\image\\ts\\yuhun.png"
yys_ts_yuhun_baqi = "F:\\pyWork\\quick-macro\\image\\ts\\baqi.png"
yys_ts_yuhun_yeyuanhuo = "F:\\pyWork\\quick-macro\\image\\ts\\yeyuanhuo.png"
yys_ts_yuhun_regui = "F:\\pyWork\\quick-macro\\image\\ts\\regui.png"

# fb选择
yys_ts_fb_fbgd = "F:\\pyWork\\quick-macro\\image\\ts\\fbgd.png"
yys_ts_fb_1 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\1.png"
yys_ts_fb_2 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\2.png"
yys_ts_fb_3 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\3.png"
yys_ts_fb_4 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\4.png"
yys_ts_fb_5 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\5.png"
yys_ts_fb_6 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\6.png"
yys_ts_fb_7 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\7.png"
yys_ts_fb_8 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\8.png"
yys_ts_fb_9 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\9.png"
yys_ts_fb_10 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\10.png"
yys_ts_fb_11 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\11.png"
yys_ts_fb_12 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\12.png"
yys_ts_fb_13 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\13.png"
yys_ts_fb_14 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\14.png"
yys_ts_fb_15 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\15.png"
yys_ts_fb_16 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\16.png"
yys_ts_fb_17 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\17.png"
yys_ts_fb_18 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\18.png"
yys_ts_fb_19 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\19.png"
yys_ts_fb_20 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\20.png"
yys_ts_fb_21 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\21.png"
yys_ts_fb_22 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\22.png"
yys_ts_fb_23 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\23.png"
yys_ts_fb_24 = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\24.png"
yys_ts_fb_fu_ts = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\fu_ts.png"
yys_ts_fb_fu_start = "F:\\pyWork\\quick-macro\\image\\ts\\fb\\start.png"

yys_ts_fb_fbgd = "F:\\pyWork\\quick-macro\\image\\ts\\fbgd.png"


def yys_action():
    return {
        # 几层 根据点击次数
        "level": 3,
        # 总次数
        "totalNum": 1,
        # 执行次数
        "execNum": 1,
        # 目标  ts
        "mb": yys_ts,
        # 项目  觉醒   御魂
        "xm": yys_ts_juexing,
        # fb  正常几直接
        "fb": [],
        # 是否需要gun
        "gdFlag": False,
        # gun触发位置
        "gd": yys_ts_juexing_yehuo_gundong,
        # 战斗开始按钮
        "start": yys_ts_juexing_yehuo_gundong_ks,
        "zhunbei": yys_ts_juexing_yehuo_gundong_zhunbei,
        # 战斗完成
        "success": yys_ts_juexing_yehuo_gundong_success,
        # 刷完 回退
        "back": yys_ts_juexing_yehuo_gundong_back,
    }


# winSpy获取句柄信息
def screenshot(filePath="11.jpg"):
    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save(os.getcwd() + "/" + filePath)
    time.sleep(random.randint(0, 2))


def caozuo(action):
    # 点击微信任务栏按钮 再点击登录
    mouse = Controller()
    # screenshot("12.png")
    # pos = match(os.getcwd() + '/12.png', action['mb'])
    # os.remove(os.getcwd() + '/12.png')

    # ts
    tans = True
    while tans:
        pos = position(action['mb'])
        print("click-ts:" + str(pos))
        if not pos:
            pos = position(yys_ts1)
            print("click-ts1:" + str(pos))
        if pos:
            mouse.position = pos
            time.sleep(0.5)
            mouse.click(Button.left, 2)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            tans = False
            print("click-ts点击:")

    time.sleep(random.randint(1, 9))

    # yehuo

    for fbImg in action['fb']:
        # ts
        tansu = True
        while tansu:
            # screenshot("121.png")
            # pos1 = match(os.getcwd() + '/121.png', action['xm'])
            # os.remove(os.getcwd() + '/121.png')
            pos1 = position(action['xm'])
            print("click-yh/jx" + str(pos1))
            if pos1:
                mouse.position = pos1
                # mouse.press(Button.right)
                mouse.click(Button.left, 1)
                tansu = False

        tansu = True
        time.sleep(random.randint(1, 3))
        while tansu:
            # screenshot("121.png")
            # pos1 = match(os.getcwd() + '/121.png', fbImg)
            # os.remove(os.getcwd() + '/121.png')
            pos1 = position(fbImg)
            print("click-jtfb" + str(fbImg))
            if pos1:
                mouse.position = pos1
                # mouse.press(Button.right)
                mouse.click(Button.left, 2)
                print("click-fb-jr")
                tansu = False

        time.sleep(random.randint(1, 5))
        # gun 十
        gundong = action["gdFlag"]
        while gundong:
            pos = position(action['gd'])
            print("click-yhgund" + str(pos))
            if pos:
                gundong = False
                mouse.position = pos
                time.sleep(0.1)
                print("click-yh-gun")
                mouse.scroll(0, -(random.randint(50, 200)))
                # mouse.press(Button.right)
                # yehuo
            # 开始
        time.sleep(random.randint(1, 2))
        while action["totalNum"] > action["execNum"]:
            pos = position(action['start'])
            print("click-开始" + str(pos))
            if pos:
                time.sleep(random.randint(0, 3))
                mouse.position = pos
                mouse.click(Button.left, 1)
                print("click-yh-点击")
                time.sleep(random.randint(1, 2))
                #  ready
                zhunbei = 1
                while zhunbei < 5:
                    pos = position(action['zhunbei'])
                    print("click-ready" + str(pos))
                    if pos:
                        time.sleep(random.randint(1, 3))
                        mouse.position = pos
                        # mouse.press(Button.right)
                        mouse.click(Button.left, 1)
                        zhunbei = 5
                        print("click-yh-click")
                    else:
                        print("click-yh-dengdai")
                        zhunbei = zhunbei + 1
                        time.sleep(random.randint(0, 2))

                time.sleep(random.randint(1, 10))
                # 判断是否结束
                zdend = True
                while zdend:
                    pos = position(action['success'])
                    print("click-end" + str(pos))
                    if pos:
                        mouse.position = pos
                        time.sleep(1)
                        # mouse.press(Button.right)
                        mouse.click(Button.left, 2)
                        zdend = False
                        action["execNum"] = action["execNum"] + 1
                        print("click-yh-end")
                    else:
                        time.sleep(random.randint(1, 5))
        # 单个循环结束  点击回退  jr下一个
        while action["totalNum"] == action["execNum"]:
            pos = position(action['back'])
            print("click-return" + str(pos))
            if pos:
                mouse.position = pos
                mouse.click(Button.left, 1)
                action["execNum"] = action["execNum"] + 1

        # 执行次数 == 总次数 修改为0  进行下一个fb
        action["execNum"] = 0


def position(templatePath, minValue=0.1):
    screenshot("121.png")
    pos = match(os.getcwd() + '/121.png', templatePath, minValue)
    os.remove(os.getcwd() + '/121.png')
    return pos


# 读取目标图片 targetPath
# 读取模板图片 temPlatePath
def match(targetPath, temPlatePath, minValue=0.1):
    # screenshot("121.png")
    # time.sleep(2)
    target = cv2.imread(targetPath, cv2.COLOR_BGR2RGB)
    template = cv2.imread(temPlatePath, cv2.COLOR_BGR2RGB)
    # 获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    # cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(min_val)
    # 绘制矩形边框，将匹配区域标注出来
    # min_loc：矩形定点
    # (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
    print(str(min_val))
    print(str(max_val))
    print(str(min_loc))
    if min_val < minValue and min_val > 0:
        print("成功")
        wei = random.randint(2, 20)
        heg = random.randint(2, 20)

        wei1 = random.randint(2, 10)
        heg1 = random.randint(2, 10)
        return (min_loc[0] - 1 + twidth / wei + twidth / wei1, min_loc[1] - 1 + theight / heg + theight / heg1)
    else:
        return ""



# 读取目标图片 targetPath
# 读取模板图片 temPlatePath
def matchMore(targetPath, temPlatePath, minValue=0.1):
    # screenshot("121.png")
    # time.sleep(2)
    target = cv2.imread(targetPath, cv2.COLOR_BGR2RGB)
    template = cv2.imread(temPlatePath, cv2.COLOR_BGR2RGB)
    # 获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    # cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #绘制矩形边框，将匹配区域标注出来
    #min_loc：矩形定点
    #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(min_val)
    #初始化位置参数
    temp_loc = min_loc
    other_loc = min_loc
    numOfloc = 1
    #一次筛选----规定匹配阈值，将满足阈值的从result中提取出来
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法设置匹配阈值为0.01
    threshold = 0.01
    loc = numpy.where(result<threshold)
    local=None
    #遍历提取出来的位置
    for other_loc in zip(*loc[::-1]):
        print(other_loc)
        #二次筛选----将位置偏移小于5个像素的结果舍去
        if (temp_loc[0]+5<other_loc[0])or(temp_loc[1]+5<other_loc[1]):
            print("成功")
            wei = random.randint(2, 20)
            heg = random.randint(2, 20)

            wei1 = random.randint(2, 10)
            heg1 = random.randint(2, 10)
            local=(min_loc[0] - 1 + twidth / wei + twidth / wei1, min_loc[1] - 1 + theight / heg + theight / heg1)
            break
    return  local


def caozuofb(action):
    # 点击微信任务栏按钮 再点击登录
    mouse = Controller()
    # screenshot("12.png")
    # pos = match(os.getcwd() + '/12.png', action['mb'])
    # os.remove(os.getcwd() + '/12.png')

    # ts
    tans = True
    while tans:
        pos = position(action['mb'])
        print("click-ts:" + str(pos))
        if not pos:
            pos = position(yys_ts1)
            print("click-ts1:" + str(pos))
        if pos:
            mouse.position = pos
            time.sleep(0.5)
            mouse.click(Button.left, 2)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            tans = False
            print("click-ts点击:")

    time.sleep(random.randint(1, 9))

    # yehuo

    for fbImg in action['fb']:
        findFb = True
        while findFb:
            pos = matchMore(fbImg)
            print("click-搜索fb:" + str(fbImg))
            print("click-搜索fb:" + str(pos))
            if pos == "":
                pos = position(action["gd"])
                while pos != "":
                    pos = (pos[0], pos[1] + random.randint(50, 300))
                    mouse.position = pos
                    mouse.scroll(0, (random.randint(200, 1000)))
                    print("click-搜索fb-gun:" + str(pos))
                    return
            else:
                print("click-tsfb成功:")
                mouse.position = pos
                time.sleep(0.5)
                mouse.click(Button.left, 2)
                findFb = False

            if findFb:
                mouse.scroll(0, (random.randint(100, 300)))

            time.sleep(0.5)

        time.sleep(2)
        findFb1 = True
        while findFb1:
            pos = position(action["ts"])
            print("click-ts:" + str(pos))
            if pos:
                mouse.position = pos
                time.sleep(0.5)
                mouse.click(Button.left, 2)
                findFb1 = False
                print("click-ts:")

        time.sleep(2)
        findFb2 = True
        while findFb2:
            pos = position(action["start"])
            print("click-ts:" + str(pos))
            if pos:
                mouse.position = pos
                time.sleep(0.5)
                mouse.click(Button.left, 2)
                findFb2 = False
                print("click-ts:")
                #  ready
        zhunbei = 1
        while zhunbei < 5:
            pos = position(action['zhunbei'])
            print("click-ready" + str(pos))
            if pos:
                time.sleep(random.randint(1, 3))
                mouse.position = pos
                # mouse.press(Button.right)
                mouse.click(Button.left, 1)
                zhunbei = 5
                print("click-fb-click")
            else:
                print("click-fb-dengdai")
                zhunbei = zhunbei + 1
                time.sleep(random.randint(0, 2))

        time.sleep(random.randint(1, 5))
        # 判断是否结束
        zdend = True
        while zdend:
            pos = position(action['success'])
            print("click-end" + str(pos))
            if pos:
                mouse.position = pos
                time.sleep(1)
                # mouse.press(Button.right)
                mouse.click(Button.left, 2)
                zdend = False
                print("click-yh-点击")
            else:
                time.sleep(random.randint(1, 5))
        # 单个循环结束  点击回退  jr下一个
    while action["totalNum"] == action["execNum"]:
        pos = position(action['back'])
        print("click-回退上一级" + str(pos))
        if pos:
            mouse.position = pos
            mouse.click(Button.left, 1)
            action["execNum"] = action["execNum"] + 1


# 御魂
def jx():
    action = yys_action()
    action["level"] = 5
    action["xm"] = yys_ts_juexing
    action["gdFlag"] = True
    action["gd"] = yys_ts_juexing_yehuo_gundong
    action["start"] = yys_ts_juexing_yehuo_gundong_ks
    action["totalNum"] = int(numText.get())
    action["execNum"] = int(0)
    fbList = []
    if checkVar1.get() == 1:
        fbList.append(yys_ts_juexing_yehuo)
    if checkVar2.get() == 1:
        fbList.append(yys_ts_juexing_yefeng)
    if checkVar3.get() == 1:
        fbList.append(yys_ts_juexing_yeshui)
    if checkVar4.get() == 1:
        fbList.append(yys_ts_juexing_yelei)

    action["fb"] = fbList

    print(json.dumps(action))
    caozuo(action)


# 御魂
def yx():
    action = yys_action()
    action["level"] = 5
    action["xm"] = yys_ts_yuhun
    action["gdFlag"] = False
    # action["gd"] = yys_ts_juexing_yehuo_gundong
    action["start"] = yys_ts_juexing_yehuo_gundong_ks
    action["totalNum"] = int(numText1.get())
    action["execNum"] = int(0)
    fbList1 = []
    if checkVar11.get() == 1:
        fbList1.append(yys_ts_yuhun_baqi)
    if checkVar21.get() == 1:
        fbList1.append(yys_ts_yuhun_yeyuanhuo)
    if checkVar31.get() == 1:
        fbList1.append(yys_ts_yuhun_regui)

    action["fb"] = fbList1

    print(json.dumps(action))
    caozuo(action)


def fuben():
    action = yys_action()
    action["xm"] = yys_ts_fb_fbgd

    fbtp = [yys_ts_fb_1, yys_ts_fb_2, yys_ts_fb_3, yys_ts_fb_4, yys_ts_fb_5, yys_ts_fb_6, yys_ts_fb_7, yys_ts_fb_8,
            yys_ts_fb_9, yys_ts_fb_10, yys_ts_fb_11, yys_ts_fb_12, yys_ts_fb_13, yys_ts_fb_14, yys_ts_fb_15,
            yys_ts_fb_16, yys_ts_fb_17, yys_ts_fb_18, yys_ts_fb_19, yys_ts_fb_20, yys_ts_fb_21, yys_ts_fb_22,
            yys_ts_fb_23, yys_ts_fb_24]

    fbListfb = []
    for i in lb.curselection():
        fbListfb.append(fbtp[i])

    action["fb"] = fbListfb
    action["gd"] = yys_ts_fb_fbgd
    action["ts"] = yys_ts_fb_fu_ts
    action["start"] = yys_ts_fb_fu_start
    caozuofb(action)

    # caozuo(action)


def qkxz():
    lb.delete(0, tkinter.END)
    for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                 "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]:
        lb.insert(tkinter.END, item)


if __name__ == '__main__':
    # check_exsit("wechat");
    # opencv("11.jpg")
    #  mouse=Controller()
    #  mouse.scroll(0,-100)
    # getClick()
    # random.randint(0,100)
    root = tkinter.Tk()
    root.geometry('300x200+600+100')

    notebook = tkinter.ttk.Notebook(root)

    frameOne = tkinter.Frame()
    tkinter.Button(frameOne, text="执行", command=jx).pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)
    numText = tkinter.Entry(frameOne, text='')
    numText.pack(side="bottom", padx=5, pady=5, anchor='s', fill='x')
    tkinter.Label(frameOne, text='执行次数（每个选中的fb执行次数）：').pack(side="bottom", padx=5, pady=5, anchor='w', fill='y')
    checkVar1 = tkinter.IntVar()
    checkVar1.set(0)
    cb1 = tkinter.Checkbutton(frameOne, text='火', variable=checkVar1)
    cb1.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    checkVar2 = tkinter.IntVar()
    checkVar2.set(0)
    cb2 = tkinter.Checkbutton(frameOne, text='风', variable=checkVar2)
    cb2.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    checkVar3 = tkinter.IntVar()
    checkVar3.set(0)
    cb3 = tkinter.Checkbutton(frameOne, text='水', variable=checkVar3)
    cb3.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    checkVar4 = tkinter.IntVar()
    checkVar4.set(0)
    cb4 = tkinter.Checkbutton(frameOne, text='雷', variable=checkVar4)
    cb4.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    frameTwo = tkinter.Frame()
    tkinter.Button(frameTwo, text="执行", command=yx).pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)
    numText1 = tkinter.Entry(frameTwo, text='')
    numText1.pack(side="bottom", padx=5, pady=5, anchor='s', fill='x')
    tkinter.Label(frameTwo, text='执行次数（每个选中的fb执行次数）：').pack(side="bottom", padx=5, pady=5, anchor='w', fill='y')
    checkVar11 = tkinter.IntVar()
    checkVar11.set(0)
    cb1 = tkinter.Checkbutton(frameTwo, text='蛇', variable=checkVar11)
    cb1.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    checkVar21 = tkinter.IntVar()
    checkVar21.set(0)
    cb2 = tkinter.Checkbutton(frameTwo, text='业', variable=checkVar21)
    cb2.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    checkVar31 = tkinter.IntVar()
    checkVar31.set(0)
    cb3 = tkinter.Checkbutton(frameTwo, text='日', variable=checkVar31)
    cb3.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)

    frameThree = tkinter.Frame()
    tkinter.Button(frameThree, text="执行", command=fuben).pack(side='left', expand='no', anchor='w', fill='y', padx=5,
                                                              pady=5)
    numText1 = tkinter.Entry(frameThree, text='')
    numText1.pack(side="bottom", padx=5, pady=5, anchor='s', fill='x')
    tkinter.Label(frameThree, text='执行次数（每个选中的fb执行次数）：').pack(side="bottom", padx=5, pady=5, anchor='w', fill='y')
    lb = tkinter.Listbox(frameThree, selectmode=tkinter.MULTIPLE)
    lb.pack(side="left", padx=5, pady=5, fill='y')
    tkinter.Button(frameThree, text="清空", command=qkxz).pack(side="right", padx=5, pady=5, fill='y')
    for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                 "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]:
        lb.insert(tkinter.END, item)

    notebook.add(frameOne, text='觉醒')
    notebook.add(frameTwo, text='御魂')
    notebook.add(frameThree, text='fb')
    notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=0)

    root.mainloop()
# screenshotWindeos("11.jpg")
