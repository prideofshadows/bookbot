import sys
from stats import get_num_words, count_characters, sort_on

def main():
  if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
  book_path = sys.argv[1]
  print("============ BOOKBOT ============")
  print(f"analyzing book found at {book_path}")
  num_words = get_num_words(book_path)
  char_counts = count_characters(book_path)
  sorted_char_counts = sort_on(char_counts)
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words.")
  print("--------- Character Count -------")
  for char in sorted_char_counts:
    if char['char'].isalpha():
      print(f"{char['char']}: {char['num']} ")
  print("============= END ===============")

main()
