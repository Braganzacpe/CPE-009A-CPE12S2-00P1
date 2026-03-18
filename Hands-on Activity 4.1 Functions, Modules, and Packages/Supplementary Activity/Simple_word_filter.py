def word_filter(sentence, bad_words):
    words = sentence.split()
    filtered_words = []

    for word in words:
        if word.lower() in bad_words:
            filtered_words.append("*" * len(word))
        else:
            filtered_words.append(word)

    return " ".join(filtered_words)

sentence = "You are a bad poopoo head 67"
bad_words = ["bad","poopoo","67"]

print(word_filter(sentence, bad_words))