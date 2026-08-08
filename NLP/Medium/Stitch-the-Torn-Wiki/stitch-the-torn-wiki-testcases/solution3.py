import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.optimize import linear_sum_assignment
sys.stdin = open('NLP/Medium/Stitch-the-Torn-Wiki/stitch-the-torn-wiki-testcases/input/input00.txt', 'r')

def main():
    raw = sys.stdin.read().split('\n')
    lines = [line.rstrip('\r') for line in raw]

    idx = 0
    while lines[idx].strip() == '':
        idx += 1
    n = int(lines[idx].strip())
    idx += 1

    set_a = []
    while len(set_a) < n:
        if lines[idx].strip() != '':
            set_a.append(lines[idx])
        idx += 1

    # skip forward to the ***** separator line
    while not (lines[idx].strip() != '' and set(lines[idx].strip()) == {'*'}):
        idx += 1
    idx += 1

    set_b = []
    while len(set_b) < n and idx < len(lines):
        if lines[idx].strip() != '':
            set_b.append(lines[idx])
        idx += 1

    # Vector space model: TF-IDF over word unigrams+bigrams
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), sublinear_tf=True)
    tfidf = vectorizer.fit_transform(set_a + set_b)
    sim = cosine_similarity(tfidf[:n], tfidf[n:])

    # Optimal one-to-one matching (Hungarian algorithm), not greedy argmax,
    # since every fragment in A pairs with exactly one distinct fragment in B.
    row_ind, col_ind = linear_sum_assignment(-sim)

    result = [0] * n
    for r, c in zip(row_ind, col_ind):
        result[r] = c + 1

    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()
