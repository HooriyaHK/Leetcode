# leetcode 1
def merge_string(word1: str, word2: str) -> str:
    """
    Function merges the strings alternately, character by character
    Time complexity and Space complexity is O(n+m)
    Parameters
        :type word1: str
        :type word2: str
        :rtype: str
    """
    # create an empty array
    merged = []
    # total length
    max_len = len(word1)+ len(word2)
    for i in range(max_len):
        # Add from word1 if within bounds
        if i < len(word1):
            merged.append(word1[i])
            # Add from word2 if within bounds
        if  i < len(word2):
            merged.append(word2[i])
    # return the string
    return ''.join(merged)


 # Test cases           
word1 = "abc"
word2 = "pqrstuv"
result = merge_string(word1, word2)

# Expected output: "apbqcrstuv"
print(result)  