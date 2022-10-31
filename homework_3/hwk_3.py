from collections import Counter


def generate_phrase(characters, phrase):
    characters_count = Counter(characters.lower())
    phrase_letter_count = Counter(phrase.lower())
    result = characters_count & phrase_letter_count

    if phrase_letter_count == result:
        return True
    else:
        return False


letters = "aabbccdef"
word = "bad"
print(generate_phrase(letters, word))
