import pickle

label_pickle=open("labels.pickle","rb")
labels=pickle.load(label_pickle)

print(len(labels))
