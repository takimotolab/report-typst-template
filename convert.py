"""
convert.py

report.typの、を，に。を．に変換するスクリプトです。
普段、と。を使っていて設定を変えるのが面倒くさい人は
最後にこのスクリプトを使って，と．に変換すると便利です。
"""

with open('report.typ', 'r', encoding='utf-8', newline='') as file:
    content = file.read()

content = content.replace('、', '，').replace('。', '．').replace('\r\n', '\n').replace('\r', '\n')

with open('report.typ', 'w', encoding='utf-8', newline='') as file:
    file.write(content)
