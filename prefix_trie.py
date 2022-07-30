END_SYMBOL = "*"
WORD_COUNT = "count"

class Trie:
    def __init__(self):
        self.root_node = {}

    # Check if string 'word' is contained in the trie
    # O(n) time | O(1) space
    def __contains__(self, word: str) -> bool:
        curr_node = self.root_node
        for c in word:
            if c not in curr_node:
                return False
            curr_node = curr_node[c]
        return END_SYMBOL in curr_node

    # Add the string 'word' to the trie
    # O(n) time | O(1) space
    def add(self, word: str) -> None:
        curr_node = self.root_node
        for c in word:
            if c not in curr_node:
                curr_node[c] = {WORD_COUNT: 0}
            curr_node = curr_node[c]
            curr_node[WORD_COUNT] += 1
        curr_node[END_SYMBOL] = True

    # Remove the string 'word' from the trie
    # O(n) time | O(1) space
    def delete(self, word: str) -> None:
        curr_node = self.root_node
        for c in word:
            curr_node[c][WORD_COUNT] -= 1
            if curr_node[c][WORD_COUNT] == 0:
                del curr_node[c]
                return
            curr_node = curr_node[c]
        del curr_node[END_SYMBOL]
