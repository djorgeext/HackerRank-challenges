# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def text_similarity(text1, text2):
    vectorizer = TfidfVectorizer(lowercase=True, stop_words="english")
    X = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(X[0], X[1])[0, 0]


def main():
    lines = sys.stdin.read().splitlines()

    separator_idx = lines.index("*****")
    a_set = lines[1:separator_idx]
    b_set = lines[separator_idx + 1 :]

    for paragraph_a in a_set:
        similarities = []
        for paragraph_b in b_set:
            similarities.append(text_similarity(paragraph_a, paragraph_b))

        best_idx = similarities.index(max(similarities)) + 1
        print(best_idx)


if __name__ == "__main__":
    main()