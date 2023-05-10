def count_word_frequencies(file_name):
    word_frequencies = {}

    # Step 1: Read the file
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # Step 2: Count the word occurrences
    words = text.split()
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Step 3: Display the word frequencies in descending order
    sorted_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    for word, frequency in sorted_frequencies:
        print(f"{word}: {frequency}")


# Usage example
file_name = 'metallica.txt'  # Replace with your file name
count_word_frequencies(file_name)
