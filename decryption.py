import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = open('word.txt','r')
    word_file = list(word_file)

    anagram = "I am Iron Man"
    words = anagram.count('')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    for i in word_file:
     flag = False
     temp_word = i.replace('\n',' ')
     temp_char = list(set(temp_word))
     for r in temp_char:
        if r not in char_list:
           flag = True
           break
     if flag == False:
        final_words.append(temp_word)
 
     print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)

        sol = hashlib.md5()
        sol.update(hash_elem.encode('utf-8'))
        word_hash = sol.hexdigest()

        if word_hash == original_hash:
          return hash_elem()
    
hash = '13b382e1a2f8e22535b4730d78bc8591'
answer = find_hash(hash)
print(f'EUREKA! THE WORD CORRESPONDING TO THE GIVE HASH IS {answer}')