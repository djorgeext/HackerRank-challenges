import sys

def solve(text):
    counts = {}
    first_seen = {}
    order = 0

    for sentence in text.split('.'):
        words = sentence.strip().lower().split()
        for i in range(len(words) - 2):
            trigram = ' '.join(words[i:i+3])
            if trigram not in counts:
                counts[trigram] = 0
                first_seen[trigram] = order
                order += 1
            counts[trigram] += 1

    if not counts:
        return

    best = max(counts, key=lambda t: (counts[t], -first_seen[t]))
    print(best)

if __name__ == '__main__':
    solve(sys.stdin.read())