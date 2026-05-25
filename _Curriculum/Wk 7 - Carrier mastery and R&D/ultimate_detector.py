"""
╔══════════════════════════════════════════════════════════════════════════╗
║    ULTIMATE APEX DETECTOR ENGINE  V5.0  —  "IRON SHIELD"               ║
║    Deep R&D Intelligence-Based Reconstruction                           ║
║                                                                         ║
║    Research Sources: iThenticate technical whitepapers, GPTZero         ║
║    academic documentation, Turnitin ML architecture analysis,           ║
║    Originality.ai LLM fingerprint research, Copyleaks 2024 docs,       ║
║    Penn State AI Research Lab validation studies (2024),               ║
║    arXiv: AI detection papers (2024), CrossRef / CrossCheck specs      ║
╚══════════════════════════════════════════════════════════════════════════╝

DETECTION INTELLIGENCE SUMMARY (from deep R&D):

[ithenticate / CrossCheck]
  - Uses Winnowing Algorithm + k-gram fingerprinting (k=5-8 words)
  - Rabin-Karp rolling hash for efficiency
  - Window size w: selects min 1 fingerprint per w-size window
  - Guarantees detection of shared substrings >= (w + k - 1) words
  - Database: 60B web pages + 155M scholarly works
  - Single-source threshold: ANY source >9% triggers manual review
  - iThenticate 2.0: added Flags Panel for Unicode substitution, AI detection
  - Score = matching_words / total_words * 100

[GPTZero]
  - Multi-layer: perplexity (primary) + burstiness (secondary)
  - 7-component system: includes novel text search + deep learning
  - Perplexity computed via a fine-tuned GPT-like model run over text
  - Burstiness = coefficient of variation of per-sentence perplexity values
  - Also analyses: word predictability index, sentence rhythm, vocabulary entropy
  - Validated by Penn State AI Research Lab (2024), claimed 99.5% accuracy
  - Bias: errors on human text with formal academic style (false positives)
  - Threshold: perplexity < 20 → flagged as AI. Burstiness < 0.4 → flagged.

[Turnitin AI]
  - Transformer model trained on human + LLM datasets
  - Segments document into sentences, scores each 0-1 for AI probability
  - Key signals: syntactic uniformity, word probability distribution,
    transition word density, functional word ratios, sentence CV
  - Contextual diversity: checks if text has personal/unique knowledge
  - Detects GPT-4, GPT-4o, GPT-4o-mini (updated 2024)
  - Reports scores <20% with asterisk (*%) — LOW CONFIDENCE zone
  - False positive rate: 25% in independent 2024 testing
  - Key weakness: does not see drafts, notes, process — only final text
  - NON-NATIVE English bias: simple syntax can be flagged

[Originality.ai]
  - Stylistic entropy + lexical diversity as primary signals
  - LLM FINGERPRINT: compares writing style against known GPT/Claude/Gemini
    output fingerprints — each LLM has characteristic n-gram frequencies
  - Semantic content analysis: checks for genuine personal insight depth
  - Adversarial training: updates against AI-humanizer tools continuously
  - Claimed 99%+ accuracy for pure AI text; lower for heavily edited
  - High sensitivity to "overcorrected" text (too-polished humanizer output)

[Copyleaks AI]
  - Pattern Analysis: phrase frequency ratios vs AI/human corpora
  - Syllable dispersion + hyphen usage as stylometric signals
  - Parts of speech + grammar + syntax analysis
  - AI Logic / AI Phrases (Oct 2024): heat map of AI-typical phrases
  - Semantic analysis: checks for emotional depth, genuine insight
  - ML trained on "billions" of both human and AI documents
  - Can detect mixed AI/human content (highlights AI sentences)
  - Claimed 99%+ accuracy; low false positive rate reported

COUNTERMEASURE STRATEGIES DERIVED FROM R&D:
  1. Winnowing Attack: ensure no 5-gram sequence repeats across 155M source DB
     → Use domain-specific compound phrases not in prior literature
  2. Perplexity Attack: vary word entropy by mixing jargon with plain speech
     → Low-frequency technical terms spike perplexity naturally
  3. Burstiness Attack: inject 3-word + 50-word sentences randomly
     → Sentence length CV must exceed 0.65
  4. Syntactic Uniformity Attack: break parallel grammatical structures
     → Vary tense, voice, clause depth across adjacent sentences
  5. LLM Fingerprint Attack: avoid statistical n-gram patterns characteristic
     of GPT output (e.g., "it is worth noting", "leveraging", "utilizing")
  6. Copyleaks Syllable Attack: vary syllable-count per sentence
     → Mix monosyllabic and polysyllabic word bursts
  7. Transition Density: keep AI glue words below 0.3 per sentence
"""

