from nltk.tokenize import sent_tokenize,word_tokenize

file=open("data").read()
sentences=sent_tokenize(file)

print(len(sentences))
#for each_sent in sentences:
#print(len(word_tokenize(each_sent)))
