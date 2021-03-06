# Pre-installed libraries
import os
import time
import re
import random
import sys
import shutil
import json as jl
import msvcrt as m
import threading as thrd
from volume import Volume
from mega import Mega
import subprocess
import pyttsx3
import pyHook
import bitly

# Must be installed
import pathlib
import pyperclip
import win32gui
import win32api
import win32ui
import win32con
import datetime
import randstr
import colorama
import mouse as ml
import win32process
import win32console
import keyboard as kl
from pytube import YouTube
import youtubesearchpython as ys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from google_trans_new import google_translator
from base64 import b64encode, b64decode
from contextlib import contextmanager
import speech_recognition as sr
from fuzzywuzzy import fuzz
import webbrowser
import convertapi
import pyautogui
import threading
from win32com.client import Dispatch
import winshell
import socket
from pyngrok import ngrok, conf
import pickle

@contextmanager
def _suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

with _suppress_stdout():
    import pygame
    pygame.init()
colorama.init(autoreset=True)
convertapi.api_secret = 'QRttNaCK0tXSOHeY'
speak_engine = pyttsx3.init()

def delAllExcNums(string):
    return re.sub("\D", "", string)
def removePrefix(string, value):
    if len(value) != int:
        if not string.startswith(value):
            raise KeyError(f"'{string}' doesn't start with '{value}'")
        value = len(value)
    full_string_without_prefix = ''
    i = 1
    for valuee in list(string):
        if i <= value:
            time.sleep(0)
        else:
            full_string_without_prefix += valuee
        i += 1
    return full_string_without_prefix
def removeSuffix(string, value):
    if len(value) != int:
        if not string.endswith(value):
            raise KeyError(f"'{string}' doesn't end with '{value}'")
        value = len(value)
    full_string_without_suffix = ''
    i = 0
    for valuee in list(string):
        if i != len(string) - value:
            full_string_without_suffix += valuee
        else:
            break
        i += 1
    return full_string_without_suffix
_typeReal = type
def _type(var):
    global typeReal
    return removeSuffix(removePrefix(str(_typeReal(var)), "<class '"), '>')
