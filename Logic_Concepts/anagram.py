def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    print(sorted(str1))
    print(sorted(str2))
    return sorted(str1) == sorted(str2)
print(is_anagram("Debit Card", "Bad Credit"))