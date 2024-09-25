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
            print(count)
    
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

            print(res)

    # Function Calls
    count_characters()

main()
