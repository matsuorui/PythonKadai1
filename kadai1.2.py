# 数を 10 個入力してその合計を表示するプログラムを作る
print('数を 10 個入力してください')
sum=0
for i in range(10):
    i=int(input())
    sum=sum+i

print('合計＝{}'.format(sum))