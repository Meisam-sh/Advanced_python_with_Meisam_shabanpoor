from typing import OrderedDict  

dictionary = OrderedDict()  
n = int(input())  
for _ in range(n):  
    word_mean = list(input().split())  
    dictionary[word_mean[0]] = [word_mean[1].lower(), word_mean[2].lower(), word_mean[3].lower()]  

# Get the sentence  
Sentence = list(input().split())  
for i in range(len(Sentence)):  
    for key, value in dictionary.items():  
        if Sentence[i].lower() in value:  
            Sentence[i] = key  

# Print the corrected sentence  
print(" ".join(Sentence))