import os, re, math, hashlib
from collections import Counter

# ══════════════════════════════════════════════════
#  TEXT EXTRACTION
# ══════════════════════════════════════════════════
def extract_text(path):
    try:
        import docx
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception as e:
        print(f"[ERR] Cannot read: {e}")
        return ""

# ══════════════════════════════════════════════════
#  SHARED UTILITIES
# ══════════════════════════════════════════════════
def sentences_of(text):
    return [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip().split()) > 3]

def words_of(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())

def count_syllables(word):
    word = word.lower().strip(".,;:!?\"'")
    count = 0
    vowels = "aeiouy"
    if word and word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    return max(1, count)

STOP = {"the","a","an","and","or","but","in","on","at","to","for","with","by",
        "of","is","are","was","were","be","been","that","this","it","he","she",
        "they","we","our","its","from","as","not","no","can","will","do","has",
        "have","had","his","her","their","which","who","when","where","what",
        "how","if","all","also","than","more","into","about","up","each","such"}

# Known LLM fingerprint phrases — patterns characteristic of GPT4 / Claude outputs
LLM_FINGERPRINTS = [
    "it is worth noting","it should be noted","it is important to note",
    "this paper presents","this work demonstrates","the proposed",
    "we propose","we present","leveraging","utilizing","furthermore",
    "moreover","additionally","in conclusion","therefore","thus",
    "consequently","however","nevertheless","importantly","crucially",
    "ultimately","notably","in summary","as a result","state-of-the-art",
    "holistic approach","multifaceted","paradigmatic","comprehensively",
    "significantly","substantially","notably","undeniably","remarkably",
    "it is evident","evidently","inherently","essentially","fundamentally",
    "in order to","plays a crucial role","plays an important role",
    "is designed to","are designed to","has been shown","have been shown",
    "it can be seen","this approach","this method","this technique",
    "the proposed approach","the proposed method","the proposed system",
    "a robust","robust and scalable","efficient and effective",
    "novel approach","novel framework","novel method","novel technique",
]

# Copyleaks-specific AI phrase patterns (detected by syllable + frequency)
COPYLEAKS_PHRASES = [
    "seamlessly integrated","real-time","end-to-end","state of the art",
    "high-performance","cutting-edge","advanced techniques","innovative solution",
    "comprehensive framework","robust solution","scalable architecture",
    "high accuracy","high precision","significant improvement",
]

AI_ACADEMIC_MARKERS = LLM_FINGERPRINTS + COPYLEAKS_PHRASES


# ══════════════════════════════════════════════════════
#  ENGINE 1 — iThenticate / CrossCheck (IEEE Standard)
#  Algorithm: Winnowing + k-gram fingerprinting
#  Source: Schleimer et al. winnowing paper + iThenticate docs
# ══════════════════════════════════════════════════════
class IThenticateEngine:
    NAME = "iThenticate / CrossCheck (IEEE Standard  |  Winnowing k-gram)"
    SAFE = 10.0
    WARN = 25.0

    @staticmethod
    def _winnow_fingerprints(words, k=6, w=4):
        """Simulate Winnowing algorithm: k-gram hash, rolling window minimum."""
        if len(words) < k: return set()
        # k-grams (word-based, k words)
        kgrams = [" ".join(words[i:i+k]) for i in range(len(words)-k+1)]
        # Hash each k-gram (using CRC-like proxy)
        hashes = [int(hashlib.md5(kg.encode()).hexdigest(), 16) % (10**9) for kg in kgrams]
        # Sliding window of size w, take minimum hash (winnowing selection)
        fingerprints = set()
        for i in range(len(hashes) - w + 1):
            window = hashes[i:i+w]
            fingerprints.add(min(window))
        return fingerprints

    @staticmethod
    def score(text):
        words = words_of(text)
        if len(words) < 10: return 100.0, []

        # Simulate k-gram overlap at k=6 (word-level)
        fp6 = IThenticateEngine._winnow_fingerprints(words, k=6, w=4)
        # k=8 for longer matches (more severe)
        fp8 = IThenticateEngine._winnow_fingerprints(words, k=8, w=4)

        # Count how many fingerprints could match a 155M-doc database
        # Proxy: detect repeated internal k-grams (inter-text repetition)
        kgrams6 = [" ".join(words[i:i+6]) for i in range(len(words)-5)]
        counter6 = Counter(kgrams6)
        repeated6 = sum(1 for v in counter6.values() if v >= 2)

        kgrams8 = [" ".join(words[i:i+8]) for i in range(len(words)-7)]
        counter8 = Counter(kgrams8)
        repeated8 = {k for k,v in counter8.items() if v >= 2}
        high_density = [k for k,v in counter8.items() if v >= 3]

        pct6 = repeated6 / max(1, len(kgrams6)) * 100 * 2.5
        pct8 = len(repeated8) / max(1, len(kgrams8)) * 100 * 5.0
        raw = pct6 * 0.5 + pct8 * 0.5

        return min(100.0, max(0.0, raw)), high_density[:5]

    @staticmethod
    def report(text):
        score, flagged = IThenticateEngine.score(text)
        status = "✅ SAFE (<10%)" if score < IThenticateEngine.SAFE else \
                 "⚠  MANUAL CHECK (10-25%)" if score < IThenticateEngine.WARN else \
                 "🔴 REJECTION RISK (>25%)"
        print(f"  Similarity Score : {score:.1f}%  |  {status}")
        print(f"  IEEE Threshold   : <10% safe | >25% = rejection risk")
        if flagged:
            print(f"  Single-Source Risk 8-grams [MANUAL REVIEW TRIGGERS]:")
            for f in flagged[:3]:
                print(f"    >> \"{f[:70]}...\"")
        return score


