import nltk
import re 

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

text = ''

# def count_words(text):

#     candidate_words = text.split()

#     word_count = 0

#     for candidate in candidate_words:
#         word = re.sub(r'[^A-Za-z]+','', candidate)
#         if word.lower() in word_list or word in name_list:
#             # print("english word", word)
#             word_count += 1
#         else:
#             pass
#             # print('not english word or name', word)

#     return word_count

# def encrypt(text,key):
#     encrypted = ""
#     for i in text.lower():

#         encrypted+=chr(ord(i)+key)
#     return(encrypted)


def encrypt(string, key):
    
    output = ''
    for i in string.lower():

        if ord(i)>96 and ord(i)<123:
            a = ord(i) - 97
            new = a+key
            new_ascci = new%26 + 97
            output+=chr(new_ascci)

        elif i == ' ':
            output += i


    return output



def decrypt(text,key):
   return encrypt(text, -key)

def crack(text,key):
    pass


print(encrypt("Klz",10))
print(decrypt("uvj",10))