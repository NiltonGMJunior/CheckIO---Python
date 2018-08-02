def findAll(text, subtext):

    index = text.find(subtext)
    output = []

    if index == -1:
        return - 1
    else:
        while index != -1:
            output.append(index)
            if(index <= len(text) - 1):
                index = text.find(subtext, index + 1)

    return output

def left_join(phrases):

    list_of_phrases = list(phrases)

    for i in range(0,len(list_of_phrases)):
        list_of_phrases[i] = list_of_phrases[i].replace('right', 'left')

    s = ','.join(list_of_phrases)
        
    return s

print(left_join(("left", "right", "left", "stop")))