import subprocess
import sys

# Automatically install numpy if it is missing
try:
    import numpy
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

def summarize_text(text: str) -> str:
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        
        summary_sentences = summarizer(parser.document, 3)
        result = " ".join([str(sentence) for sentence in summary_sentences])
        
        return result if result else "Could not generate summary."
        
    except Exception as e:
        return f"Local AI Error: {str(e)}"
