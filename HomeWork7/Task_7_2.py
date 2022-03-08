class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = Node()
            pointer = pointer.children[letter]
        pointer.end_of_word = True

    def search(self, word):
        pointer = self.root
        ans =[]
        for letter in word:
            if letter not in pointer.children:
                return word
            pointer = pointer.children[letter]
            ans.append(letter)
            if pointer.end_of_word:
                return ''.join(ans)
        return word



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer =[]
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        sentence_list = sentence.split()
        for word in sentence_list:
            checker = trie.search(word)
            answer.append(checker)
        return ' '.join(answer)