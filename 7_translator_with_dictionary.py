n = int(input())
dictionary = {}
for _ in range(n):
    word, english, french, german = input().split()
    dictionary[word] = (english, french, german)

sentence = input().split()

translated_sentence = []
for word in sentence:
    if word in dictionary:
        translated_word = dictionary[word]
        translated_sentence.append(translated_word)

final_translation = ' '.join([f"{word[0]} {word[1]} {word[2]}" for word in translated_sentence])
print(final_translation)