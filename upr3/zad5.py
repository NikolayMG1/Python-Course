def unique_chars_count(s):
    s = set(s)
    return len(s)

assert unique_chars_count("abcdef") == 6
assert unique_chars_count("aabbcc") == 3
assert unique_chars_count("abcabc") == 3
assert unique_chars_count("aaaaaa") == 1
assert unique_chars_count("") == 0
