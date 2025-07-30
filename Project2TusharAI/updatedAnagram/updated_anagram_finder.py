"""
Anagram Finder - Improved Version

Features:
- Uses type hints for better readability.
- Supports external word libraries (NLTK) or user-provided dictionaries.
- Implements optimized recursive search with memoization.
- Prevents infinite recursion by ensuring proper base cases.
"""

import collections
from typing import Set, Dict
import nltk
from nltk.corpus import words

# Ensure the words list is available in NLTK
nltk.download('words')


class AnagramFinder:
    """
    An improved anagram finder that generates valid anagrams efficiently.
    """

    def __init__(self, word: str, dictionary_file: str = "") -> None:
        """
        Initializes the Anagram Finder with a given word and dictionary.
        """
        self.word: str = word.lower().replace(" ", "")  # Normalize input
        self.letter_count: collections.Counter = collections.Counter(
            self.word)  # Track character frequencies
        self.memo: Dict = {}  # Memoization for optimization
        self.dictionary: Set[str] = self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file: str) -> Set[str]:
        """
        Loads a dictionary of valid words.
        """
        if dictionary_file:
            try:
                with open("dictionary.txt", "r", encoding="utf-8") as file:
                    return {line.strip().lower() for line in file}
            except FileNotFoundError:
                print("Error: Dictionary file not found. Using NLTK word list instead.")
        return set(words.words())

    def is_valid_word(self, word: str) -> bool:
        """
        Checks if a word is valid and can be formed from the input string.
        """
        word_count = collections.Counter(word)
        return all(word_count[char] <= self.letter_count[char]
                   for char in word) and word in self.dictionary

    def find_anagrams(self) -> Set[str]:
        """
        Finds valid anagrams of the input word using recursive search.
        """
        return self._find_anagrams_recursive("", self.letter_count)

    def _find_anagrams_recursive(
            self,
            current: str,
            remaining_letters: collections.Counter) -> Set[str]:
        """
        Recursively generates anagrams using backtracking with memoization.
        """
        key = tuple(sorted(remaining_letters.items()))
        if key in self.memo:
            return self.memo[key]

        # BASE CASE: If there are no letters left, return the current word
        if sum(remaining_letters.values()) == 0:
            return {current.strip()} if current.strip(
            ) in self.dictionary else set()

        anagrams: Set[str] = set()
        for word in self.dictionary:
            if self.is_valid_word(word):
                new_remaining = remaining_letters - collections.Counter(word)

                # 🚨 Prevent infinite recursion: Ensure `new_remaining` is reducing
                if new_remaining != remaining_letters:
                    anagrams.update(
                        self._find_anagrams_recursive(
                            current + " " + word, new_remaining))

        self.memo[key] = anagrams
        return anagrams

    def display_anagrams(self) -> None:
        """
        Displays the found anagrams in a structured format.
        """
        anagrams = self.find_anagrams()
        if anagrams:
            print(f"Found {len(anagrams)} anagrams for '{self.word}':")
            print(", ".join(sorted(anagrams)))
        else:
            print(f"No anagrams found for '{self.word}'.")
