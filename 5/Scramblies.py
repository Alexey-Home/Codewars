def scramble(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    def get_count_letter(s):
        d = {}
        for letter in alphabet:
            d[letter] = s.count(letter)
        return d

    d_s1 = get_count_letter(s1)
    d_s2 = get_count_letter(s2)

    for letter in alphabet:
        if d_s1[letter] < d_s2[letter]:
            return False
    return True