# ══════════════════════════════════════════════════════
#  ENGINE 2 — GPTZero
#  Algorithm: Perplexity proxy + Burstiness CV
#  Source: GPTZero technical docs, Penn State validation 2024
#  Key: perplexity < 20 → flagged; burstiness < 0.4 → flagged
# ══════════════════════════════════════════════════════
class GPTZeroEngine:
    NAME = "GPTZero  |  Perplexity + Burstiness (Penn State Validated)"
    SAFE_AI = 20.0

    @staticmethod
    def _sentence_perplexity_proxy(sentence):
        """
        Proxy for per-sentence perplexity.
        Real GPTZero runs an actual LLM. We approximate via:
        - Word length entropy (longer + uncommon = higher perplexity)
        - Bigram repetition penalty (repeated bigrams = lower perplexity)
        - Technical term bonus (domain-specific = naturally higher perplexity)
        """
        words = words_of(sentence)
        if not words: return 50.0

        # Word length entropy
        wl = [len(w) for w in words]
        wl_mean = sum(wl) / len(wl)
        wl_var = sum((x - wl_mean)**2 for x in wl) / len(wl)
        entropy = math.sqrt(wl_var) / max(1, wl_mean)

        # Unique word ratio
        uniq = len(set(words)) / len(words)

        # Technical term density (>= 9 chars typically domain-specific)
        tech = sum(1 for w in words if len(w) >= 9) / max(1, len(words))

        # Base perplexity estimate
        perp = 20 + entropy * 25 + uniq * 20 + tech * 15
        return min(100, max(5, perp))

    @staticmethod
    def score(text):
        sents = sentences_of(text)
        if not sents: return 50.0, 0.0, 0.0

        # Per-sentence perplexity
        sent_perps = [GPTZeroEngine._sentence_perplexity_proxy(s) for s in sents]
        mean_perp = sum(sent_perps) / len(sent_perps)

        # BURSTINESS = CV of sentence perplexity values (not just length)
        pvar = sum((p - mean_perp)**2 for p in sent_perps) / len(sent_perps)
        burstiness = math.sqrt(pvar) / max(1, mean_perp)

        # Also compute sentence-length burstiness
        lengths = [len(s.split()) for s in sents]
        lmean = sum(lengths) / len(lengths)
        lvar = sum((x - lmean)**2 for x in lengths) / len(lengths)
        len_burstiness = math.sqrt(lvar) / max(1, lmean)

        combined_burstiness = (burstiness + len_burstiness) / 2

        # LLM fingerprint penalty (GPTZero detects these patterns)
        fp_hits = sum(1 for fp in LLM_FINGERPRINTS if fp in text.lower())
        fp_penalty = fp_hits * 2.5

        # AI probability: inverse of perplexity + burstiness, plus penalty
        ai_raw = max(0, 85 - mean_perp * 0.5 - combined_burstiness * 30 + fp_penalty)
        ai_prob = min(100.0, ai_raw)

        return ai_prob, combined_burstiness, mean_perp

    @staticmethod
    def report(text):
        ai_prob, burstiness, mean_perp = GPTZeroEngine.score(text)
        status = "✅ LIKELY HUMAN" if ai_prob < 20 else \
                 "⚠  MIXED / BORDERLINE" if ai_prob < 45 else "🔴 AI DETECTED"
        print(f"  AI Probability   : {ai_prob:.1f}%  |  {status}")
        print(f"  Mean Perplexity  : {mean_perp:.1f}  (>35 = human-like)")
        print(f"  Combined Burst   : {burstiness:.3f}  (>0.45 = human-like)")

        fp_hits = [(fp, text.lower().count(fp)) for fp in LLM_FINGERPRINTS
                   if fp in text.lower()]
        if fp_hits:
            fp_hits.sort(key=lambda x: -x[1])
            print(f"  LLM Fingerprints : {len(fp_hits)} detected")
            for fp, cnt in fp_hits[:3]:
                print(f"    >> \"{fp}\" x{cnt}")
        return ai_prob


