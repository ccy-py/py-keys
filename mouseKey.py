import json
import threading
import time
import tkinter
import tkinter.messagebox
import os
from pynput import mouse, keyboard
from pynput.keyboard import Controller as KeyController, KeyCode
from pynput.mouse import Controller as MouseController, Button


# 键盘动作模板
def keyboard_action_template():
    return {
        "name": "keyboard",
        "event": "default",
        "sleep": "0.01",
        "vk": "default"
    }



# 鼠标动作模板
def mouse_action_template():
    return {
        "name": "mouse",
        "event": "default",
        "target": "default",
        "action": "default",
        "sleep": "0.01",
        "location": {
            "x": "0",
            "y": "0"
        }
    }


keyboardFile = "keyboard.action"
mouseFile = "mouse.action"


class jsTime():
    def getTime(self):
        nowtime = time.time()
        print(str(nowtime))
        return int(round(nowtime * 1000000))

    def difTime(self, end, start):
        return ((end - start) / 1000000)


# 鼠标动作监听
class KeyboardActionListener(threading.Thread):

    def __init__(self, file_name=keyboardFile, nowtime=jsTime().getTime()):
        super().__init__()
        self.file_name = file_name
        self.time = nowtime

    def close_listener(self, listener):
        if MouseActionListener.esc_key:
            listener.stop()

    def run(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            def on_press(key):
                print("按键：" + str(key))
                k = keyboard_action_template()
                k['event'] = 'press'
                nowTime = jsTime().getTime()
                k['sleep'] = jsTime().difTime(nowTime, self.time)
                self.time = nowTime
                try:
                    k["vk"] = key.vk
                except AttributeError:
                    k['vk'] = key.value.vk
                finally:
                    file.writelines(json.dumps(k) + "\n")
                    file.flush()

            def release(key):
                print("按键：" + str(key))
                nowTime = jsTime().getTime()
                if key == keyboard.Key.esc:
                    print("停止---esc")
                    MouseActionListener.esc_key = True
                    listener.stop()
                    return False
                k = keyboard_action_template()
                k['event'] = 'release'
                k['sleep'] = jsTime().difTime(nowTime, self.time)
                self.time = nowTime;
                try:
                    k["vk"] = key.vk
                except AttributeError:
                    k['vk'] = key.value.vk
                finally:
                    file.writelines(json.dumps(k) + "\n")
                    file.flush()
                    self.close_listener(listener)

            with keyboard.Listener(on_press=on_press, on_release=release) as listener:
                listener.join()


# 鼠标动作监听
class KeyboardActionExec(threading.Thread):
    key_end = True
    count = 0

    def __init__(self, file_name=keyboardFile, count=0):
        super().__init__()
        self.file_name = file_name
        self.count = int(count)
        KeyboardActionExec.count =  int(count)

    def run(self):
        while self.count > 0:
            if self.count == MouseActionExec.execute_count:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    keyController = KeyController()
                    line = file.readline()
                    while line:
                        obj = json.loads(line)
                        time.sleep(float(obj['sleep']))
                        if obj['event'] == 'press':
                            keyController.press(KeyCode.from_vk(obj['vk']))
                        else:
                            keyController.release(KeyCode.from_vk(obj['vk']))
                        line = file.readline()
                self.count = self.count - 1
                KeyboardActionExec.count = self.count


# 鼠标动作监听
class MouseActionListener(threading.Thread):
    esc_key = False

    def __init__(self, file_name=mouseFile, nowtime=jsTime().getTime()):
        super().__init__()
        self.file_name = file_name
        self.time = nowtime

    def close_listener(self, listener):
        print("停止11" + str(self.esc_key))
        if self.esc_key:
            listener.stop()

    def run(self):
        with open(self.file_name, 'w', encoding="UTF-8") as file:
            def on_move(x, y):
                nowTime = jsTime().getTime()
                temp = mouse_action_template()
                temp['sleep'] = jsTime().difTime(nowTime, self.time)
                self.time = nowTime
                temp['event'] = 'move'
                temp["location"]["x"] = x
                temp["location"]["y"] = y
                file.writelines(json.dumps(temp) + "\n")
                file.flush()
                self.close_listener(mouseListener)

            def on_click(x, y, button, pressed):
                nowTime = jsTime().getTime()
                temp = mouse_action_template()
                temp['sleep'] = jsTime().difTime(nowTime, self.time)
                self.time = nowTime;
                temp['event'] = 'click'
                temp["location"]["x"] = x
                temp["location"]["y"] = y
                temp['target'] = button.name
                temp['action'] = pressed
                print("点击：" + str(button.name))
                file.writelines(json.dumps(temp) + "\n")
                file.flush()
                self.close_listener(mouseListener)

            def on_scroll(x, y, x_axis, y_axis):
                nowTime = jsTime().getTime()
                temp = mouse_action_template()
                temp['sleep'] = jsTime().difTime(nowTime, self.time)
                self.time = nowTime
                temp['event'] = 'scroll'
                temp["location"]["x"] = x_axis
                temp["location"]["y"] = y_axis
                file.writelines(json.dumps(temp) + "\n")
                file.flush()
                self.close_listener(mouseListener)

            with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouseListener:
                mouseListener.join()


# 鼠标动作监听
class MouseActionExec(threading.Thread):
    mouse_end = True
    execute_count = 0

    def __init__(self, file_name=mouseFile, execute_count=0):
        super().__init__()
        self.file_name = file_name
        self.execute_count = int(execute_count)
        MouseActionExec.execute_count = int(execute_count)

    def close_listener(self, listener):
        print("111")

    def run(self):
        while self.execute_count > 0:
            if self.execute_count == KeyboardActionExec.count:
                with open(self.file_name, 'r', encoding="UTF-8") as file:
                    mouse = MouseController()
                    line = file.readline()
                    while str(line) != '':
                        obj = json.loads(line)
                        print("line:" + str(line))
                        time.sleep(float(obj['sleep']))
                        if obj['name'] == 'mouse':
                            if obj['event'] == 'move':
                                mouse.position = (obj['location']['x'], obj['location']['y'])
                                print("x:" + str(obj['location']['x']) + ",y:" + str(obj['location']['y']))
                                # time.sleep(0.01)
                            elif obj['event'] == 'click':
                                if obj['action']:
                                    if obj['target'] == 'left':
                                        mouse.press(Button.left)
                                    else:
                                        mouse.press(Button.right)
                                else:
                                    if obj['target'] == 'left':
                                        mouse.release(Button.left)
                                    else:
                                        mouse.release(Button.right)
                                # time.sleep(0.01)
                            elif obj['event'] == 'scroll':
                                mouse.scroll(obj['location']['x'], obj['location']['y'])
                                # time.sleep(0.01)
                        line = file.readline()
                self.execute_count = self.execute_count - 1
                MouseActionExec.execute_count = self.execute_count


def countNum():
    file=entFile.get()
    if not file:
        tkinter.messagebox.showinfo('提示','人生苦短')
        return

    i = ent.get()
    m=MouseActionExec(file+mouseFile,i)
    k=KeyboardActionExec(file+keyboardFile,i)
    m.start()
    k.start()


def close():
    if not MouseActionListener.esc_key:
        print("停止")
        MouseActionListener.esc_key = True


# threading.Timer(5, close).start()

def startService():
    file=entFile.get()

    mouseFile = file+"mouse.action"
    keyboardFile = file+"keyboard.action"

    MouseActionListener.esc_key = False
    if os.path.isfile(mouseFile):
        with open(mouseFile, "r+") as f:
            f.truncate()

    if os.path.isfile(keyboardFile):
        with open(keyboardFile, "r+") as f:
            f.truncate()

    nowTime = jsTime().getTime()
    mouseAction = MouseActionListener(mouseFile, nowTime)
    mouseAction.start()
    keyboardAction = KeyboardActionListener(keyboardFile, nowTime)
    keyboardAction.start()


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('按键精灵')
    root.geometry('200x200+400+100')
    tkinter.Label(root, text="脚本:").pack()
    tkinter.Button(root, text="启动", command=startService).pack(fill ='x')
    tkinter.Button(root, text="停止", command=close).pack(fill ='x')
    tkinter.Button(root, text="回访", command=countNum).pack(fill ='x')

    tkinter.Label(root, text="脚本地址:").pack(fill ='x')
    entFile = tkinter.Entry(root, text="")
    entFile.pack(fill ='x')

    tkinter.Label(root, text="循环次数:").pack(fill ='x')
    ent = tkinter.Entry(root, text="1")
    ent.insert(0,1)
    ent.pack()
    root.mainloop()
