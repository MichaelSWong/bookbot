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
    print_words()
    word_count()

main()
