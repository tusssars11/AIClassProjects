
Anagram Finder - Improved Version
Overview
This project is an Anagram Finder that takes a word or phrase as input and finds all possible valid anagrams from a given dictionary. It can use the NLTK words corpus or a user-provided dictionary file. The code implements recursive search with memoization to optimize performance and avoid redundant calculations.
Features
	•	Type hints for improved readability.
	•	Supports both external word libraries (NLTK) and user-provided dictionaries.
	•	Implements optimized recursion with memoization.
	•	Prevents infinite recursion by ensuring proper base cases.
	•	Displays the found anagrams in a structured format or indicates if none are found.
Requirements
	•	Python 3.7+ (tested on Python 3.12)
	•	NLTK 3.9.1 (or compatible version)
	•	NLTK words corpus (downloaded via nltk.download('words'))
	•	Operating System: macOS, Windows, or Linux
Installation and Setup
	1	Install Python 3.7+ if not already installed.
	2	Clone or download this repository to your local machine.
	3	Open a terminal and navigate to the project folder: cd path/to/updatedAnagram
	4	
	5	Install NLTK: pip install nltk
	6	
	7	Download the NLTK words corpus: python -m nltk.downloader words
	8	
	9	Ensure the file structure looks like this: updatedAnagram/
	10	├── mainAnagram.py
	11	├── updatedAnagramFinderTK.py
	12	└── README.md
	13	
Usage
	1	In your terminal, navigate to the project directory.
	2	Run: python mainAnagram.py
	3	
	4	Enter the word or phrase you want to find anagrams for when prompted.
	5	If you have a custom dictionary file, enter its path when asked, or leave it blank to use the default NLTK corpus.
	6	The program will display all valid anagrams found or indicate that none are found.
File Descriptions
	•	updatedAnagramFinderTK.py Contains the AnagramFinder class, which does the following:
	◦	load_dictionary: Loads words from a specified file or defaults to the NLTK words corpus.
	◦	is_valid_word: Checks if a word can be formed from the letters of the input and if it exists in the dictionary.
	◦	find_anagrams: Calls the recursive method to generate valid anagrams.
	◦	_find_anagrams_recursive: Implements backtracking and memoization to build anagrams without infinite recursion.
	◦	display_anagrams: Prints the results in a structured format.
	•	mainAnagram.py A simple script that:
	◦	Prompts for user input (word/phrase and optional dictionary file path).
	◦	Instantiates AnagramFinder and calls display_anagrams() to show the results.
Citation
This project was developed with assistance from ChatGPT 4o to improve code efficiency, fix recursion issues, and enhance documentation. If citing this project, you can include:
Generated with support from OpenAI's ChatGPT for debugging, optimization, and documentation improvements.
For academic work, consider citing OpenAI:
OpenAI. (2025). ChatGPT - AI Language Model. Retrieved from https://openai.com/
