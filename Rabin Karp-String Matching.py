def rabin_karp(text, pattern):
    d = 256           # Number of characters (ASCII)
    q = 101           # A prime number (modulus)

    n = len(text)
    m = len(pattern)

    p_hash = 0   
    t_hash = 0   
    h = 1

    # h = (d^(m-1)) % q
    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):

        # If hash match, check characters
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                return f"Pattern found at index {i}"
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return "Pattern not found"

text = "ABCCDDAEFG"
pattern = "CDD"
print(rabin_karp(text, pattern))
