
# Function that reverse the words of the sentence


def wordreverse(sentence):
    # Split word of string seperated  by space
    word_list = sentence.split(' ')
    # print("Step1", words)
    # Reverse List of words
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    reversed_word_list = word_list[-1::-1]
    # print("Step2", words)
    # Now Join words with space
    reversed_sentence = ' '.join(reversed_word_list)
    # print("Step3", new_words)
    # Return the Output to wordreverse Function
    return reversed_sentence


# Take the String form user and store it in string variable
sentence = input('Type the sentence to reverse: ')
# call the wordreverse function with string as an argument
reversed_string = wordreverse(sentence)
print(reversed_string)
