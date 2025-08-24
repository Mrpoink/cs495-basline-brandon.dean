def tokenizer (s, enum=None): 
    #s is defined as a sentence

    s_clean = s.replace(',', '')

    s_split = s_clean.split() #s_split turns sentence into array of words


    s_lower = [] 

    for word in s_split : s_lower.append(word.lower())  #s_lower turns all items in s_split into lowercase

    s_num = len(s_lower)    #s_num returns number of words

    if enum == True:    #You don't always need the enumerator

        s_enum = []

        for word in s_lower:

            letter_enum = []

            for letter in word: letter_enum.append(ord(letter)) #creating a list of letters to numbers

            word_to_num = 0

            if len(letter_enum) == 1: word_to_num = ord(word)   #If a word only has one letter such as a and i

            else:

                for num in letter_enum: word_to_num = word_to_num + num #Turning each word into a number

                word_to_num = word_to_num + letter_enum[0]  #ensuring each word is different


            s_enum.append(word_to_num)  

        return s_num, s_lower, s_enum   #if enum is needed
    
    else:
        
        return s_num, s_lower   #if enum is not needed

