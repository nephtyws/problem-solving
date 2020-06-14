# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1


from typing import Tuple


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    count = 0
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        count += 1
        print(char)
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            count *= 8
            return False, count
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, count


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "majmunica")
    add(root, 'majmun')
    add(root, 'majka')
    add(root, 'malina')
    add(root, 'malinska')
    add(root, 'malo')
    add(root, 'maleni')
    add(root, 'malesnica')

    print(find_prefix(root, 'krampus'))
    print(find_prefix(root, 'malnar'))
    print(find_prefix(root, 'majmun'))


'''
number_of_words = int(input())

words = []

for _ in range(number_of_words):
    words.append(input())

number_of_queries = int(input())

for _ in range(number_of_queries):
    query = input()
    count = 0

    for word in words:
        find = False
        length_counter = 1

        for query_character, word_character in zip(query, word):
            count += 1

            if length_counter == len(query):
                if query == word[:length_counter] and len(query) == len(word):
                    find = True

                count += 1

                break

            if query_character != word_character:
                break

            length_counter += 1

        if find:
            break

    print(count)
'''