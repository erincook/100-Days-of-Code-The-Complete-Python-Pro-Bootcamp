def check_plagiarism(file1, file2):
    file_1 = open(file1, "r")
    file_2 = open(file2, "r")
    file_1_string = file_1.read()
    file_2_string = file_2.read()
    file_1_list = file_1_string.split()
    file_2_list = file_2_string.split()

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

    if all_common_phrases == []:
        return False

    longest_length = 4
    longest_phrase = []
    for text in all_common_phrases:
        if len(text) > longest_length:
            longest_length = len(text)
            longest_phrase = text
    return " ".join(longest_phrase)


    file_1.close()
    file_2.close()

print(check_plagiarism("file1.txt", "file2.txt"))