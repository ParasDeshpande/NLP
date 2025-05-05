# 📌 Import libraries
import pandas as pd
import re
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')

# -------------------------------------------
# 📚 Morphology Operations: Add/Delete
# -------------------------------------------

# ✨ Sample words
words = ["happy", "kind", "run", "move", "use"]

# ✨ Define affixes
prefixes = ["un", "re", "in"]
suffixes = ["ness", "ing", "ed"]

# 📌 Function to add affix
def add_affix(word, affix, affix_type):
    if affix_type == "prefix":
        return affix + word
    elif affix_type == "suffix":
        return word + affix

# 📌 Function to delete affix (only if present)
def delete_affix(word, affix, affix_type):
    if affix_type == "prefix" and word.startswith(affix):
        return word[len(affix):]
    elif affix_type == "suffix" and word.endswith(affix):
        return word[:-len(affix)]
    else:
        return word  # no affix found → return word as-is

# ---------------------------------------------------------
# 🗂️ Create Add/Delete Table (simulating morphology ops)
# ---------------------------------------------------------

rows = []

for word in words:
    # Apply all prefixes
    for pre in prefixes:
        new_word = add_affix(word, pre, "prefix")
        deleted_word = delete_affix(new_word, pre, "prefix")
        rows.append([word, "prefix", pre, new_word, deleted_word])
    
    # Apply all suffixes
    for suf in suffixes:
        new_word = add_affix(word, suf, "suffix")
        deleted_word = delete_affix(new_word, suf, "suffix")
        rows.append([word, "suffix", suf, new_word, deleted_word])

# 📊 Create DataFrame (Add/Delete Table)
morph_table = pd.DataFrame(rows, columns=["Root Word", "Affix Type", "Affix", "After Addition", "After Deletion"])
morph_table
