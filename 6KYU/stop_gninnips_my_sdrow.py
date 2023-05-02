def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


sentence = "Hey fellow ranger warriors"
print(spin_words(sentence))