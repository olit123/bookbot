path_to_file = "books/frankenstein.txt"

def main():
    print("--- Begin report of " + path_to_file + " ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"{count_words(file_contents)} words found in the document")
        character_counts = ordered_char_count(count_characters(file_contents))
    for (char, count) in character_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def count_words(string):
    return len(string.split())

def count_characters(string):
    counts = {}
    for char in clean_charset(set(string.lower())):
        count = count_char(char, string)
        counts[char] = count
    return counts

def count_char(char, string):
    count = 0
    for ch in string:
        if char == ch:
            count += 1
    return count

def clean_charset(charset):
    unwanted = ["1","2","3","4","5","6","7","8","9","0", " ", "[", "]", "/", "$", "£", "\n", "_", "#", "@", "%", "~"]
    for char in unwanted:
        charset.discard(char)
    return charset

def ordered_char_count(char_counts):
    return sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

main()