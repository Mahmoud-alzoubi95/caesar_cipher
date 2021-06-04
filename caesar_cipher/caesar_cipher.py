import nltk
import re 

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

text = ''



def encrypt(string,key):
    
    output = ''
    for i in string:

        if ord(i)>96 and ord(i)<123:
            a = ord(i) - 97
            new = a+key
            new_ascci = new%26 + 97
            output+=chr(new_ascci)

        
        if ord(i) > 65 and ord(i) < 97:
            a = ord(i) - 65
            new = a+key
            new_ascci = new%26 + 65
            output+=chr(new_ascci)
        

        elif i == ' ':
            output += i


    return output


def decrypt(text,key):
   return encrypt(text, -key)



def crack(tar):
    parse_in = 0
    for i in range(len(tar.split())*26):
        candidate_dec = decrypt(tar, i)
        word_count = is_english_words(candidate_dec)
        perce = int(word_count / len(candidate_dec.split()) * 100)
        if perce > parse_in:
            parse_in = perce 
            decrypt_word = candidate_dec
    return decrypt_word

nltk.download('words')
english_words = nltk.corpus.words.words()

nltk.download('words')
english_words = nltk.corpus.words.words()


def is_english_words(sent):
    new_word = sent.split()
    count = 0
    for i in new_word:
        if i in english_words or i.lower() in english_words or i.upper() in english_words:
            count += 1
    return count



if __name__ == '__main__':
    a = encrypt('my age ten',10)
    print(a)




# print(encrypt("Klz",10))
# print(decrypt("uvj",10))