type = _type
def hex2rgb(hex):
    hex = removePrefix(hex, '#')
    lv = len(hex)
    return tuple(int(hex[i:i+lv//3], 16) for i in range(0, lv, lv//3))
def rgb2hex(rgb):
    return '#%02x%02x%02x' % rgb
class blockInput():
    def OnKeyboardEvent(self, event):
        return False
    def OnMouseEvent(self, event):
        return False
    def unblock(self, kl=True, mouse=True):
        try:
            if self.t.is_alive():
                self.t.cancel()
        except: pass
        if kl:
            try: self.hm.UnhookKeyboard()
            except: pass
        if mouse:
            try: self.hm.UnhookMouse()
            except: pass
    def block(self, timeout = None, kl = True, mouse = True):
        self.t = thrd.Timer(timeout, self.unblock(kl = kl, mouse = mouse))
        self.t.start()
        if timeout == None:
            self.t.cancel()
        if mouse:
            self.hm.MouseAll = self.OnMouseEvent
            self.hm.HookMouse()
        if kl:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()
        win32gui.PumpWaitingMessages()
    def __init__(self):
        self.hm = pyHook.HookManager()
blockObj = blockInput()
class keyboard:
    global blockObj
    __block = blockObj
    keys = ['Ctrl', 'Shift', 'Alt', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Escape', 'Space',
            'BackSpace', 'Tab', 'Linefeed', 'Clear', 'Return', 'Pause', 'Scroll_Lock', 'Sys_Req', 'Delete', 'Home', 'Left', 'Up',
            'Right', 'Down', 'Page_Up', 'Page_Down', 'End', 'Select', 'Print', 'Execute', 'Insert', 'Num_Lock', 'F1', 'F2', 'F3',
            'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
    def press(self, key):
        kl.press(key)
    def release(self, key):
        kl.release(key)
    def click(self, key, delay=0):
        if delay/1000 == 0:
            kl.send(key)
        else:
            kl.press(key)
            time.sleep(delay/1000)
            kl.release(key)
    def write(self, keys, delay=100):
        kl.write(keys, delay=delay/1000)
    def isPressed(self, key):
        return kl.is_pressed(key)
    def wait(self, key=None):
        if key == None:
            while 1:
                for value in self.keys:
                    if self.isPressed(value):
                        return value
        elif type(key) == 'list':
            while 1:
                for value in key:
                    if self.isPressed(value):
                        return value
        else:
            while 1:
                if self.isPressed(key):
                    return key
    def block(self, timeout=None):
        self.__block.block(timeout=timeout, kl=True, mouse=False)
    def unblock(self):
        self.__block.unblock(kl=True, mouse=False)
keyboard = keyboard()
keys = keyboard
class mouse:
    global blockObj
    __block = blockObj
    def scroll(self, x):
        ml.wheel(x)
    def click(self, side):
        ml.click(button = side)
    @property
    def position(self):
        return ml.get_position()
    def move(self, x, y, absolute=True, delay=100):
        ml.move(x, y, absolute=absolute, duration=delay/1000)
    def isPressed(self, side):
        return ml.is_pressed(button = side)
    def wait(self, side=None):
        if side == None:
            while 1:
                if self.isPressed('left'):
                    return 'left'
                elif self.isPressed('right'):
                    return 'right'
                elif self.isPressed('middle'):
                    return 'middle'
        elif type(side) == 'list':
            while 1:
                for value in side:
                    if self.isPressed(value):
                        return value
        else:
            while 1:
                if self.isPressed(side):
                    return side
    def block(self, timeout=None):
        self.__block.block(timeout=timeout, kl=False, mouse=True)
    def unblock(self):
        self.__block.unblock(kl=False, mouse=True)
mouse = mouse()
del blockObj
class colors:
    class text:
        black = colorama.Fore.BLACK
        red = colorama.Fore.RED
        green = colorama.Fore.GREEN
        yellow = colorama.Fore.YELLOW
        blue = colorama.Fore.BLUE
        magenta = colorama.Fore.MAGENTA
        cyan = colorama.Fore.CYAN
        white = colorama.Fore.WHITE
    text = text()
    class bg:
        black = colorama.Back.BLACK
        red = colorama.Back.RED
        green = colorama.Back.GREEN
        yellow = colorama.Back.YELLOW
        blue = colorama.Back.BLUE
        magenta = colorama.Back.MAGENTA
        cyan = colorama.Back.CYAN
        white = colorama.Back.WHITE
    bg = bg()
    class style:
        dim = colorama.Style.DIM
        normal = colorama.Style.NORMAL
        bright = colorama.Style.BRIGHT
    style = style()
color = colors()
colors = color

class console:
    def __init__(self):
        self._printed = ''
        self._win = win32console.GetConsoleWindow()
        self._blockThread = None
        self._isBlock = False
    def focus(self):
        self.hide()
        self.show()
        win32gui.BringWindowToTop(self._win)
        win32gui.ShowWindow(self._win, win32con.SW_SHOWNORMAL)
    def unfocus(self):
        win32gui.SetForegroundWindow(self._win)
    def hide(self):
        win32gui.ShowWindow(self._win, win32con.SW_HIDE)
    def show(self):
        win32gui.ShowWindow(self._win, win32con.SW_SHOW)
    def move(self, x, y):
        win32gui.SetWindowPos(self._win, x, y, self.size[0], self.size[1])
    def resize(self, width, height):
        win32gui.SetWindowPos(self._win, self.position[0], self.position[1], width, height)
    def minimize(self):
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        return self.size
    def maximize(self):
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        return self.size
    def title():
        def fget(self):
            return win32console.GetConsoleTitle()
        def fset(self, value):
            win32console.SetConsoleTitle(str(value))
        def fdel(self):
            pass
        return locals()
    title = property(**title())
    def block(self, move=False, click=False):
        self._isBlock = True
        if self._blockThread != None:
            self._isBlock = False
            self._blockThread.join()
            self._isBlock = True
        if not move and not click:
            win32gui.EnableWindow(self._win, False)
        elif move and not click:
            def funcBlock(self):
                blocked = False
                while self._isBlock:
                    if mouse.position[1]-self.position[1] > 30:
                        if not blocked:
                            win32gui.EnableWindow(self._win, False)
                            blocked = True
                    else:
                        if blocked:
                            win32gui.EnableWindow(self._win, True)
                            blocked = False
            self._blockThread = thrd.Thread(target=lambda: funcBlock(self), name='Block window')
            self._blockThread.start()
        elif not move and click:
            def funcBlock(self):
                blocked = False
                while self._isBlock:
                    if mouse.position[1]-self.position[1] <= 30:
                        if not blocked:
                            win32gui.EnableWindow(self._win, False)
                            blocked = True
                    else:
                        if blocked:
                            win32gui.EnableWindow(self._win, True)
                            blocked = False
            self._blockThread = thrd.Thread(target=lambda: funcBlock(self), name='Block window')
            self._blockThread.start()
    def unblock(self):
        self._isBlock = False
        if self._blockThread != None:
            self._blockThread.join()
        self._blockThread = None
        win32gui.EnableWindow(self._win, True)
    def pause(self, text='Press any key to continue...'):
        self.print(text)
        m.getch()
    @property
    def visible(self):
        return win32gui.IsWindowVisible(self._win)
    @property
    def position(self):
        rect = win32gui.GetWindowRect(self._win)
        x = rect[0]+7
        y = rect[1]
        return (x, y)
    @property
    def size(self):
        rect = win32gui.GetWindowRect(self._win)
        w = rect[2] - self.position[0]-7
        h = rect[3] - self.position[1]-7
        return (w, h)
    @property
    def printed(self):
        return self._printed.split('\n')
    @property
    def args(self):
        args = []
        for i in sys.argv:
            if i != sys.argv[0]:
                args.append(i)
        return args
    def screenshot(self, path):
        rect = self.position+self.size
        self.focus()
        pyautogui.screenshot(path, region=rect)
        return path
    def input(self, *string, center=False, delay=0, color=color.text.white, newLine=True, whitelist=None, limit=None):
        def inwlc(text, whitelist=None, count=None):
            if whitelist == None and count == None:
                input(text)
            else:
                was = ""
                while True:
                    key = keys.wait()
                    if key == "backspace":
                        was0 = ""
                        for i in was:
                            if i != was[-1]:
                                was0 += i
                        was = was0
                    elif key == "enter":
                        return was
                    elif key == "space":
                        was += " "
                    else:
                        if whitelist != None:
                            if count != None:
                                if key in whitelist:
                                    if len(was) != count:
                                        was += key
                            else:
                                if key in whitelist:
                                    was += key
                        elif count != None:
                            if len(was) != count:
                                was += key
                    os.system("cls")
                    print(was)
        string0 = ''
        for value in string:
            string0 += str(value)
        string = string0
        del string0
        beforePrint = self._printed
        if not center:
            if delay == 0:
                if newLine:
                    self._printed += '\n' + color + str(string)
                    return inwlc(color + str(string), whitelist, limit)
                else:
                    self._printed += color + str(string)
                    os.system('cls')
                    return inwlc(self._printed, whitelist, limit)
            else:
                string = str(string)
                no_full_str = ''
                for value in list(string):
                    no_full_str += value
                    time.sleep(delay / 1000)
                    os.system('cls')
                    print(self._printed)
                    print(color + no_full_str)
                os.system('cls')
                print(self._printed)
                self._printed += '\n' + color + str(string)
                return inwlc(color + no_full_str, whitelist, limit)
        else:
            if delay == 0:
                line = [str(string)]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, line))) // 2
                self._printed += '\n' + color + str(line[0].center(width))
                return inwlc(color + str(line[0].center(width)), whitelist, limit)
            else:
                lines = str(string)
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                no_full_str = ''
                for value in list(string):
                    os.system('cls')
                    print(self._printed)
                    time.sleep(delay / 1000)
                    print(color + no_full_str.center(width))
                    no_full_str += value
                self._printed += '\n' + str(color + no_full_str.center(width))
                return inwlc(color + no_full_str.center(width), whitelist, limit)
    def print(self, *string, center=False, delay=0, color=color.text.white, newLine=True, msBeforeDelete=None):
        string0 = ''
        for value in string:
            string0 += str(value)
        string = string0
        del string0
        beforePrint = self._printed
        if not center:
            if delay == 0:
                if newLine:
                    print(color + str(string))
                    self._printed += '\n' + color + str(string)
                else:
                    self._printed += color + str(string)
                    os.system('cls')
                    print(self._printed)
            else:
                string = str(string)
                no_full_str = ''
                for value in list(string):
                    no_full_str += value
                    time.sleep(delay / 1000)
                    os.system('cls')
                    print(self._printed)
                    print(color + no_full_str)
                self._printed += '\n' + color + str(string)
        else:
            if delay == 0:
                if type(string) == 'list':
                    lines = str(string)
                else:
                    lines = [string]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                for line in lines:
                    print(color + line.center(width))
                    self._printed += '\n' + color + str(line.center(width))
            else:
                if type(string) == 'list':
                    lines = str(string)
                else:
                    lines = [string]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                for line in lines:
                    no_full_str = ''
                    for value in list(string):
                        os.system('cls')
                        print(self._printed)
                        time.sleep(delay / 1000)
                        print(color + no_full_str.center(width))
                        no_full_str += value
                    self._printed += '\n' + str(color + no_full_str.center(width))
        if msBeforeDelete != None:
            def deleteDef():
                nonlocal beforePrint, msBeforeDelete
                time.sleep(msBeforeDelete/1000)
                os.system('cls')
                self._printed = beforePrint
                return
            deleteThread = thrd.Thread(target=deleteDef)
            deleteThread.start()
    def clear(self, lines=0):
        if lines == 0:
            os.system('cls')
            self._printed = ''
        else:
            splitLines = self._printed.split('\n')
            fixedLines = ''
            i = 0
            for value in splitLines:
                if i == len(splitLines) - lines:
                    break
                else:
                    fixedLines += value
                    if i != len(splitLines):
                        fixedLines += '\n'
                i += 1
            os.system('cls')
            print(fixedLines)
            self._printed = fixedLines
    def run(self, cmd, show=False):
        if show:
            subprocess.check_call(cmd, shell=True)
        returnedText = subprocess.check_output(cmd, shell=True).decode()
        try:
            returnedText = removeSuffix(returnedText, '\r\n')
        except:
            pass
        return returnedText
    def start(self, path):
        _0, _1, pid, _2 = win32process.CreateProcess(
                    None, apppath, None, None, 0,
                    win32con.NORMAL_PRIORITY_CLASS, None,
                    None, win32process.STARTUPINFO())
        for win in windows(False):
            if win.pid == pid:
                return win
console = console()
cnsl = console
cmd = console

def wait(ms):
    time.sleep(ms/1000)
def rand(x=0, y=0):
    if type(x) != list:
        return random.randint(x, y)
    else:
        return x[random.randint(0, len(x)-1)]
def randStr(countKeys, symbols=None):
    if symbols == None:
        return randstr.randstr(countKeys)
    else:
        return randstr.randstr(countKeys, symbols)
class base64:
    def encode(self, string):
        string = str(string)
        return b64encode(string.encode('ascii')).decode('utf8')
    def decode(self, string):
        string = str(string)
        return b64decode(string).decode('utf8')
base64 = base64()

class thread:
    def __init__(self, func, name=None, daemon=True, group=None):
        self.function = func
        self.name = name
        self.daemon = daemon
        self.group = group
        self.isStarted = False
        self.thread = thrd.Thread(target=self.function,
                                        name=self.name,
                                        daemon=self.daemon,
                                        group=self.group)
    def start(self):
        self.thread.start()
        self.isStarted = True
    def stop(self):
        self.thread.join()
        self.isStarted = False
class timer:
    def __init__(self, func, interval):
        self.function = func
        self.interval = interval
        self.thread = thrd.Timer(self.interval, self.function)
    def start(self):
        self.thread.start()
    def stop(self):
        self.thread.cancel()
    @property
    def isStarted(self):
        return self.thread.isAlive()
class files:
    def read(self, path):
        file_ = open(path, 'rb')
        read_ = file_.read()
        file_.close()
        return read_
    def write(self, path, str):
        file_ = open(path, 'w')
        file_.write(str)
        file_.close()
    def create(self, path):
        open(path, 'w').close()
    def remove(self, path):
        os.remove(path)
    def exists(self, path):
        return os.path.isfile(path)
    def localDir(self):
        return str(pathlib.Path(win32api.GetFullPathName(__file__)).parent)
    def files(self, path):
        return os.listdir(path)
    def convert(self, path, to_format):
        format_ = path.split('.')[-1]
        outfile = removeSuffix(path, format_)
        convertapi.convert(format_, { 'File': path }).file.save(f'{outfile}.{to_format}')
    def createDir(self, path):
        os.mkdir(path)
    def removeDir(self, path):
        shutil.rmtree(path)
    def addedFile(self, path):
        base_path = sys._MEIPASS
        return os.path.join(base_path, path)
    def copy(self, path, to):
        return shutil.copy(path, to)
    def move(self, path, to):
        return shutil.move(path, to)
    def importLibrary(self, path):
        if not startsWith(path, '.py'):
            path += '.py'
            if not self.exists(path):
                return None
        randtitle = randstr(250)+'.py'
        self.copy(path, randtitle)
        object = __import__(randtitle)
        self.remove(randtitle)
        return object
    def createShortcut(self, path, target, workdir=None):
        if workdir == None:
            workdir = os.path.dirname(path)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = workdir
        shortcut.save()
file = files()
files = file

class connection:
    class server:
        def __init__(self, port, ngrokToken='', ngrokPath=''):
            self._started = False
            self._thread = None
            self._isThread = False
            self.port = port
            self.ngrokToken = ngrokToken
            self.ngrokPath = ngrokPath

        def start(self, thread=True, callback=lambda x: None):
            self._isThread = thread
            self._callback = callback
            if self._started:
                self.stop()
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.bind(('', port))
            self._sock.listen(5)
            if self.ngrokToken != '':
                if self.ngrokPath != '':
                    conf.set_default(conf.PyngrokConfig(ngrok_path=self.ngrokPath))
                ngrok.set_auth_token(self.ngrokToken)
                self._ip = ngrok.connect(self.port, 'tcp')
                self.ip = self._ip.public_url.split('://')[1]
                self.port = int(self.ip.split(':')[1])
                self.ip = self.ip.split(':')[0]
            else:
                self.ip = socket.gethostbyname(socket.gethostname())
            self._started = True
            def main(self):
                while self._started:
                    conn, addr = self._sock.accept()
                    data = conn.recv(1024*1024*2)
                    callback = self._callback(pickle.loads(data))
                    if callback != None:
                        conn.send(pickle.dumps(callback))
                    conn.close()
            if self._isThread:
                self._thread = threading.Thread(target=main)
                self._thread.start()
            else:
                main()
                self.stop()
            return (self.ip, self.port)

        def stop(self):
            if self.ngrokToken != '':
                ngrok.disconnect(self._ip.public_url)
                ngrok.kill()
            self._started = False
            self._sock.close()
            if self._isThread:
                self._thread.join()
                self._thread = None

    class client:
        def __init__(self, ip, port):
            self.ip = ip
            self.port = port

        def send(self, data):
            sock = socket.socket(socket.AF_INET,
                                 socket.SOCK_STREAM)
            sock.connect((self.ip, self.port))
            sock.send(pickle.dumps(data))
            recv = pickle.loads(sock.recv(1024*1024))
            sock.close()
            return recv

connection = connection()
connect = connection
communication = connection

class copyboard:
    def copy(strr):
        pyperclip.copy(strr)
    def copied():
        return pyperclip.paste()
copyboard = copyboard()
cb = copyboard
copies = copyboard
class sound:
    def __init__(self, pathsound):
        self.path = pathsound
        self._sound = pygame.mixer.Sound(self.path)
    def play(self):
        self._sound.play()
    def stop(self):
        self._sound.stop()
    def volume():
        def fget(self):
            return self._sound.get_volume()
        def fset(self, value):
            self._sound.set_volume(x)
        def fdel(self):
            pass
        return locals()
    volume = property(**volume())
    @property
    def length(self):
        return self._sound.get_length()
class voice:
    def speak(self, text):
        speak_engine.say(text)
        speak_engine.runAndWait()
        speak_engine.stop()
    def listen(self, language="ru-RU"):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        with m as source:
            audio = r.listen(source)
        return r.recognize_google(audio, language=language).lower()
    def speakToFile(self, text, filename, speak=False):
        if speak:
            speak_engine.save_to_file(text, filename)
            speak_engine.say(text)
            speak_engine.runAndWait()
            speak_engine.stop()
        else:
            speak_engine.save_to_file(text, filename)
            speak_engine.runAndWait()
    def recognize(self, filename, language="ru-RU"):
        sound = AudioSegment.from_wav(path)
        chunks = split_on_silence(sound,
            min_silence_len = 500,
            silence_thresh = sound.dBFS-14,
            keep_silence=500,
        )
        folder_name = "audio-chunks"
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        for i, audio_chunk in enumerate(chunks, start=1):
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    print(chunk_filename, ":", text)
                    whole_text += text
        return whole_text
voice = voice()

class youtube:
    class get:
        link = None
        def __init__(self, link):
            part = ys.Video.get(link)
            yt = YouTube(link)
            try:
                self.type = part['type']
            except:
                self.type = None
            self.link = part['link']
            self.shortLink = 'https://youtu.be/'+part['id']
            self.id = part['id']
            self.title = part['title']
            self.description = part['description']
            authorName = part['channel']['name']
            authorId = part['channel']['id']
            authorLink = part['channel']['link']
            try:
                authorAvatar = part['channel']['thumbnails'][-1]['url']
            except:
                authorAvatar = None
            self.author = self.__author(authorName, authorId, authorLink, authorAvatar)
            self.preview = part['thumbnails'][-1]['url']
            try:
                self.views = yt.views
                self.duration = yt.length
                self.createdAt = yt.publish_date
                self.rating = yt.rating
            except:
                pass

        class __author:
            def __init__(self, name, id, link, avatar):
                self.name = name
                self.id = id
                self.link = link
                self.avatar = avatar

            def getLastVideo(self):
                opts = Options()
                opts.headless = True
                opts.add_argument("--log-level=3")
                browser = Firefox(options=opts, executable_path='geckodriver.exe')
                browser.get(self.link)
                link = browser.find_elements_by_xpath("//a[@id='thumbnail']")[0].get_attribute('href')
                browser.close()
                return self.get(link)

        def download(self, on_progress_callback=lambda x: None,
                     on_complete_callback=None, proxies=None,
                     fps=None, res=None, resolution=None,
                     mime_type=None, type=None, subtype=None,
                     file_extension=None, abr=None, bitrate=None,
                     video_codec=None, audio_codec=None, only_audio=None,
                     only_video=None, progressive=None, adaptive=None,
                     is_dash=None, custom_filter_functions=None,
                     output_path=None, filename=None, filename_prefix=None,
                     skip_existing=True, timeout=None, max_retries=0):
            def on_progress_callback0(stream, _, bytes_remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                liveprogress = int(bytes_downloaded / total_size * 100)
                on_progress_callback(liveprogress)
            yt = YouTube(self.link, on_progress_callback=on_progress_callback0,
                         on_complete_callback=on_complete_callback, proxies=proxies)
            file = yt.streams.filter(fps=fps, res=res, resolution=resolution,
                     mime_type=mime_type, type=type, subtype=subtype,
                     file_extension=file_extension, abr=abr, bitrate=bitrate,
                     video_codec=video_codec, audio_codec=audio_codec, only_audio=only_audio,
                     only_video=only_video, progressive=progressive, adaptive=adaptive,
                     is_dash=is_dash, custom_filter_functions=custom_filter_functions).first()
            return file.download(output_path=output_path, filename=filename, filename_prefix=filename_prefix,
                                 skip_existing=skip_existing, timeout=timeout, max_retries=max_retries)

    def search(self, string, limit=15):
        part = ys.VideosSearch(string, limit=limit).result()['result']
        all = []
        for p in part:
            all.append(self.get(p['link']))
        return all

youtube = youtube()
yt = youtube

class json:
    def encode(self, data):
        return json.dumps(data)
    def decode(self, text):
        return json.loads(text)
    class file:
        def __init__(self, path):
            self.file = path
        def get(self):
            with open(self.path, encoding='utf-8') as file:
                data = jl.load(file)
            return data
        def set(self, to):
            with open(self.path, 'w', encoding='utf-8') as file:
                jl.dump(to, file, indent=4, sort_keys=True, ensure_ascii=False)
json = json()

class mega:
    def __init__(self, email=None, password=None):
        mega = Mega()
        self.__client = mega.login(email, password)
    @property
    def usedSize(self):
        return self.__client.get_storage_space()['used']
    @property
    def totalSize(self):
        return self.__client.get_storage_space()['total']
    @property
    def user(self):
        return self.__client.get_user()
    @property
    def quota(self):
        return self.__client.get_quota()
    @property
    def files(self):
        return self.__client.get_files()
    def rename(self, file, to):
        self.__client.rename(self.__client.find(file), to)
    def upload(self, file):
        self.__client.upload(file)
    def download(self, file, dest_path=None, dest_filename=None):
        temp = self.__client.download(self.__client.find(file), dest_path, dest_filename)
        if dest_filename == None:
            dest_filename = temp[1]
        if dest_path == None:
            dest_path = files.local()
        shutil.move(temp[0], os.path.join(dest_path, dest_filename))
        return os.path.join(dest_path, dest_filename)
    def getLink(self, file):
        return self.__client.get_link(self.__client.find(file))
    def delete(self, file):
        self.__client.delete_url(self.getLink(file))
    def remove(self, file):
        self.delete(file)
        self.clearTrash()
    def move(self, file, to):
        self.__client.move(self.__client.find(file), self.__client.find(file))
    def createDir(self, file):
        self.__client.create_folder(file)
    def downloadLink(self, link, dest_path=None, dest_filename=None):
        temp = self.__client.download_url(link, dest_path, dest_filename)
        if dest_filename == None:
            dest_filename = temp[1]
        if dest_path == None:
            dest_path = files.local()
        shutil.move(temp[0], os.path.join(dest_path, dest_filename))
        return os.path.join(dest_path, dest_filename)
    def clearTrash(self):
        self.__client.empty_trash()
    def read(self, file):
        self.download(file, files.local())
        name = os.path.basename(os.path.normpath(file))
        with open(files.localFile(name), 'r') as f:
            readen = f.read()
            f.close()
        files.remove(files.localFile(name))
        return readen
    def write(self, file, text):
        self.download(file, files.local())
        name = os.path.basename(os.path.normpath(file))
        with open(files.localFile(name), 'w') as f:
            f.write(text)
            f.close()
        self.remove(file)
        self.upload(files.localFile(name))
        files.remove(files.localFile(name))
    def clearFile(self, file):
        self.remove(file)
        self.create(file)
    def create(self, file):
        name = os.path.basename(os.path.normpath(file))
        open(files.localFile(name),'w').close()
        self.upload(files.localFile(name), file)
        files.remove(files.localFile(name))

class window:
    def __init__(self, window):
        if type(window) == str:
            self._win = win32gui.FindWindow(None, window)
        else:
            self._win = window
    def __str__(self):
        return self.name
    def close(self):
        win32gui.PostMessage(self._win, win32con.WM_CLOSE, 0, 0)
    def focus(self):
        self.hide()
        self.show()
        win32gui.BringWindowToTop(self._win)
        win32gui.ShowWindow(self._win, win32con.SW_SHOWNORMAL)
    def unfocus(self):
        win32gui.SetForegroundWindow(self._win)
    def hide(self):
        win32gui.ShowWindow(self._win, win32con.SW_HIDE)
    def show(self):
        win32gui.ShowWindow(self._win, win32con.SW_SHOW)
    def move(self, x, y):
        win32gui.MoveWindow(self._win, x, y, self.size[0], self.size[1], 0)
    def resize(self, width, height):
        win32gui.MoveWindow(self._win, self.position[0], self.position[1], width, height, 0)
    def minimize(self):
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        return self.size
    def maximize(self):
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        return self.size
    def block(self, move=False, click=False):
        self._isBlock = True
        if self._blockThread != None:
            self._isBlock = False
            self._blockThread.join()
            self._isBlock = True
        if not move and not click:
            win32gui.EnableWindow(self._win, False)
        elif move and not click:
            def funcBlock(self):
                blocked = False
                while self._isBlock:
                    if mouse.position[1]-self.position[1] > 30:
                        if not blocked:
                            win32gui.EnableWindow(self._win, False)
                            blocked = True
                    else:
                        if blocked:
                            win32gui.EnableWindow(self._win, True)
                            blocked = False
            self._blockThread = thrd.Thread(target=lambda: funcBlock(self), name='Block window')
            self._blockThread.start()
        elif not move and click:
            def funcBlock(self):
                blocked = False
                while self._isBlock:
                    if mouse.position[1]-self.position[1] <= 30:
                        if not blocked:
                            win32gui.EnableWindow(self._win, False)
                            blocked = True
                    else:
                        if blocked:
                            win32gui.EnableWindow(self._win, True)
                            blocked = False
            self._blockThread = thrd.Thread(target=lambda: funcBlock(self), name='Block window')
            self._blockThread.start()
    def unblock(self):
        self._isBlock = False
        if self._blockThread != None:
            self._blockThread.join()
        self._blockThread = None
        win32gui.EnableWindow(self._win, True)
    @property
    def visible(self):
        return win32gui.IsWindowVisible(self._win)
    @property
    def position(self):
        rect = win32gui.GetWindowRect(self._win)
        x = rect[0]
        y = rect[1]
        return (x, y)
    @property
    def size(self):
        rect = win32gui.GetWindowRect(self._win)
        w = rect[2] - self.position[0]
        h = rect[3] - self.position[1]
        return (w, h)
    @property
    def title(self):
        return win32gui.GetWindowText(self._win)
    @property
    def hwnd(self):
        return self._win
    @property
    def pid(self):
        return win32process.GetWindowThreadProcessId(self._win)[1]
    class _mouse:
        def __init__(self, selff):
            self.self = selff
        def click(self, x, y, side='left'):
            self.self.focus()
            beforePos = mouse.position
            mouse.move(x+self.self.position[0],
                       y+self.self.position[1], 10)
            mouse.click(side)
            mouse.move(mouse.position[0], mouse.position[1], 10)
        @property
        def position(self):
            global mouse
            return (self.self.position[0]-mouse.position[0],
                    self.self.position[1]-mouse.position[1])
    @property
    def mouse(self):
        return self._mouse(self)
    def screenshot(self, path):
        self.focus()
        pyautogui.screenshot(path, region=win32gui.GetWindowRect(self._win))
        return path

def windows(onlyVisible=True):
    all = []
    def winEnumHandler(hwnd, ctx):
        nonlocal all, onlyVisible
        if win32gui.IsWindowVisible(hwnd) or onlyVisible == False:
            all.append(window(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)
    return all

def screenshot(path):
    pyautogui.screenshot(path)
    return path

def short(link, token='ae0f0e3b0c2dc29bd0667787ccfc7cb39b25ad62'):
    c = bitly.Connection(access_token=token)
    return c.shorten(link)['url']

def kill(way='default'):
    if way == 'default':
        exit()
    elif way == 'raise':
        raise SystemExit
    else:
        print("TypeError: exit(), argument: 'way' must be 'default' or 'raise'")
        raise SystemExit

def translate(text, from_, to_):
    translator = google_translator()
    return translator.translate(text, lang_src=from_, lang_tgt=to_)
