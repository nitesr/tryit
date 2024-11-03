from collections import deque

class Solution1:
    def __init__(self, start_word, target_word, words):
        self.src_words = [w for w in words]
        self.words = set(words)
        self.start_word = start_word
        self.target_word = target_word
        self.adjacency_list = {}
        self.current_path = []
        self.shortest_paths = []
    
    # This function finds all the possible transformation of a word that exists in the word list.
    def find_neighbors(self, word):
        neighbors = []
        for i in range(len(word)):
            original_character = word[i]
            # Replace the i-th character with all letters from a to z except the original character.
            for replaced_character in range(ord('a'), ord('z') + 1):
                replaced_character = chr(replaced_character)
                if replaced_character != original_character and word[:i]+replaced_character + word[i + 1:] in self.words:
                    neighbors.append(word[:i]+replaced_character + word[i + 1:])
            word = word[:i] + original_character + word[i + 1:]
        return neighbors


    # This function traverses the DAG to find all the paths between `start_word` and `target_word`.
    def backtrack(self, start_word, target_word):
        if start_word == target_word:
            self.shortest_paths.append(list(self.current_path))
        for neighbor in self.adjacency_list.get(start_word, []):
            self.current_path.append(neighbor)
            self.backtrack(neighbor, target_word)
            self.current_path.pop()


    # This function builds a DAG using BFS.
    def bfs(self, start_word, target_word):
        # Remove the root word which is the first layer.
        if start_word in self.words:
            self.words.remove(start_word)

        queue = deque()
        is_enqueued = {start_word: 1}
        queue.append(start_word)
        while queue:
            # `visited` will store the words of the current layer.
            visited = []
            queue_size = len(queue)
            while queue_size:
                current_word = queue.popleft()

                # `neighbors` will store the adjacent words of `current_word`.
                neighbors = self.find_neighbors(current_word)
                for word in neighbors:
                    visited.append(word)
                    # Add an edge from `current_word` to `word` to create a DAG.
                    self.adjacency_list.setdefault(current_word, []).append(word)

                    if word not in is_enqueued:
                        queue.append(word)
                        is_enqueued[word] = 1
                queue_size -= 1

            # Removing the words of the previous layer.
            for word in visited:
                if word in self.words:
                    self.words.remove(word)

    def get_all_shortest_transformation_sequences(self):
        self.bfs(self.start_word, self.target_word)
        self.current_path.clear()
        self.current_path.append(self.start_word)
        self.backtrack(self.start_word, self.target_word)
        return self.shortest_paths

class Solution2:
    def __init__(self, start_word, target_word, words):
        self.words = set([w for w in words])
        self.src_words = words
        self.start_word = start_word
        self.target_word = target_word
        self.all_short_moves = []
        self.word_visits = {}
    
    def find_neighbors(self, word):
        nbs = set()
        for i in range(len(word)):
            for ci in range(ord('a'), ord('z')+1):
                c = chr(ci)
                nb = f"{word[0:i]}{c}{word[i+1:]}"
                if c != word[i] and nb in self.word_set:
                    nbs.add(nb)
        return nbs

    def bfs(self, start_word, target_word):
        q = deque()
        q.append((start_word, 0))
        
        self.word_visits = {}
        for w in self.word_set:
            self.word_visits[w] = (-1, [])
        self.word_visits[start_word] = (0, [])
        
        min_hops = len(self.word_set)
        while len(q) > 0:
            w, hops = q.popleft()
            
            if hops == min_hops:
                break
            
            for nb in self.find_neighbors(w):
                next_hops = hops + 1
                if self.word_visits[nb][0] == -1:
                    q.append((nb, hops+1))
                    self.word_visits[nb] = (next_hops, [w])
                elif self.word_visits[nb][0] == next_hops:
                    self.word_visits[nb][1].append(w)
                else:
                    self.word_set.remove(nb)
                
                if nb == target_word:
                    min_hops = next_hops

    def collect_paths(self, cur_word, start_word, path):
        if cur_word == start_word:
            self.all_short_moves.append([start_word, *list(reversed(path))])
            return
        
        path.append(cur_word)
        for next_word in self.word_visits[cur_word][1]:
            self.collect_paths(next_word, path)
        path.pop()
    
    def get_all_shortest_transformation_sequences(self):
        if self.target_word not in self.words:
            return []
    
        self.bfs(self.start_word, self.target_word)
        
        if self.word_visits[self.target_word][0] != -1:
            self.collect_paths(self.target_word, [])

        return self.all_short_moves

def get_all_shortest_transformation_sequences(start_word, target_word, words):
    """
    Args:
     start_word(str)
     target_word(str)
     words(list_str)
    Returns:
     list_list_str
    """
    sol1 = Solution1(start_word, target_word, words)
    sol2 = Solution2(start_word, target_word, words)

    