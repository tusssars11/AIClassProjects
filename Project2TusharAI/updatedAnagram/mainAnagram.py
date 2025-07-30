"""
Main script to execute the Anagram Finder
"""
import sys
import os

# Ensure the script can find 'updatedAnagramFinderTK.py' in the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from updated_anagram_finder import AnagramFinder 

def main() -> None:
    """
    Main function to handle user input and execute the anagram finder.
    """
    user_input: str = input("Enter a word or phrase to find anagrams: ").strip()
    dictionary_file: str = input("Enter dictionary file path (leave blank for NLTK default): ").strip()
    
    # Create an instance of the AnagramFinder class
    finder = AnagramFinder(user_input, dictionary_file)
    
    # Display found anagrams
    finder.display_anagrams()

if __name__ == "__main__":
    main()
