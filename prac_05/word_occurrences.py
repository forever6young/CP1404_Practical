def main():
    # Setup dict
    my_dict = {}

    text = input("Text: ")

    # Remove white space
    clean_text = " ".join(text.split())

    # Split data
    raw_data = clean_text.split()

    # Sort data
    raw_data.sort()

    for word in raw_data:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    # Find the longest word
    longest_word_len = max([len(key) for key in my_dict])

    # Print result
    for key, value in my_dict.items():
        print("{0:<{1}} : {2}".format(key, longest_word_len, value))


main()
