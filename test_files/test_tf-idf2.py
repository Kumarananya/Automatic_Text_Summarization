##from sklearn.feature_extraction.text import CountVectorizer
##from sklearn.feature_extraction.text import TfidfTransformer
##
##train_set = ("The sky is blue.", "The sun is bright.")
##test_set = ("The sun in the sky is bright.", "We can see the shining sun, the bright sun.")
##
##count_vectorizer = CountVectorizer()
##count_vectorizer.fit_transform(train_set)
##
##print("Vocabulary:", count_vectorizer.vocabulary_)
##
##freq_term_matrix = count_vectorizer.transform(test_set)
##print(freq_term_matrix.todense())
##
##tfidf = TfidfTransformer(norm="l2")
##tfidf.fit(freq_term_matrix)
##print ("IDF:", tfidf.idf_)
##
##tf_idf_matrix = tfidf.transform(freq_term_matrix)
##print(tf_idf_matrix.todense())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.", "We can see the shining sun,the bright sun.")


vect = CountVectorizer()
vect.fit(train_set)
#print(vect.get_feature_names())
train_dtm=vect.transform(train_set)
test_dtm=vect.transform(test_set)
##print(train_dtm.toarray())

tfidf = TfidfTransformer(norm="l2")
tfidf.fit(train_dtm)

print("IDF", tfidf.idf_)
