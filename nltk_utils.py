import nltk

rizal = "Kenalkan Nama Saya Rizal Mujahiddan, Kalau nama kamu siapa ?"

# Pysastrawi , Stemming for indonesian
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

output   = stemmer.stem(rizal)

print(output)

# nltk.demo()
# print(nltk.word_tokenize(rizal))
# print(help(nltk.word_tokenize))