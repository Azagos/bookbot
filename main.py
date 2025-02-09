def main(): 
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = character_count(file_contents)
        report(char_count,word_count)    

def count_words(text):
    words_list = text.split()
    num_of_words = len(words_list)
    return num_of_words

def character_count(text):
    characters = {}
    lowered_string = text.lower()
    for i in lowered_string:
        if i.isalpha():
            if i not in characters:
                characters[i] = 1
            else:
                characters[i] += 1                 
    return characters  
     

def report(char_count, word_count):    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    # First, create the list and sort it
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})
    
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    # Then print the sorted results
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

main()     