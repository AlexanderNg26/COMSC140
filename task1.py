forbidden = ["spam" , "ad" , "buy" ]
sentence = input("Enter a sentence: ")
sentence_adjusted = sentence.split()
clean_words = []

for word in sentence_adjusted: 
    if word in forbidden:
        new_word = len(word) * "*"
        clean_words.append(new_word)
    else:
        clean_words.append(word)

for words in clean_words: 
    print(words,end= ' ')