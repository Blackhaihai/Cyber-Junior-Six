import tkinter as tk
from tkinter import messagebox
import random

# 小六壬固定排列，依次为大安 -> 空亡
elements = ['大安', '留连', '速喜', '赤口', '小吉', '空亡']

# 十二时辰表，顺序为子时=1，丑时=2，以此类推到亥时=12
time_periods = [
    ("子时", 23, 0, 1), ("丑时", 1, 2, 2), ("寅时", 3, 4, 3),
    ("卯时", 5, 6, 4), ("辰时", 7, 8, 5), ("巳时", 9, 10, 6),
    ("午时", 11, 12, 7), ("未时", 13, 14, 8), ("申时", 15, 16, 9),
    ("酉时", 17, 18, 10), ("戌时", 19, 20, 11), ("亥时", 21, 22, 12)
]

def get_time_period(hour, minute):
    """获取时间对应的时辰名称和编号"""
    for name, start, end, number in time_periods:
        if (start == 23 and hour == 23) or (end == 0 and hour == 0) or (start <= hour <= end):
            return name, number
    return "未知时辰", 0

def calculate_elements(n1, n2, n3):
    """递归计算小六壬结果"""
    first_index = (n1 - 1) % 6
    second_index = (first_index + (n2 - 1)) % 6
    third_index = (second_index + (n3 - 1)) % 6
    result = elements[first_index], elements[second_index], elements[third_index]
    return result

def get_elements():
    """获取用户输入并计算结果"""
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        n3 = int(entry3.get())
        result = calculate_elements(n1, n2, n3)
        result_label.config(text=f"结果: {result[0]}, {result[1]}, {result[2]}")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")

def random_elements():
    """随机生成三组数字并计算"""
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    n3 = random.randint(1, 9)
    var1.set(n1)
    var2.set(n2)
    var3.set(n3)
    result = calculate_elements(n1, n2, n3)
    result_label.config(text=f"随机问卦结果: {result[0]}, {result[1]}, {result[2]}")

def advanced_query():
    """进阶问卦计算"""
    try:
        month = int(month_entry.get())
        day = int(day_entry.get())
        time_input = time_entry.get()
        hour, minute = map(int, time_input.split(":"))
        time_name, time_number = get_time_period(hour, minute)
        time_name_label.config(text=f"时辰: {time_name} ({time_number})")
        result = calculate_elements(month, day, time_number)
        advanced_result_label.config(text=f"进阶问卦结果: {result[0]}, {result[1]}, {result[2]}")
    except (ValueError, IndexError):
        messagebox.showerror("错误", "请输入有效的日期和时间格式！")

def show_advanced():
    """显示进阶问卦界面，隐藏基础问卦"""
    title_label.config(text="进阶问卦")
    normal_frame.pack_forget()  # 隐藏基础问卦功能
    advanced_frame.pack(pady=20)  # 显示进阶问卦功能

def show_basic():
    """返回基础问卦界面，隐藏进阶问卦"""
    title_label.config(text="赛博小六壬")
    advanced_frame.pack_forget()  # 隐藏进阶问卦功能
    normal_frame.pack(pady=10)  # 显示基础问卦功能

# 创建GUI窗口
root = tk.Tk()
root.title("赛博小六壬")
root.geometry("500x500")  # 窗口大小

# 设置窗口居中显示
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2
y = (screen_height - 700) // 2
root.geometry(f"+{x}+{y}")

# 标题
title_label = tk.Label(root, text="赛博小六壬", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

# 普通问卦区域
normal_frame = tk.Frame(root)
normal_frame.pack(pady=10)

normal_title_label = tk.Label(normal_frame, text="普通问卦", font=("Arial", 16))
normal_title_label.grid(row=0, column=0, columnspan=3, pady=5)

entry_frame = tk.Frame(normal_frame)
entry_frame.grid(row=1, column=0, columnspan=3, pady=5)

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

entry1 = tk.Entry(entry_frame, textvariable=var1, width=5, font=("Arial", 14))
entry1.grid(row=0, column=0, padx=5)
entry2 = tk.Entry(entry_frame, textvariable=var2, width=5, font=("Arial", 14))
entry2.grid(row=0, column=1, padx=5)
entry3 = tk.Entry(entry_frame, textvariable=var3, width=5, font=("Arial", 14))
entry3.grid(row=0, column=2, padx=5)

submit_button = tk.Button(normal_frame, text="提交", command=get_elements, font=("Arial", 14))
submit_button.grid(row=2, column=0, columnspan=3, pady=10)

ask_button = tk.Button(normal_frame, text="问卦", command=random_elements, font=("Arial", 14))
ask_button.grid(row=3, column=0, columnspan=3, pady=10)

result_label = tk.Label(normal_frame, text="结果:", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=3, pady=5)

advanced_button = tk.Button(root, text="进阶问卦", command=show_advanced, font=("Arial", 14))
advanced_button.pack(pady=10)

# 进阶问卦区域（初始隐藏）
advanced_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)

advanced_title_label = tk.Label(advanced_frame, text="进阶问卦", font=("Arial", 16))
advanced_title_label.grid(row=0, column=0, columnspan=2, pady=5)

month_label = tk.Label(advanced_frame, text="月:", font=("Arial", 12))
month_label.grid(row=1, column=0, pady=5, sticky="e")
month_entry = tk.Entry(advanced_frame, width=5, font=("Arial", 12))
month_entry.grid(row=1, column=1, pady=5)

day_label = tk.Label(advanced_frame, text="日:", font=("Arial", 12))
day_label.grid(row=2, column=0, pady=5, sticky="e")
day_entry = tk.Entry(advanced_frame, width=5, font=("Arial", 12))
day_entry.grid(row=2, column=1, pady=5)

time_label = tk.Label(advanced_frame, text="时间 (HH:MM):", font=("Arial", 12))
time_label.grid(row=3, column=0, pady=5, sticky="e")
time_entry = tk.Entry(advanced_frame, width=10, font=("Arial", 12))
time_entry.grid(row=3, column=1, pady=5)

time_name_label = tk.Label(advanced_frame, text="时辰: ", font=("Arial", 12))
time_name_label.grid(row=4, column=0, columnspan=2, pady=5)

advanced_button = tk.Button(advanced_frame, text="问卦", command=advanced_query, font=("Arial", 12))
advanced_button.grid(row=5, column=0, columnspan=2, pady=10)

advanced_result_label = tk.Label(advanced_frame, text="结果:", font=("Arial", 14))
advanced_result_label.grid(row=6, column=0, columnspan=2, pady=5)

back_button = tk.Button(advanced_frame, text="返回", command=show_basic, font=("Arial", 12))
back_button.grid(row=7, column=0, columnspan=2, pady=10)

# 启动主循环
root.mainloop()
