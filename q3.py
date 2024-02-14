import sys
file_name = sys.argv[1]
def wordCount(t):
    """Read the file and return a dictionary of unique words as keys, and the lines number they appear as a value"""
    input_file = open(t, "r")
    file_contents = input_file.read()
    word_list = file_contents.split()
    line_number = 0
    unique_Words = set(word_list)

    dict_words = dict.fromkeys(unique_Words)

    """For every line in the file, create a set of unique words, and append the line number to the dictionary value if the word is found as a key"""
    with open(t) as file_words:
        for line in file_words:
            line = line.strip()
            list = line.split()
            unique = set(list)
            for word in unique:
                if word in dict_words:
                    if dict_words.get(word) == None:
                        dict_words.update({word:[line_number]})
                    else:
                        dict_words[word].append(line_number)
            line_number += 1
    return dict_words
print(wordCount(file_name))



