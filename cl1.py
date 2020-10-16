import sys

Words = dict()

w1 = input()
w2 = input()

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

for i in range(len(w1)):
    if ('0'<= w1[i]) and (w1[i] <= '9'):
        sys.exit("Please, do not use numbers")
    else:
        if (('a' <= w1[i]) and (w1[i] <= 'z')) or (('A' <= w1[i]) and (w1[i] <= 'Z')):
            cnt1 += 1
        elif (('а' <= w1[i]) and (w1[i] <= 'я')) or (('А' <= w1[i]) and (w1[i] <= 'Я')):
            cnt2 += 1
if (cnt1!=0 and cnt1 != len(w1)) or (cnt2!=0 and cnt2 != len(w1)):
    sys.exit("Mistake in word 1")

for i in range(len(w2)):
    if ('0'<= w2[i]) and (w2[i] <= '9'):
        sys.exit("Please, do not use numbers")
    else:
        if (('a' <= w2[i]) and (w2[i] <= 'z')) or (('A' <= w2[i]) and (w2[i] <= 'Z')):
            cnt3 += 1
        elif (('а' <= w1[i]) and (w2[i] <= 'я')) or (('А' <= w2[i]) and (w2[i] <= 'Я')):
            cnt4 += 1
if (cnt3!=0 and cnt3 != len(w2)) or (cnt4!=0 and cnt4 != len(w2)):
    sys.exit("Mistake in word 2")

if cnt1 == len(w1) and cnt4 == len(w2):
    Words[w1] = w2
    print(w1, " in English is ", w2, " in Russian")
elif cnt2 == len(w1) and cnt3 == len(w2):
    Words[w2] = w1
    print(w2, "in English is", w1, "
          in Russian")
else:
    sys.exit("Something went wrong...")
    
    


