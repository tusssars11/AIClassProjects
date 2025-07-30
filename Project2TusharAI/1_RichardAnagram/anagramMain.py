from Anagram import *

"""
Main function for the program. The Anagram initialization takes input in the
following format:  
  1. A word or phrase (string)  
  2. A dictionary file (located in the current directory)  
  3. A list of words that **must** be included in the anagram  
  4. A list of words that **must not** be included in the anagram  
  5. The maximum number of words allowed in the anagram (0 = unlimited)  

Example:  
  Anagram("cat", "test.txt", ["act"], ["at"], 3)  
  - Finds all anagrams for "cat" using words from `test.txt`.  
  - Ensures that the word "act" **must** be included in the result.  
  - Ensures that the word "at" **must not** appear in any anagram.  
  - Limits each anagram to **at most 3 words**.  
"""

def main():
	"""
	Main function: Handles user input and runs the anagram finder.
	"""
	DICTIONARY = "test.txt"  # Set the dictionary file to use (test.txt in this case)

	# Prompt the user to enter a word or phrase for which to find anagrams
	inputstring = input("Enter a word or phrase to find anagrams: ").strip()  

	# Ask the user if they want to enable advanced options (true/false)
	advanced_options = input("Enable advanced options? (true/false): ").strip().lower()  

	# If the user chooses advanced options, prompt for additional inputs
	if advanced_options == "true":
		# Ask for words that must be included in the anagram (comma-separated)
		include_words = input("Enter words to include (comma-separated): ").strip()

		# Ask for words that must be excluded from the anagram (comma-separated)
		exclude_words = input("Enter words to exclude (comma-separated): ").strip()

		# Ask for the maximum number of words allowed in each anagram (leave blank for unlimited)
		max_length = input("Enter max words per anagram (leave blank for unlimited): ").strip()

		# Convert the comma-separated words into a list, handle empty input gracefully
		include_list = include_words.split(', ') if include_words else []
		exclude_list = exclude_words.split(', ') if exclude_words else []

		# Convert the max_length input to an integer (default to 0 if blank)
		max_length = int(max_length) if max_length.isdigit() else 0

		# Create an Anagram object with user inputs (includes, excludes, max length)
		anagram_finder = Anagram(inputstring, DICTIONARY, include_list, exclude_list, max_length)
	else:
		# If advanced options are not selected, create an Anagram object with just the input string and dictionary
		anagram_finder = Anagram(inputstring, DICTIONARY)

	# Call the function to find anagrams for the given input
	anagram_finder.findAnagrams()



if __name__ == '__main__':
    main()