file_1_list = ['i', 'took', 'a', 'walk', 'around', 'the', 'world', 'to', 'ease', 'my', 'troubled', 'mind', 'i', 'left', 'my', 'body', 'lying', 'somewhere', 'in', 'the', 'sands', 'of', 'time', 'i', 'watched', 'the', 'world', 'float', 'to', 'the', 'dark', 'side', 'of', 'the', 'moon', 'i', 'feel', 'there', 'is', 'nothing', 'i', 'can', 'do', 'yeah', 'i', 'watched', 'the', 'world', 'float', 'to', 'the', 'dark', 'side', 'of', 'the', 'moon', 'after', 'all', 'i', 'knew', 'it', 'had', 'to', 'be', 'something', 'to', 'do', 'with', 'you', 'i', 'really', 'dont', 'mind', 'what', 'happens', 'now', 'and', 'then', 'as', 'long', 'as', 'youll', 'be', 'my', 'friend', 'at', 'the', 'end', 'if', 'i', 'go', 'crazy', 'then', 'will', 'you', 'still', 'call', 'me', 'superman', 'if', 'im', 'alive', 'and', 'well', 'will', 'you', 'be', 'there', 'holding', 'my', 'hand', 'ill', 'keep', 'you', 'by', 'my', 'side', 'with', 'my', 'superhuman', 'might', 'kryptonite']
file_2_list = ['i', 'took', 'care', 'if', 'i', 'walk', 'around', 'then', 'one', 'two', 'three', 'four', 'five', 'switch', 'crazy', 'go', 'i', 'if', 'care', 'dont', 'i', 'five', 'four', 'three', 'two', 'one', 'and', 'switch']

file_1_start = 0
file_1_counter = file_1_start
file_2_counter = 0
all_common_phrases = []
list_of_common_words = []
while file_1_start < len(file_1_list) - 4:
    while file_2_counter < len(file_2_list) - 4:
        if file_1_list[file_1_counter] == file_2_list[file_2_counter]:
            # add the word to a list, and compare the next word in each file, until they stop matching
            list_of_common_words.append(file_1_list[file_1_counter])
            file_1_counter += 1
            file_2_counter += 1
        else:
            # stay on the same word in the first file and go to the next word in the second file
            if len(list_of_common_words) >= 5:
                all_common_phrases.append(list_of_common_words)
            list_of_common_words = []
            file_2_counter += 1
            file_1_counter = file_1_start

    file_1_start += 1
    file_2_counter = 0

    print(all_common_phrases)