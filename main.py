def main():
    with open("books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        
        file_contents = split_text(file_contents)
        print(len(file_contents))   
        return file_contents

def split_text(text):
    return text.split()


main()