

# Word Ladder - I : G-29 

from collections import deque

def word_ladder_length(start_word, target_word, word_list):
    # Convert word_list to a set for O(1) lookups and deletions
    word_set = set(word_list)
    if target_word not in word_set:
        return 0
    
    # BFS queue storing (current_word, transformation_steps)
    queue = deque([(start_word, 1)])
    word_set.discard(start_word)
    
    while queue:
        word, steps = queue.popleft()
        
        # If we reach the target word, return the steps
        if word == target_word:
            return steps
        
        # Try changing each character in the word
        for i in range(len(word)):
            original_char = word[i]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch != original_char:  # Avoid replacing with the same character
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, steps + 1))
    
    return 0  # No transformation sequence found

# Driver Code
word_list = ["des", "der", "dfr", "dgt", "dfs"]
start_word = "der"
target_word = "dfs"

result = word_ladder_length(start_word, target_word, word_list)
print(result)

