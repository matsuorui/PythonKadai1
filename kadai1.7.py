#ユーザーに名前と年齢の入力を求めるプログラムを作成する．
# 彼らが 100 歳になる年を告げる メッセージを表示してください
name=''
age=0
year=0
print('ユーザー名を入力してください。')
name=str(input())
print('年齢を入力してください。')
age=int(input())
year=2019+(100-age)
print(name+'さんが100歳になるのは'+str(year)+'年です。')