import numpy as np
import pandas as pd
import nltk
from gensim.models import Word2Vec
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from gensim.utils import simple_preprocess
from tqdm import tqdm

# Load data
df = pd.read_csv('SMSSpamCollection.csv', sep='\t', names=['label', 'message'])

# Drop missing values
df.dropna(inplace=True)

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Set up stop words and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess the messages
corpus = []
for i in range(len(df)):
    text = re.sub('[^a-zA-Z]', ' ', df['message'][i])
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words]
    text = ' '.join(text)
    corpus.append(text)

print(corpus[:5])

# Tokenize sentences and preprocess text
words = []
for sent in corpus:
    sent_token = sent_tokenize(sent)
    for token in sent_token:
        words.append(simple_preprocess(token))

# Train Word2Vec model
model = Word2Vec(words)

print(model.wv.most_similar('good'))

# Function to compute the average Word2Vec vector for a document
def avg_word2vec(doc):
    vectors = [model.wv[word] for word in doc if word in model.wv.index_to_key]
    if len(vectors) > 0:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

# Compute the average Word2Vec vector for each document
X = []
filtered_corpus = []

for i in tqdm(range(len(corpus))):
    doc_words = simple_preprocess(corpus[i])
    avg_vector = avg_word2vec(doc_words)
    if not np.all(avg_vector == 0):  # Check if the document vector is not all zeros
        X.append(avg_vector)
        filtered_corpus.append(df['label'][i])

X_new = np.array(X)
y = pd.Series(filtered_corpus).map({'ham': 0, 'spam': 1})

X_pd = pd.DataFrame(X_new)

print(X_pd.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_pd, y, test_size=0.2, random_state=42)

print(X_train.head())


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

# Train a Random Forest model

rf = RandomForestClassifier()


from sklearn.model_selection import GridSearchCV

random_forest_grid = {
    'n_estimators': [100, 200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth': [10, 20, 30, 40, 50],
    'criterion': ['gini', 'entropy']
}

rf_gridsearch = GridSearchCV(RandomForestClassifier(), random_forest_grid, n_jobs=-1, verbose=3)

rf_gridsearch.fit(X_train, y_train)

print('Best parameters found:', rf_gridsearch.best_params_)

rf.set_params(**rf_gridsearch.best_params_)

rf.fit(X_train, y_train)

# Evaluate the model

y_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))


email = 'Congratulations! You have won a free ticket to the Bahamas. Send us your details to claim your prize.'

# Preprocess the email

email = re.sub('[^a-zA-Z]', ' ', email)
email = email.lower()
email = email.split()
email = [lemmatizer.lemmatize(word) for word in email if word not in stop_words]
email = ' '.join(email)

# Compute the average Word2Vec vector for the email

email_vector = avg_word2vec(simple_preprocess(email)).reshape(1, -1)

# Scale the email vector

email_vector = scaler.transform(email_vector)

# Predict the email

prediction = rf.predict(email_vector)

if prediction[0] == 0:
    print('The email is not spam.')
else:
    print('The email is spam.')