import tkinter
from tkinter import filedialog

def import_music():
    root = tkinter.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 弹出目录选择对话框
    
    if not folder_path:  # 如果用户没有选择文件夹
        return None  # 或者可以根据你的需求决定返回什么值
    
    return folder_path  # 返回用户选择的文件夹路径