#input，print，変数の 3 つだけで借金返済計画（無利子）を立てるプログラムを作る
#借金の総額と，ひと月に返済する金額を入力すると，返済にかかる年数を表示しする
# さらに，毎年のボーナスから返済する金額を入力すると，返済完了が何年早まるかを表示する
# その次に返済を完了したい年数を入力すると，ボーナスからいくら返せばよいかを表示する
import math
sum=0
a=0
b=0
print('借金の総額を入力してください。')
sum=int(input())
print('ひと月に返済する金額を入力してください。')
a=int(input())
b=sum/a/12
print('返済にかかる年数は'+str(math.ceil(b))+'年間です。')