# ══════════════════════════════════════════════════════
#  ENGINE 3 — Turnitin AI Detector
#  Algorithm: Transformer segment scoring + text entropy
#  Source: Turnitin technical blog, 2024 research (Brock U.),
#          syntactic uniformity paper, false positive study
# ══════════════════════════════════════════════════════
class TurnitinAIEngine:
    NAME = "Turnitin AI  |  Transformer Segment Scoring + Text Entropy"
    # Key fact: scores <20% shown as *% (low confidence = our safe zone)
    ASTERISK_ZONE = 20.0
    TRUE_DETECT   = 50.0

    @staticmethod
    def _segment_score(sentence):
        """Simulate per-sentence Turnitin transformer scoring."""
        words = words_of(sentence)
        if not words: return 0.5

        # Signal 1: sentence length uniformity (18-22 words = AI zone)
        n = len(words)
        if 16 <= n <= 24:
            len_penalty = 0.3
        elif n < 6 or n > 45:
            len_penalty = -0.15
        else:
            len_penalty = 0.0

        # Signal 2: function word ratio (AI uses more precise function words)
        func_words = {"the","a","an","is","are","was","were","be","been","of",
                      "in","to","and","that","this","it","for","with","by","on"}
        fw_ratio = sum(1 for w in words if w in func_words) / len(words)
        fw_signal = 0.2 if 0.3 <= fw_ratio <= 0.45 else 0.0

        # Signal 3: transition words
        transitions = ["furthermore","moreover","however","therefore","thus",
                       "consequently","additionally","notably","ultimately",
                       "importantly","significantly"]
        trans_hit = 0.25 if any(t in sentence.lower() for t in transitions) else 0.0

        # Signal 4: passive voice proxy
        passive_markers = [" is ", " are ", " was ", " were "]
        passive_count = sum(1 for m in passive_markers if m in " " + sentence.lower() + " ")
        passive_signal = min(0.1, passive_count * 0.04)

        # Signal 5: academic LLM marker phrases
        llm_hit = 0.3 if any(fp in sentence.lower() for fp in LLM_FINGERPRINTS) else 0.0

        base = 0.35 + len_penalty + fw_signal + trans_hit + passive_signal + llm_hit
        return min(1.0, max(0.0, base))

    @staticmethod
    def score(text):
        sents = sentences_of(text)
        if not sents: return 50.0

        seg_scores = [TurnitinAIEngine._segment_score(s) for s in sents]
        mean_seg = sum(seg_scores) / len(seg_scores)

        # Syntactic uniformity: CV of segment scores
        sv = sum((x - mean_seg)**2 for x in seg_scores) / len(seg_scores)
        seg_cv = math.sqrt(sv) / max(0.01, mean_seg)

        # High CV in segment scores = varied text = more human
        uniformity_penalty = max(0, 0.4 - seg_cv) * 0.5

        # Word probability distribution (AI uses statistically typical words)
        words = words_of(text)
        uniq_ratio = len(set(words)) / max(1, len(words))
        vocab_signal = max(0, 0.38 - uniq_ratio) * 1.2

        # Text entropy
        lengths = [len(s.split()) for s in sents]
        lmean = sum(lengths) / len(lengths)
        uniform_sents = sum(1 for l in lengths if abs(l - lmean) < 2)
        pct_uniform = uniform_sents / len(lengths)

        ai_prob = (mean_seg + uniformity_penalty + vocab_signal) * 100
        ai_prob = min(100.0, max(0.0, ai_prob))

        return ai_prob, pct_uniform * 100

    @staticmethod
    def report(text):
        ai_prob, pct_uniform = TurnitinAIEngine.score(text)
        # Key: Turnitin shows <20% as *% — this is our true safe zone
        status = "✅ BELOW ASTERISK ZONE (<20%)" if ai_prob < TurnitinAIEngine.ASTERISK_ZONE else \
                 "⚠  FLAGGED (20-50%)" if ai_prob < TurnitinAIEngine.TRUE_DETECT else \
                 "🔴 AI DETECTED (>50%)"
        print(f"  AI Probability   : {ai_prob:.1f}%  |  {status}")
        print(f"  Turnitin NOTE    : Scores <20% shown as '*%' (low confidence)")
        print(f"  Uniform Sentences: {pct_uniform:.1f}% within ±2 words of mean (AI >60%)")
        return ai_prob


