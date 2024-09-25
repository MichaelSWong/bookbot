def main():
    def print_words():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    
    def word_count():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            count = 0
            for word in words:
                count+=1
            return count
    
    def count_characters():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            chars = []
            char_set = set()
            res = {}
            for char in file_contents:
                chars.append(char.lower())

            for char in chars:
                if char.isalpha():
                    char_set.add(char)
            
            for char in char_set:
                res[char] = chars.count(char)

            print("Characters found: ", res)
            return res

    def print_report():
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count()} words found in the document")
        for key, value in count_characters().items():
            print(f"The '{key}' character was found {value} times")

            #print(f"The '{char}': was found {count_characters()[char]} times")
        print(f"--- End report of books/frankenstein.txt ---")

    # Function Calls
    count_characters()
    print_report()

main()
