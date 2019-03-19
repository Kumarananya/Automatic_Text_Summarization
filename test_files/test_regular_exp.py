##import re
##import time
##
##file1=open("file1.txt")
##
##for line in file1:
##    print(re.sub('^([Nn]onetheless|[Mm]oreover),? ?',"",line))


##def whose_whom(doc):
##
##    return re.sub(',who[(se)|(m)] .+ ?,',"",doc)

##print(re.sub('[(who)|(google)]',"",file1))

##print(re.findall('[0-9 a-z]',file1))

##print(re.findall('\S+@\S+',file1))

##print(re.findall('\.',file1))

##print(re.findall('[0-9a-z\.('a')]',file1))
##for line in file1:
##    print(line)
##    time.sleep(10)

##print(re.findall('I am',file1))

##for line in file1:
##    print(re.findall('^I want.*',line))
    
from nltk.tokenize import sent_tokenize

file2=open("murder.txt").read()
sentences=sent_tokenize(file2)
text=' '.join(sentences)
file3=open("murder2.txt","w")
file3.write(text)
file3.close()
