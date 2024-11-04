import re

QUOTES = re.compile(r'["”“]+')
GREEK_PUNCT = re.compile(r"[\\/':;,·!\?\._『@#\$%^&\*—]+")
CRITICAL_APPARATUS_CHARACTERS = re.compile(r"[⸀⸂⸃⟧⟦⸄⸁⸅]+")

def drop_grc_punct(text: str) -> str:
    """
    Drop all Greek punctuation, replacing the punctuation with a space.

    :param text: Text to clean
    :return: cleaned text

    """
    text = GREEK_PUNCT.sub("", text)
    text = QUOTES.sub("", text)
    return text

def drop_critical_apparatus_char(text: str) -> str:
    """
    Drop all critical appartus characters.

    :param text: Text to clean
    :return: cleaned text

    """
    text = CRITICAL_APPARATUS_CHARACTERS.sub("", text)
    return text