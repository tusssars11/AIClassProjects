# The defaultdict has a default value for all keys, which speeds up lookup time considerably.
from collections import defaultdict 

"""
Summary: Given a word/phrase and a dictionary, this program generates all valid anagrams.
The main class `Anagram` handles input processing, while `Trie` is used for fast word lookup.
"""

class Anagram:
    """ 
    Precondition: 
        - Takes as arguments:
            1. `inputstring`: The string for which to find anagrams.
            2. `filename`: Name of the dictionary file.
            3. `include`: List of words that **must** be in the anagram.
            4. `exclude`: List of words that **must not** be in the anagram.
            5. `maxlength`: Maximum number of words in the anagram (0 = unlimited).
    
    Postcondition:
        - Generates a **Trie** of all dictionary words (excluding unwanted words).
        - Cleans and processes the input string.
    
    Summary: 
        - Prepares the **Trie** for searching anagrams efficiently.
        - Stores letter counts for lookup and recursive traversal.
    """

    def __init__(self, inputstring, filename, include=[], exclude=[], maxlength=0):
        # Normalize the input string: Convert to lowercase and remove non-alphabetic characters.
        self.string = ''.join(char for char in inputstring.lower() if 97 <= ord(char) <= 122)

        # Open the dictionary file and initialize necessary class variables.
        dictionaryFile = open(filename, 'r')
        self.filename = filename
        self.inputstring = inputstring

        # Convert the input string into a list of characters.
        # Remove letters that are part of "must-include" words to ensure they are used in anagrams.
        stringlist = list(self.string)
        for word in include:
            for letter in word:
                if letter in stringlist:
                    stringlist.remove(letter)  # Remove used letters
                else:
                    raise Exception(f"Not enough occurrences of '{letter}' in input '{self.inputstring}'.")

        # Update the cleaned input string after reserving letters for required words.
        self.string = ''.join(stringlist)

        # Create a new Trie and insert dictionary words into it, excluding unwanted words.
        self.trie = Trie(include, maxlength)
        for word in dictionaryFile:
            cleanword = word.strip().lower()  # Normalize word
            if cleanword not in exclude:
                self.trie.insert(cleanword)  # Insert only if not in exclusion list

    """
    Precondition: `__init__()` must have been run to set up the Trie.
    Postcondition: Prints an exhaustive list of all valid anagrams.
    Summary: Starts recursive traversal of the Trie to generate anagrams.
    """
    def findAnagrams(self):
        # Create a dictionary to count occurrences of each unique letter in `self.string`.
        # This helps in quick lookups to check if a letter is still available.
        chars = defaultdict(int)
        for char in set(self.string):
            chars[char] = self.string.count(char)

        # Start the recursive anagram generation from the Trie root.
        self.trie.anagramization(chars, self.trie.root, [], len(self.string), "")

        # Display the total number of unique anagrams found.
        print(f"\nThere were {self.trie.count} unique anagrams made from '{self.inputstring}' using the dictionary '{self.filename}'.")


"""
Summary: The Trie class stores words from the dictionary in an efficient **prefix tree** format.
"""
class Trie:
    """ 
    Precondition: 
        - List of words to include (`include`) and maximum length of an anagram (`maxlength`).
    
    Postcondition:
        - Creates a Trie where each word is stored **letter by letter**.
        - Allows **fast traversal** for checking anagrams.
    
    Summary: 
        - Stores dictionary words in a Trie for **efficient prefix-based search**.
        - Uses recursion to explore all possible anagrams.
    """
    def __init__(self, include, maxlength):
        self.root = Node('')  # Root node of the Trie (empty character)
        self.count = 0  # Counter for the number of valid anagrams found
        self.maxlength = maxlength if maxlength else float('inf')  # Set max words per anagram
        self.include = include  # List of words that **must** appear in an anagram

    """
    Precondition: `insert()` is called with a valid word.
    Postcondition: The word is added letter by letter to the Trie.
    Summary: Stores dictionary words in a structured Trie for efficient searching.
    """
    def insert(self, word):
        current = self.root  # Start at the Trie root
        for letter in word:
            child = current.findChild(letter)  # Check if letter already exists in Trie
            if not child:
                child = Node(letter)  # Create a new node for the letter
                current.addChild(letter, child)  # Add it to Trie
            current = child  # Move to next letter
        
        current.leafiness = True  # Mark last letter as the end of a word

    """
    Precondition: The Trie is built, and a defaultdict `chars` contains letter counts.
    Postcondition: Outputs valid anagrams by traversing the Trie recursively.
    Summary: Uses **backtracking** to generate anagrams using available letters.
    """
    def anagramization(self, chars, current, progress, wordlength, previousWord):
        # Base case: If we reach a leaf node, we have formed a valid word.
        if current.leafiness:
            word = ''.join(progress)  # Convert list of characters to a word
            
            # Ensure lexicographic order to avoid duplicate anagrams.
            if word.split()[-1] >= previousWord:
                # If the length of the formed word matches the original word, print it.
                if len(''.join(word.split())) == wordlength:
                    self.count += 1  # Increment the count of found anagrams
                    print(f"{self.count:4}: {' '.join(sorted(self.include + word.split()))}")
                
                # Continue searching for multi-word anagrams if max length allows.
                elif len(self.include + word.split()) < self.maxlength:
                    self.anagramization(chars, self.root, progress + [' '], wordlength, word.split()[-1])

        # Recursive exploration: Try extending the word with each available letter.
        for letter, node in current.children.items():
            if chars[letter] > 0:  # Ensure we still have this letter available
                chars[letter] -= 1  # Reduce the count of this letter (backtracking)
                self.anagramization(chars, node, progress + [letter], wordlength, previousWord)
                chars[letter] += 1  # Restore the letter count after recursion

"""
Summary: Represents a **single node** in the Trie, storing a letter and its child nodes.
"""
class Node:
    def __init__(self, letter):
        self.letter = letter  # Character stored in this Trie node
        self.children = {}  # Dictionary mapping letters to child nodes
        self.leafiness = False  # Marks whether this node completes a word

    def addChild(self, letter, child):
        """ Adds a child node to this Trie node. """
        self.children[letter] = child

    def findChild(self, letter):
        """ Retrieves a child node if it exists. """
        return self.children.get(letter, None)
