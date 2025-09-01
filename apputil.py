

# add code below ...
def palindrome(word):
    cleaned = ""
    for ch in word:
        # Keep lowercase letters a–z
        if "a" <= ch.lower() <= "z" or "0" <= ch <= "9":
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]

def parentheses(sequence):
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack