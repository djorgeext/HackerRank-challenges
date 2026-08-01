from nltk.tokenize import wordpunct_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def text_similarity(text1, text2):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    X = vectorizer.fit_transform([text1, text2])

    return cosine_similarity(X[0], X[1])[0, 0]

text_path = 'NLP/Medium/Stitch-the-Torn-Wiki/stitch-the-torn-wiki-testcases/input/input00.txt'

with open(text_path, 'r') as f:
    text = f.read().splitlines()

separator_set = text.index("*****")

a_set = text[1:separator_set]
b_set = text[separator_set+1:]

matches = []
for paragraph_a in a_set:
    similarity = []
    for paragraph_b in b_set:
        similarity.append(text_similarity(paragraph_a, paragraph_b))
    idx = similarity.index(max(similarity)) + 1
    matches.append(idx)


print(matches)