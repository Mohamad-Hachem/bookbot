def counting_nwords_in_book(text:str):
    words = text.split()
    return f"Found {len(words)} total words"


def counting_char(text:str):
    char_count_dic = {}
    for char in text:
        char = char.lower()
        if char in char_count_dic.keys():
            char_count_dic[char] += 1
        else : 
            char_count_dic[char] = 1
    
    return char_count_dic

def sorting_dic(char_count:dict):
    return dict(sorted(char_count.items(),key=lambda item: item[1], reverse=True))

def print_sorted_dic(char_count:dict):
    for key, value in char_count.items():
        if key.isalpha() and key is not None:
            print(f"{key}: {value}")
        