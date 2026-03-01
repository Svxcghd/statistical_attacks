#!/usr/bin/env python3
"""
Simple Substitution Cipher Decrypter

Edit the variables below:
- CIPHERTEXT: your encrypted text
- KEY: your substitution mapping (cipher -> plain)
- WORDLIST: set of known words (add more as needed)
"""

# ========================
# 1. PUT YOUR CIPHERTEXT HERE
# ========================
CIPHERTEXT = "PUT YOUR CIPHERTEXT HERE"

# ========================
# 2. PUT YOUR SUBSTITUTION KEY HERE
# ========================
# Format: "cipher_letter=plain_letter,cipher_letter=plain_letter,..."
# Example: a=o, n=p, etc.
KEY = "PUT THE DECRYPT WORDS HERE IN THE FORMAT a=o,n=p,..."


# ========================
# 3. WORDLIST (known English words)
# ========================
WORDLIST = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see",
    "other", "than", "then", "now", "look", "only", "come", "its", "over",
    "think", "also", "back", "after", "use", "two", "how", "our", "work",
    "first", "well", "way", "even", "new", "want", "because", "any", "these",
    "give", "day", "most", "us", "hello", "world", "test", "word", "text",
    "message", "secret", "code", "cipher", "plain", "decode", "encrypt"
}


# ========================
# DECRYPTION FUNCTION
# ========================
def build_substitution(key_string):
    """Build dict from key string like"""
    sub = {}
    pairs = key_string.replace(" ", "").split(",")
    for pair in pairs:
        if "=" in pair:
            cipher, plain = pair.split("=")
            sub[cipher.lower()] = plain.lower()
            sub[cipher.upper()] = plain.upper()
    return sub


def decrypt_word(word, sub):
    """Decrypt a single word using substitution"""
    result = []
    for ch in word:
        if ch.isalpha():
            result.append(sub.get(ch, ch))
        else:
            result.append(ch)
    return "".join(result)


def process_text(text, sub, wordlist):
    """Decrypt text and uppercase unknown words"""
    import re
    
    tokens = re.findall(r"[\w]+|[^\w\s]|\s+", text)
    output = []
    
    for token in tokens:
        if token.isalpha():
            decrypted = decrypt_word(token, sub)
            if decrypted.lower() in wordlist:
                output.append(decrypted)
            else:
                output.append(decrypted.upper())
        else:
            output.append(token)
    
    return "".join(output)


# ========================
# RUN
# ========================
if __name__ == "__main__":
    # Build substitution dictionary
    substitution = build_substitution(KEY)
    
    # Decrypt
    result = process_text(CIPHERTEXT, substitution, WORDLIST)
    
    print("=" * 40)
    print("CIPHERTEXT:", CIPHERTEXT)
    print("KEY:", KEY)
    print("=" * 40)
    print("DECRYPTED:", result)
    print("=" * 40)