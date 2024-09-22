from googletrans import Translator  

sentence = input("Enter a sentence: ")  
translator = Translator()  

try:  
    translation = translator.translate(sentence, dest='de', src='en')  
    print(f"Translated text: {translation.text}")  
except Exception as e:  
    print(f"Error occurred: {e}")