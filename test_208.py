class TrieNode:
    def __init__(self):
            self.word=False
            self.children={}


class Trie: 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
                
        node.word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch  not in node.children:
                return False
            node = node.children[ch]   
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch  not in node.children:
                return False
            node = node.children[ch]   
        
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()

obj.insert("dtest")
obj.insert("dtes")

re = obj.search("dtes")
print ("result :%s"% re)

re = obj.search("dtet")
print ("result :%s"% re)

# param_2 = obj.search(word)
param_3 = obj.startsWith("dt")
print ("param_3 :%s"% param_3)