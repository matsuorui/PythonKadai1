# ユーザーに番号を尋ね,番号が偶数か奇数かに応じて，適切なメッセージをユーザーに出力 する．
# また，数値が 4 の倍数の場合、別のメッセージを出力.
print('番号を入力してください。')
n=int(input())
if n%2==0:
    print('偶数です。')
else:print('奇数です。')
if n%4==0:\
    print('4の倍数です。')
