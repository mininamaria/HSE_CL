import collections


def count_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

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
                                    
print (count_tf(txt1))
print (count_tf(txt2))
print (count_tf(txt3))
print (count_tf(txt4))
