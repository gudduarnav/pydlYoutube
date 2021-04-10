# helper

import os

try:
    import win32clipboard
except ImportError as __ex:
    print("Install win32clipboard. Exception:", str(__ex))
    exit(1)

try:
    from tkinter import filedialog
    from tkinter import Tk
except ImportError as __ex:
    print("Install tkinter. Exception:", str(__ex))
    exit(1)

def getUserProfile() -> str:
    return os.environ["USERPROFILE"]


def getDesktopPath() -> str:
    return os.path.join(getUserProfile(), "Desktop")+"\\"


def getCurrentPath() -> str:
    return os.path.dirname(__file__)+"\\"

def execyoutubedl(cmdList : list):
    try:
        cmdline = "{}\\{} {}".format(getCurrentPath(), "youtube-dl", " ".join(cmdList))
        print(cmdline)
        os.system(cmdline)
    except Exception as ex:
        print("execyoutubedl(...) Exception:", str(ex))


def getClipboardText():
    try:
        win32clipboard.OpenClipboard()
        data =  win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        return data
    except:
        return ""

def getDirName():
    try:
        root = Tk()
        root.withdraw()
        return filedialog.askdirectory()
    except:
        return ""