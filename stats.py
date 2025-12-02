def get_words_count(text):
    words = text.split()
    return f"Found {len(words)} total words"

def get_character_counts(text: str):
    lowered_text = text.lower()
    dict = {}
    for character in lowered_text:
        if character.isalpha():
            if character in dict:
                dict[character] = dict[character] + 1
            else:
                dict[character] = 1
    return dict

def get_two_keyed_dict_list(dict :dict):
    list = []
    for key,value in dict.items():
        each_dict = {}
        each_dict["char"] = key
        each_dict["num"] = value
        list.append(each_dict)
    return list

def sort_on(item):
    return item["num"]

def get_total_words(list :list):
    sum = 0
    for value in list:
        sum = sum + value["num"]
    return sum

def print_dict_list_contents(list: list):
    for value in list:
        print(f"{value['char']}: {value['num']}")


def print_report(formatted_dict_list):
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_total_words(formatted_dict_list)} total words
--------- Character Count -------""")
    print_dict_list_contents(formatted_dict_list)
    print("============= END ===============")
