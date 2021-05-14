from PIL import Image
import pytesseract as pt
import nltk
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

stopWords = set(stopwords.words('turkish'))

image = Image.open("example_text.jpeg")
text = pt.image_to_string(image, lang='tur')
words = nltk.word_tokenize(text, "turkish")

wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for i in wordsFiltered:
    lemmatizer.lemmatize(i)
    lemmatized_words.append(i)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 5).generate(" ".join(lemmatized_words))

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
