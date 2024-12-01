
def sort_on(d):
    return d["num"] #returns value with this key 

def dict_list(dictionary):
    sorted_list = []
    for char in dictionary:
        sorted_list.append({"char":char, "num": dictionary[char]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list

def count_char(book):
    lowercase = book.lower()
    dictionary = {}
    for char in lowercase:
        if char.isalpha():
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] +=1
    return dictionary

def count_words(book):
    splitwords = book.split()
    count = len(splitwords)
    return count

def main():
    book_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counted_words = count_words(file_contents)
        counted_chars = count_char(file_contents)
        dict_lists = dict_list(counted_chars)
    
    print (f"--- Begin report of {book_path} ---")
    print (f"{counted_words} words found in the document")
    print ()

    for item in dict_lists:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character was found {item['num']} times")

    print("---End report---")



main()
