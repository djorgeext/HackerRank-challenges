from nltk.tokenize import wordpunct_tokenize

# text_path = 'NLP/Medium/Stitch-the-Torn-Wiki/stitch-the-torn-wiki-testcases/input/input00.txt'

# with open(text_path, 'r') as f:
#     text = f.read().splitlines()

# separator_set = text.index("*****")
# a_set = text[1:separator_set]
# b_set = text[separator_set+1:]

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def text_similarity(text1, text2):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    X = vectorizer.fit_transform([text1, text2])

    return cosine_similarity(X[0], X[1])[0, 0]

p1 = "Natural language processing is useful for text similarity."
p2 = "Text similarity can be measured using natural language methods."

print(text_similarity(p1, p2))