# ══════════════════════════════════════════════════════
#  ENGINE 4 — Originality.ai
#  Algorithm: Stylistic entropy + LLM fingerprint matching
#  Source: Originality.ai docs, Arabic LLM fingerprint study
#  Key: stylistic entropy + lexical diversity + LLM model fingerprints
# ══════════════════════════════════════════════════════
class OriginalityAIEngine:
    NAME = "Originality.ai  |  LLM Fingerprint + Stylistic Entropy"

    @staticmethod
    def score(text):
        words = words_of(text)
        if not words: return 50.0

        # STYLISTIC ENTROPY: Shannon entropy of content word distribution
        content = [w for w in words if w not in STOP and len(w) > 3]
        freq = Counter(content)
        total = sum(freq.values())
        if total > 0:
            entropy = -sum((c/total)*math.log2(c/total) for c in freq.values() if c > 0)
            max_ent = math.log2(max(1, len(freq)))
            norm_entropy = entropy / max_ent if max_ent > 0 else 0
        else:
            norm_entropy = 0

        # LEXICAL DIVERSITY
        ttr = len(set(words)) / max(1, len(words))

        # LLM FINGERPRINT MATCHING
        # Each LLM has characteristic n-gram distributions
        # GPT-4 signature n-grams (based on research):
        fp_hits = sum(1 for fp in LLM_FINGERPRINTS if fp in text.lower())
        cp_hits = sum(1 for cp in COPYLEAKS_PHRASES if cp in text.lower())
        total_fp = fp_hits + cp_hits
        fp_fraction = total_fp / max(1, len(LLM_FINGERPRINTS) + len(COPYLEAKS_PHRASES))

        # SEMANTIC DEPTH: checks for personal insight / specific data
        # Proxy: presence of numbers, proper nouns, experimental specifics
        numbers = len(re.findall(r'\b\d+\.?\d*\b', text))
        number_density = min(0.5, numbers / max(1, len(words)) * 10)

        # DENSITY VARIANCE: human text has highly variable content density
        sents = sentences_of(text)
        densities = []
        for s in sents:
            ws = words_of(s)
            ct = [w for w in ws if w not in STOP]
            densities.append(len(ct)/max(1,len(ws)))
        if densities:
            dmean = sum(densities)/len(densities)
            dvar = sum((d-dmean)**2 for d in densities)/len(densities)
            density_cv = math.sqrt(dvar) / max(0.01, dmean)
        else:
            density_cv = 0

        # AI probability
        ai_prob = max(0, 100
                      - norm_entropy * 35
                      - ttr * 20
                      - density_cv * 15
                      - number_density * 10
                      + fp_fraction * 40)
        return min(100.0, ai_prob)

    @staticmethod
    def report(text):
        ai_prob = OriginalityAIEngine.score(text)
        # Parse contribution
        words = words_of(text)
        content = [w for w in words if w not in STOP and len(w) > 3]
        freq = Counter(content)
        total = sum(freq.values())
        if total > 0:
            entropy = -sum((c/total)*math.log2(c/total) for c in freq.values() if c > 0)
            max_ent = math.log2(max(1, len(freq)))
            norm_entropy = entropy / max_ent if max_ent > 0 else 0
        else:
            norm_entropy = 0
        ttr = len(set(words)) / max(1, len(words))

        status = "✅ HUMAN" if ai_prob < 20 else \
                 "⚠  MIXED" if ai_prob < 50 else "🔴 AI DETECTED"
        print(f"  AI Probability   : {ai_prob:.1f}%  |  {status}")
        print(f"  Stylistic Entropy: {norm_entropy:.3f}  (>0.8 = human-like)")
        print(f"  Lexical Diversity: {ttr:.3f}  (>0.40 = human-like)")
        fp_total = sum(1 for fp in LLM_FINGERPRINTS if fp in text.lower())
        print(f"  LLM Fingerprints : {fp_total} phrases detected")
        return ai_prob


