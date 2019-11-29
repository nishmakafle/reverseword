def wordReverse(string):
    # Split the string into multiple word in list form
    list1 = string.split(' ')
    list1.reverse()           # Reverse the splited list
    list1 = ' '.join(list1)   # Join the list and make a sentence
    return list1			  # Return that list to the function wordReverse


# Asked the Sentence, and saved it into question
question = input('Please enter a sentence: ')
# Apply the wordReverse function and get the answer which is saved in answer variable
answer = wordReverse(question)
print(answer)  # Print the Answer
