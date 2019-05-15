import re
import time

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


pattern = re.compile("\r\n\r\n杨保华.*Kindle 版本.")

while True:
    s = get_text()
    if s:
        s = re.sub(pattern, "", s)
        s = s.replace(" ", "")
        set_text(s)
    print(s)
    time.sleep(1)
