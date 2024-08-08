import sys

def characterCounter(text):
    lowered_string = text.lower()
    char_dict = {}
    for char in lowered_string:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
                
    return char_dict

def wordCounter(text):
    return len(text.split())

def sort_on(dict):
    return dict["num"]

def main() -> int:
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()   
    total_words = wordCounter(file_contents) 
    char_dict = characterCounter(file_contents)
    
    # Convert character dictionary to a list of dictionaries
    char_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    
    # Sort the character list by frequency
    char_list.sort(reverse=True, key=sort_on)
    
    # Print the report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document\n")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


if __name__ == '__main__':
    sys.exit(main())