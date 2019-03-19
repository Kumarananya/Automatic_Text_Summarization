from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

train_set = ["The the the sky is blue .","the sun  bright. "]
##, "The the the the the the  sun is bright."
##test_set = ("The sun in the sky is bright.", "We can see the shining sun,the bright sun.")
test_set = ["the sun  bright. "]
##token_pattern=r'\b\w+\b', min_df=1
vect = CountVectorizer()
vect.fit(train_set)

print(vect.get_feature_names())

train_dtm=vect.transform(train_set)
print(train_dtm.toarray())

    
##test_dtm=vect.transform(test_set)
##print(train_dtm.toarray())
##print(test_dtm.toarray())
##a=train_dtm.toarray()
##print(a[0])
##for i in a[0]:
##    print(i)
##print(a)
##print(type(a))

tfidf = TfidfTransformer()
tfidf.fit(train_dtm)
tfidf_train=tfidf.transform(train_dtm)
print(tfidf_train.toarray())

##tfidf_test=tfidf.transform(test_dtm)
##print("\n")
##print(tfidf_train.toarray())
##print(tfidf_test.toarray())

##print("IDF", tfidf.idf_)
