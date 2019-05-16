

#Remove punctuations from a given a sentence and count the word frequency
text = 'hello this is swaroop. How are you doing with training. I hope training is going well.'
punc_list = ['.',';',',','?']
new_txt = "".join(text.split('.'))
print(new_txt)
word_dict = dict()

for word in new_txt.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)

#how to remove if there are many such punctuations
import re
new_text = 'this is a punctuation test sentence, try removing the punctuations. All the best!'
punct_text = re.sub(r'[.,!?]','', new_text)
print(punct_text)
