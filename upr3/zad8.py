def find_shortest_and_longest_words(words, letter):
    words_with_letter = [word for word in words if word.startswith(letter)]

    if not words_with_letter:
        return None, None

    shortest_word = min(words_with_letter, key=len)
    longest_word = max(words_with_letter, key=len)

    return shortest_word, longest_word


assert find_shortest_and_longest_words(["abracadabra", "banana", "kugelschreiber", "ant", "almost", "thisshouldbeaverylongword"], "a") == ("ant", "abracadabra")
assert find_shortest_and_longest_words(["abracadabra", "banana", "kugelschreiber", "ant", "almost", "thisshouldbeaverylongword"], "b") == ("banana", "banana")

