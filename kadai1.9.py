#ユーザーに文字列を尋ね，この文字列が回文であるかどうかを出力する．
# （回文は，前から，後ろ から両方を読み取る文字列です。）
print("文字列を教えてください。")
string=str(input())
if string==string[::-1]:
    print("回文です")
else:print("回文ではありません")