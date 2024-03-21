# bin(), oct(), hex()で、数値を2進数、8進数、16進数に変換
k = int(input())
s = str(bin(k)[2:]).replace('1', '2')
print(s)