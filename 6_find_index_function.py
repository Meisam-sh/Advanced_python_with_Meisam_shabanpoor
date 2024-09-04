def find_index_words(text):
    words = text.split()
    index_words = [word.strip(".,") for word in words if word[0].isupper() and word not in ['The', 'A', 'An']]
    
    if not index_words:
        print("None")
    else:
        for i, word in enumerate(words, start=1):
            if word.strip(".,") in index_words:
                print(f"{i}:{word.strip('.,')}")

# متن ورودی
text = input()

find_index_words(text)