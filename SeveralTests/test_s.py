'''テスト'''
import tkinter as tk
from instabot import Bot

root = tk.Tk()
root.title("Test App")
root.geometry("500x500")
bot = Bot()

name_label = tk.Label(text="ユーザー名を入れてください", foreground='#000000')
name_label.pack()
name_entry = tk.Entry(width=30)
name_entry.pack()

pass_name = tk.Label(text="パスワードを入れてください", foreground='#000000')
pass_name.pack()
pass_entry = tk.Entry(width=30)
pass_entry.pack()

def log_in(event):
    '''ログインする'''
    bot.login(username=name_entry.get(),
              password=pass_entry.get())


button = tk.Button(text="ログイン", width=20)
button.bind("<Button-1>", log_in)
button.pack()


root.mainloop()
