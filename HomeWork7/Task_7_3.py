class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.end = True

    def advanced_search(self, word: str, node) -> bool:
        for i in range(len(word)):
            if word[i] not in node.children and word[i] != '.':
                return False
            elif word[i] == '.':
                for key in node.children:
                    if self.advanced_search(word[i + 1:], node.children[key]):
                        return True
                return False
            else:
                node = node.children[word[i]]
        if node.end:
            return True
        else:
            return False

    def search(self, word: str) -> bool:
        return self.advanced_search(word, self.root)