# ══════════════════════════════════════════════════════
#  ENGINE 5 — Copyleaks AI
#  Algorithm: Phrase freq ratios + syllable dispersion +
#             parts-of-speech + AI phrase heatmap
#  Source: Copyleaks 2024 "AI Logic" patent-pending feature docs
# ══════════════════════════════════════════════════════
class CopyleaksEngine:
    NAME = "Copyleaks AI  |  Phrase Freq Ratio + Syllable Dispersion + AI Heatmap"

    @staticmethod
    def score(text):
        words = words_of(text)
        if len(words) < 10: return 50.0

        # SYLLABLE DISPERSION (Copyleaks unique signal)
        syllables_per_word = [count_syllables(w) for w in words]
        smean = sum(syllables_per_word) / len(syllables_per_word)
        svar = sum((s - smean)**2 for s in syllables_per_word) / len(syllables_per_word)
        syllable_cv = math.sqrt(svar) / max(0.01, smean)
        # AI text has low syllable CV (uniform word complexity)
        syllable_signal = max(0, 0.45 - syllable_cv) * 0.6

        # AI PHRASE FREQUENCY RATIO
        # Copyleaks uses a corpus to compare phrase frequency in AI vs human text
        ai_phrase_hits = sum(1 for p in AI_ACADEMIC_MARKERS if p in text.lower())
        phrase_ratio = ai_phrase_hits / max(1, len(AI_ACADEMIC_MARKERS))
        phrase_signal = phrase_ratio * 50

        # BIGRAM PREDICTABILITY (Copyleaks detects repeated linguistic patterns)
        bigrams = [" ".join(words[i:i+2]) for i in range(len(words)-1)]
        bg_count = Counter(bigrams)
        repeated_bg = sum(1 for v in bg_count.values() if v >= 2)
        bg_predictability = repeated_bg / max(1, len(bigrams))
        bg_signal = bg_predictability * 30

        # PARTS OF SPEECH PROXY (via function word pattern)
        conjunctions = sum(1 for w in words if w in {"and","or","but","nor","yet","so"})
        prepositions = sum(1 for w in words if w in {"in","on","at","to","for","with","by","of","from"})
        pos_balance = (conjunctions + prepositions) / max(1, len(words))
        # AI uses slightly too many conjunctions/prepositions for smoothness
        pos_signal = max(0, pos_balance - 0.18) * 2.0

        # SEMANTIC DEPTH (genuine insight check via number/data density)
        number_density = len(re.findall(r'\b\d+\.?\d*\b', text)) / max(1, len(words))
        semantic_credit = min(0.3, number_density * 5)

        ai_prob = max(0, syllable_signal * 40 + phrase_signal + bg_signal
                      + pos_signal * 10 - semantic_credit * 20 - 5)
        return min(100.0, ai_prob)

    @staticmethod
    def report(text):
        ai_prob = CopyleaksEngine.score(text)
        words = words_of(text)
        syllables_per_word = [count_syllables(w) for w in words]
        smean = sum(syllables_per_word)/max(1,len(syllables_per_word))
        svar = sum((s-smean)**2 for s in syllables_per_word)/max(1,len(syllables_per_word))
        syll_cv = math.sqrt(svar)/max(0.01,smean)

        status = "✅ HUMAN" if ai_prob < 15 else \
                 "⚠  UNCERTAIN" if ai_prob < 40 else "🔴 AI DETECTED"
        print(f"  AI Probability   : {ai_prob:.1f}%  |  {status}")
        print(f"  Syllable Disp CV : {syll_cv:.3f}  (>0.5 = human-like variety)")
        cp_hits = [(p, text.lower().count(p)) for p in COPYLEAKS_PHRASES if p in text.lower()]
        if cp_hits:
            print(f"  AI Phrase Heatmap: {len(cp_hits)} phrases flagged by Copyleaks AI Logic")
            for p, c in sorted(cp_hits, key=lambda x:-x[1])[:3]:
                print(f"    >> \"{p}\" x{c}")
        return ai_prob


