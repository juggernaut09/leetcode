class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use a Hashmap. Assume that the string contains only 128 characters. Not an
        ASCII. Take an array of length 128 and initialize that array with 0s.
        traverse through the list of words. count the number of alphabets by
        updating the array(128 length). if you encounter 'a' character increment the
        index of that respective ASCII code. use the array as the key to store the
        list of the strings with the same keys. 
        """
        hmap = {}
        for s in strs:
            char_set = [0]*128
            for c in s:
                char_set[ord(c)] += 1
            if tuple(char_set) not in hmap.keys():
                hmap[tuple(char_set)] = [s]
            else:
                hmap[tuple(char_set)].append(s)
        res = []
        for key, value in hmap.items():
            res.append(value)
        return res



        