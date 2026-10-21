import random
import json
my_list=["お菓子を選びあう","写真を撮る","散歩する"]
friend_list=["好きな曲を聴く","変顔する","飲み物を選びあう"]
all_list=my_list+friend_list
import os
if os.path.exists("actions.json"):
    with open("actions.json","r",encoding="utf-8")as f:
        all_list=json.load(f)
        if os.path.exists("actions.json"):
            with open("actions.json","r",encoding="utf-8")as f:
                all_list=json.load(f)
                all_list=[item for item in all_list if item!=""]
new_action=input("追加したいことを入力してね:")
if new_action!="":
    all_list.append(new_action)
    print("追加しました")
else:
    print("何も追加しませんでした")
history=[]
if os.path.exists("history.json"):
    with open("history.json","r",encoding="utf-8")as f:
        history=json.load(f)
while len(all_list)>0:
    selected=random.choice(all_list)
    print("今日やることは")
    print(selected)
    all_list.remove(selected)
    history.append(selected)
    comment=input("ひと言コメントを書いてね")
    history[-1]={"action":selected,"coment":comment}
    print("残りの候補",all_list)
    answer=input("もう一度抽選する？ yes/no:")
    if answer=="no":
        break
with open("actions.json","w",encoding="utf-8")as f:
    json.dump(all_list,f,ensure_ascii=False)
print("今回の抽選履歴",history)
with open("history.json","w",encoding="utf-8")as f:
    json.dump(history,f,ensure_ascii=False)