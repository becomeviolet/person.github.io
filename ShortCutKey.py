import pyautogui
def backToDesktop():
    """使用快捷键返回桌面"""
    pyautogui.hotkey('win', 'd')

def lockDesktop():
    """锁住桌面"""
    pyautogui.hotkey('win','l')

def shear():
    """使用快捷键剪切"""
    pyautogui.hotkey('ctrl', 'x')

def copy():
    """使用快捷键复制"""
    pyautogui.hotkey('ctrl','c')

def stick():
    """使用快捷键粘贴"""
    pyautogui.hotkey('ctrl','v')

