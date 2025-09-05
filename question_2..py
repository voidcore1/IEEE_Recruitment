text = """Madam and her Dad went to the civic center. 
They saw a racecar and a level bridge. 
Later, Anna read a book."""

words = text.split()

palindromes = []

for word in words:
    clean_word = ''.join(ch for ch in word if ch.isalnum()).lower()
    if clean_word and clean_word == clean_word[::-1]:
        palindromes.append(word.strip(".,!?"))


print("Number of Palindromes:", len(palindromes))
print("Palindromes:", palindromes)
