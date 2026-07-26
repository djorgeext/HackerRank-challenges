import re

text_path = 'NLP/Easy/The-Trigram/the-trigram-testcases/input/input04.txt'

with open(text_path, 'r') as f:
    text = f.read()

phrases = [p.strip() for p in re.split(r"[,\.;:\!\?¿¡]+", text) if p.strip()]
trigrams = {}
for phrase in phrases:
    words = phrase.split(' ')
    words = [w.lower() for w in words]
    if len(words) >= 3:
        i = 0
        while i <= (len(words) - 3):
            trigram = " ".join(words[i:i+3])
            if trigram in trigrams:
                trigrams[trigram] += 1
            else:
                trigrams[trigram] = 1
            i += 1
    
    else:
        continue

highest_trigram = max(trigrams, key=trigrams.get)
print(highest_trigram)