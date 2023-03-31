#taking into account the initial sentence given
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog.!"
#we create a new variable replacing the "!" for a space and print it calling it "fixed_sentence"
fixed_sentence = (sentence.replace("!" , " "))
print (fixed_sentence)
#in order to get the sentence in Upper case we apply the upper formula
print(fixed_sentence.upper())
#In order to print the sentence in reverse, we apply the "all characters with a -1 step"
print(fixed_sentence[::-1])