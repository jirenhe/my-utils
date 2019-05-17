import re
import time
import traceback

import win32clipboard as wincld
import win32con


def get_text():
    wincld.OpenClipboard()
    try:
        text_result = wincld.GetClipboardData(win32con.CF_UNICODETEXT)
        return text_result
    except:
        return None
    finally:
        wincld.CloseClipboard()


def set_text(info):
    wincld.OpenClipboard()
    wincld.EmptyClipboard()
    wincld.SetClipboardData(win32con.CF_UNICODETEXT, info)
    wincld.CloseClipboard()


pattern = re.compile(r"\r\n\r\n.*Kindle 版本.")
pattern2 = re.compile(r"([^\x00-\xff])\s+([^\x00-\xff])")
pattern3 = re.compile(r"([/:.\\<[_-])\s+")
pattern4 = re.compile(r"(?<!\s)(\[[a-zA-Z]+?.*?\])")
pattern5 = re.compile(r"([A-Za-z])(<.*?>)")
pattern6 = re.compile(r"([a-zA-Z])(-+)")

while True:
    try:
        s = get_text()
        if s:
            s = re.sub(pattern, "", s)
            s = re.sub(pattern2, lambda x: x.group(1) + x.group(2), s)
            s = re.sub(pattern3, lambda x: x.group(1), s)
            s = re.sub(pattern4, lambda x: " " + x.group(1), s)
            s = re.sub(pattern5, lambda x: x.group(1) + " " + x.group(2), s)
            s = re.sub(pattern6, lambda x: x.group(1) + " " + x.group(2), s)
            set_text(s)
        print(s)
    except Exception as e:
        traceback.print_exc()
        pass
    finally:
        time.sleep(1)