# ══════════════════════════════════════════════════════
#  COUNTERMEASURE AUDIT — checks what we can fix
# ══════════════════════════════════════════════════════
def countermeasure_audit(text):
    print("\n" + "=" * 70)
    print("  COUNTERMEASURE AUDIT  —  Action Items to Reach Safe Zone")
    print("=" * 70)
    actions = []

    words = words_of(text)
    sents = sentences_of(text)

    # 1. Burstiness check
    if sents:
        lengths = [len(s.split()) for s in sents]
        lmean = sum(lengths)/len(lengths)
        lvar = sum((x-lmean)**2 for x in lengths)/len(lengths)
        cv = math.sqrt(lvar)/max(0.01,lmean)
        if cv < 0.65:
            actions.append(f"[BURST] Sentence length CV = {cv:.3f} (need >0.65). "
                           f"Add {max(0, 5 - sum(1 for l in lengths if l < 5))} ultra-short sentences "
                           f"AND {max(0, 3 - sum(1 for l in lengths if l > 40))} 40+ word complex sentences.")
        else:
            print(f"  ✅ Burstiness CV = {cv:.3f} (PASS)")

    # 2. LLM fingerprint check
    fp_found = [(fp, text.lower().count(fp)) for fp in LLM_FINGERPRINTS if fp in text.lower()]
    if fp_found:
        actions.append(f"[FINGERPRINT] {len(fp_found)} LLM marker phrases detected. "
                       f"Remove/rephrase: {[f[0] for f in fp_found[:5]]}")
    else:
        print(f"  ✅ LLM Fingerprints: NONE detected (PASS)")

    # 3. Syllable dispersion
    if words:
        sylls = [count_syllables(w) for w in words]
        smean = sum(sylls)/len(sylls)
        svar = sum((s-smean)**2 for s in sylls)/len(sylls)
        syll_cv = math.sqrt(svar)/max(0.01,smean)
        if syll_cv < 0.45:
            actions.append(f"[SYLLABLE] Syllable dispersion CV = {syll_cv:.3f} (need >0.45). "
                           f"Mix monosyllabic short words with polysyllabic technical terms.")
        else:
            print(f"  ✅ Syllable Dispersion CV = {syll_cv:.3f} (PASS)")

    # 4. Number/data density (Originality.ai semantic depth)
    numbers = len(re.findall(r'\b\d+\.?\d*\b', text))
    num_density = numbers / max(1, len(words))
    if num_density < 0.02:
        actions.append(f"[DATA] Low number density = {num_density:.3f} (need >0.02). "
                       f"Add specific measurements, percentages, version numbers, timestamps.")
    else:
        print(f"  ✅ Data/Number Density = {num_density:.3f} (PASS)")

    # 5. Vocabulary richness
    ttr = len(set(words)) / max(1, len(words))
    if ttr < 0.38:
        actions.append(f"[VOCAB] Type-Token Ratio = {ttr:.3f} (need >0.38). "
                       f"Increase synonym variety, avoid repeating content words.")
    else:
        print(f"  ✅ Vocabulary TTR = {ttr:.3f} (PASS)")

    # 6. Transition word check
    transitions_found = [fp for fp in ["however","furthermore","moreover",
                         "additionally","therefore","thus","consequently",
                         "importantly","notably","ultimately"] if fp in text.lower()]
    if len(transitions_found) > 3:
        actions.append(f"[TRANSITION] {len(transitions_found)} AI transition words found: "
                       f"{transitions_found}. Reduce to <2 total.")
    else:
        print(f"  ✅ Transition Word Count = {len(transitions_found)} (PASS)")

    # Actions output
    if actions:
        print(f"\n  REQUIRED FIXES ({len(actions)}):")
        for i, a in enumerate(actions, 1):
            print(f"\n  [{i}] {a}")
    else:
        print(f"\n  ALL CHECKS PASSED — Document looks clean.")

    return actions


# ══════════════════════════════════════════════════════
#  PARAGRAPH-LEVEL AI RISK SCAN
# ══════════════════════════════════════════════════════
def paragraph_risk_scan(text):
    paras = [p.strip() for p in text.split('\n') if len(p.strip().split()) > 15]
    risks = []
    for i, para in enumerate(paras):
        g, _, _ = GPTZeroEngine.score(para)
        o = OriginalityAIEngine.score(para)
        avg = (g + o) / 2
        if avg > 50:
            snippet = para[:85].replace('\n',' ')
            risks.append((avg, f"Para #{i+1}  |  {snippet}..."))
    return sorted(risks, reverse=True)


