import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nltk
import re
from tqdm import tqdm


nltk.download('stopwords')
nltk.download('punkt')


df = pd.read_csv('Natural-Language-Processing/Algorithms/Word2Vec/all_kindle_review.csv')

df.head()

#reviewText and rating are the columns we are interested in

df = df[['reviewText', 'rating']]

df.isnull().sum()

df.drop_duplicates(inplace=True)

df["rating"].value_counts()

# df["rating"] = df["rating"].map({1:0, 2:0, 3:0, 4:1, 5:1})

df["rating"] = df["rating"].apply(lambda x: 1 if x > 3 else 0)

df["rating"].value_counts()

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

corpus = []


for i in range(len(df)):
    review = re.sub('[^a-zA-Z]', ' ', df['reviewText'][i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(nltk.corpus.stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

words = []


from nltk.tokenize import sent_tokenize
from gensim.utils import simple_preprocess

for sent in corpus:
    sent_tokenize_list = sent_tokenize(sent)
    for sentence in sent_tokenize_list:
        words.append(simple_preprocess(sentence))


# from gensim.models import Word2Vec

# model = Word2Vec(words)

# print(model.wv.most_similar('good'))


# def avg_word2vec(doc):
#     vectors = [model.wv[word] for word in doc if word in model.wv.index_to_key]
#     if len(vectors) > 0:
#         return np.mean(vectors, axis=0)
#     else:
#         return np.zeros(model.vector_size)

# # Compute the average Word2Vec vector for each document
# X = []
# y = []

# for i in tqdm(range(len(corpus))):
#     doc_words = simple_preprocess(corpus[i])
#     avg_vector = avg_word2vec(doc_words)
#     if not np.all(avg_vector == 0):  # Check if the document vector is not all zeros
#         X.append(avg_vector)
#         y.append(df['rating'][i])

# X_new = pd.DataFrame(np.array(X))
# y_new = pd.Series(y)


# print(X_new.head())
# print(y_new.head())

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(corpus).toarray()
y = df['rating']

X_new = pd.DataFrame(X)
y_new = pd.Series(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Naive Bayes classifier



from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

# nb.fit(X_train, y_train)

# from sklearn.model_selection import GridSearchCV

# multi_nb_params = {
#     'alpha': [0.1, 0.5, 1.0, 10.0]
# }

# multi_nb_grid = GridSearchCV(nb, multi_nb_params, cv=5, n_jobs=-1, verbose=2)

# multi_nb_grid.fit(X_train, y_train)

# print(multi_nb_grid.best_params_)

# nb.set_params(alpha=multi_nb_grid.best_params_['alpha'])

nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:', classification_report(y_test, y_pred))
print('Confusion Matrix:', confusion_matrix(y_test, y_pred))

# Plot the confusion matrix

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()