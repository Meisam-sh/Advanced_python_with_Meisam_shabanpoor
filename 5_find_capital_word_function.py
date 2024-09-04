def find_capital_words(text):
    words = text.split()
    index = 1
    
    for word in words:
        cleaned_word = word.rstrip('.').rstrip(',')
        
        if cleaned_word[0].isupper() and cleaned_word not in ['The', 'This']:
            print(f"{index}:{cleaned_word}")
            index += 1
    
    if index == 1:
        print("None")

# گرفتن متن ورودی از کاربر
text = input()
find_capital_words(text)