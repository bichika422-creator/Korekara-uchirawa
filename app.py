import tkinter as tk
from tkinter import simpledialog
import json
from tkinter import messagebox
def add_action():
    action=simpledialog.askstring("追加","やりたいことを入力してね")
    if action:
        with open("actions.json","r",encoding="utf-8")as f:
            actions=json.load(f)
        actions.append(action)
        with open("actions.json","w",encoding="utf-8")as f:
            json.dump(actions,f,ensure_ascii=False)   
import random
def draw_action():
    with open("actions.json","r",encoding="utf-8")as f:
        actions=json.load(f)
    if actions:
        selected=random.choice(actions)
        answer=messagebox.askyesno("抽選結果",selected+"\n完了した？")
        if answer:
            comment=simpledialog.askstring("完了","ひと言コメントを書いてね")
            actions.remove(selected)  
            with open("actions.json","w",encoding="utf-8")as f:
                json.dump(actions,f,ensure_ascii=False)
            with open("history.json","r",encoding="utf-8")as f:
                history=json.load(f)
            history.append({"action":selected,"comment":comment or ""})
            with open("history.json","w",encoding="utf-8")as f:
                json.dump(history,f,ensure_ascii=False)        
    else:
        messagebox.showinfo("抽選結果","候補がありません")
def show_history():
    with open("history.json","r",encoding="utf-8")as f:
        history=json.load(f)
    if not history:
       messagebox.showinfo("過去の記録","まだ記録がありません") 
       return
    text=""
    for item in history:
        if isinstance(item,dict):
            text+=item["action"]+"\n"
            text+="ひとこと:"+str(item.get("comment","なし"))+"\n\n"
        else:    
            text+=item+"\n\n"
    messagebox.showinfo("過去の記録",text)
app=tk.Tk()
app.title("これからうちらは")
app.geometry("400x500")
title=tk.Label(app,text="これからうちらは",font=("Arial",20))
title.pack(pady=30)
add_button=tk.Button(app,text="追加",command=add_action)
add_button.pack(pady=10)
draw_button=tk.Button(app,text="抽選",command=draw_action)
draw_button.pack(pady=10)
history_button=tk.Button(app,text="過去の記録",command=show_history)
history_button.pack(pady=10)
app.mainloop()