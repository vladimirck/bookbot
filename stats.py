def word_counter( s: str) -> int:
    return len(s.split())

def character_counter( s: str)-> dict:
    char_stats = {}
    text = s.lower()
    for char in text:
        if char in char_stats.keys():
            char_stats[char] += 1
        else:
            char_stats[char] = 1
    
    return char_stats

def sort_on(val):
    return val["count"]

def convert_to_sorted_list(char_stats: dict) -> list:
    sorted_list = []
    for key in char_stats:
        sorted_list.append({"char": key, "count": char_stats[key]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
