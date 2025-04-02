from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

news = fetch_20newsgroups(subset='all')
print(len(news.data))
print(news.data[0])

x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)
cv = CountVectorizer()
x_train = cv.fit_transform(x_train)
x_test = cv.transform(x_test)

ml = MultinomialNB()
ml.fit(x_train, y_train)
y_predict = ml.predict(x_test)

print(f'The accuracy of Naive Bayes: {ml.score(x_test, y_test)}')
print(classification_report(y_test, y_predict, target_names=news.target_names))