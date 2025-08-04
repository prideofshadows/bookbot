def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def get_num_words(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def count_characters(path):
    char_counts = {}
    text = get_book_text(path)
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(char_counts):
  char_list = []
  for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
  char_list.sort(reverse=True, key=lambda x: x["num"])
  return char_list            