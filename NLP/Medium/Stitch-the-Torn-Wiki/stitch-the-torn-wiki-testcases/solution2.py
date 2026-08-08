# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def find_best_match_char_ngrams(a_sample, paragraph_list):
    # analyzer='char' is the key here, capturing structural style rather than just topics
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5))
    
    # Fit and transform the sample and the list
    all_texts = [a_sample] + paragraph_list
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Calculate cosine similarity between a_sample (index 0) and the rest
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    best_match_idx = np.argmax(similarities)
    return best_match_idx, similarities[best_match_idx]


def main():
    lines = sys.stdin.read().splitlines()

    separator_idx = lines.index("*****")
    a_set = lines[1:separator_idx]
    b_set = lines[separator_idx + 1 :]

    for paragraph_a in a_set:
        best_idx, _ = find_best_match_char_ngrams(paragraph_a, b_set)
        best_idx += 1
        print(best_idx)


if __name__ == "__main__":
    main()
