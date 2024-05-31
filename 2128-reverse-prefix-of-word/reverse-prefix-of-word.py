class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the character 'ch' in the word
        ind = word.find(ch)
        if ind == -1:
            return word  # If character not found, return the original word
        
        # Reverse the prefix up to the index 'ind'
        prefix = word[:ind+1][::-1]
        
        # Append the remaining characters after 'ch'
        ans = prefix + word[ind+1:]
        
        return ans