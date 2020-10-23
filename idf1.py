import collections
import math
#все время пишет 0
# *звуки паники*
def count_idf(word, corpus):
    if corpus.count(word)==0: 
        return 0
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))


txt1 = []
txt2 = []
txt3 = []
txt4 = []



with open('kak_delat_stihi.txt', 'r') as myself:
    for word in myself.read().split():
        txt1.append (word)
with open('i_snova_tuchi.txt', 'r') as myself:
    for word in myself.read().split():
        txt2.append (word)
with open('bolshevism_yesenin.txt', 'r') as myself:
    for word in myself.read().split():
        txt3.append (word)
with open('nezavisimost_kuhelbecker.txt', 'r') as myself:
    for word in myself.read().split():
        txt4.append (word)  
         
print (count_idf('стихи',[txt1,txt2,txt3,txt4]))
print (count_idf('революция',[txt1,txt2,txt3,txt4]))


