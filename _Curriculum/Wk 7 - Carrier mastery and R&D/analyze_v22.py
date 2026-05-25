import sys
sys.path.insert(0, r'e:\Wk 7 - Carrier mastery and R&D')
from ultimate_detector import sentences_of, words_of, AI_GLUE
import docx, math

path = r'e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\Lulit_Conference_Paper_v23_CLEAN.docx'
doc = docx.Document(path)
text = '\n'.join(p.text for p in doc.paragraphs if p.text.strip())

sents = sentences_of(text)
lengths = [len(s.split()) for s in sents]
mean = sum(lengths)/len(lengths)
cv = math.sqrt(sum((x-mean)**2 for x in lengths)/len(lengths)) / mean

print(f"Total sentences: {len(sents)}")
print(f"Mean length: {mean:.1f} words")
print(f"CV (burstiness): {cv:.3f}  (need >0.6)")

buckets = {}
for l in lengths:
    b = (l//5)*5
    buckets[b] = buckets.get(b,0)+1
print()
for k in sorted(buckets):
    print(f"  {k:3d}-{k+4:3d} words: {buckets[k]:3d} sentences  {'#'*buckets[k]}")

glue_hits = [(g, text.lower().count(g)) for g in AI_GLUE if g in text.lower()]
print("\nAI glue phrases found:")
for g,cnt in sorted(glue_hits, key=lambda x: -x[1]):
    print(f'  "{g}" x{cnt}')
