def count_word_occurrences(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count
def print_word_occurrences(word_count):
    for word, count in word_count.items():
        print(f'{word}: {count}')


file_path = input("Enter the path to the text file: ")
try:
    word_count = count_word_occurrences(file_path)
    print("Word occurrences in the file:")
    print_word_occurrences(word_count)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")
except Exception as e:
    print("An error occurred:", e)