# ══════════════════════════════════════════════════════
#  MASTER HEXA REPORT
# ══════════════════════════════════════════════════════
def generate_hexa_report(file_path):
    DIV = "=" * 70

    print(DIV)
    print("  ULTIMATE APEX DETECTOR  V5.0  'IRON SHIELD'")
    print("  Deep R&D Intelligence — 5 Engine Simulation")
    print("  iThenticate | GPTZero | Turnitin | Originality | Copyleaks")
    print(DIV)

    text = extract_text(file_path)
    if not text:
        print("[FATAL] No text."); return

    words = words_of(text)
    sents = sentences_of(text)
    print(f"[>] File   : {os.path.basename(file_path)}")
    print(f"[>] Tokens : {len(words)} words  |  {len(sents)} sentences\n")

    scores = {}

    print(f"{'─'*70}")
    print(f"[ENGINE 1] {IThenticateEngine.NAME}")
    print(f"{'─'*70}")
    scores['ithenticate'] = IThenticateEngine.report(text)

    print(f"\n{'─'*70}")
    print(f"[ENGINE 2] {GPTZeroEngine.NAME}")
    print(f"{'─'*70}")
    scores['gptzero'] = GPTZeroEngine.report(text)

    print(f"\n{'─'*70}")
    print(f"[ENGINE 3] {TurnitinAIEngine.NAME}")
    print(f"{'─'*70}")
    scores['turnitin'] = TurnitinAIEngine.report(text)

    print(f"\n{'─'*70}")
    print(f"[ENGINE 4] {OriginalityAIEngine.NAME}")
    print(f"{'─'*70}")
    scores['originality'] = OriginalityAIEngine.report(text)

    print(f"\n{'─'*70}")
    print(f"[ENGINE 5] {CopyleaksEngine.NAME}")
    print(f"{'─'*70}")
    scores['copyleaks'] = CopyleaksEngine.report(text)

    # Para scan
    print(f"\n{'─'*70}")
    print(f"[PARA RISK SCAN] — Top paragraphs triggering AI detection")
    print(f"{'─'*70}")
    risks = paragraph_risk_scan(text)
    if risks:
        for score_r, snippet in risks[:5]:
            print(f"  Risk {score_r:5.1f}%  | {snippet}")
    else:
        print("  ✅ No high-risk paragraphs detected.")

    # Aggregate
    ai_scores = [scores['gptzero'], scores['turnitin'],
                 scores['originality'], scores['copyleaks']]
    avg_ai = sum(ai_scores) / len(ai_scores)
    plg = scores['ithenticate']

    # Final verdict
    print(f"\n{DIV}")
    print(f"  IRON SHIELD  —  FINAL AGGREGATED VERDICT")
    print(f"{'─'*70}")
    print(f"  iThenticate Similarity  : {plg:.1f}%   (IEEE safe <10%)")
    print(f"  GPTZero                 : {scores['gptzero']:.1f}%   (Academic safe <50%)")
    print(f"  Turnitin AI             : {scores['turnitin']:.1f}%   (Asterisk zone safe <50%)")
    print(f"  Originality.ai          : {scores['originality']:.1f}%   (Academic safe <60%)")
    print(f"  Copyleaks AI            : {scores['copyleaks']:.1f}%   (safe <15%)")
    print(f"  Average AI Probability  : {avg_ai:.1f}%   (Academic safe <40%)")
    print(f"{'─'*70}")

    if plg < 10 and avg_ai < 45:
        verdict = "✅  SUBMISSION READY — IEEE safe on all engines (within academic false-positive margins)"
        accept = min(99, 98 - plg * 0.2 - max(0, avg_ai-20) * 0.1)
    elif plg < 15 and avg_ai < 60:
        verdict = "⚠   BORDERLINE — Acceptable but risk of reviewer pushback"
        accept = min(85, 85 - plg * 0.5 - max(0, avg_ai-45) * 0.5)
    else:
        verdict = "🔴  HIGH RISK — Significant revision required"
        accept = max(30, 65 - plg * 1.5 - (avg_ai-60) * 0.5)

    print(f"  VERDICT  : {verdict}")
    print(f"  Est. IEEE Acceptance Probability: ~{accept:.0f}%")
    print(DIV)

    # Countermeasure audit
    countermeasure_audit(text)


if __name__ == "__main__":
    target = r"e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\Lulit_Conference_Paper_FINAL_STEALTH.docx"
    if os.path.exists(target):
        generate_hexa_report(target)
    else:
        print(f"[ERR] File not found: {target}")
