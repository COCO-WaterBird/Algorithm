
def validate_bracket(string):
    stack = [] # Create an empty stack
    bracket_mapping = { ')':'(', '}':'{', ']':'['}
    #mapping the closing parentheses to the opening

    # Traverse the string
    for char in string:
        if char in bracket_mapping.values():      # if it is opening parentheses
            stack.append(char)
        elif char in bracket_mapping.keys():      # if it is closing parentheses
            if not stack or stack[-1] != bracket_mapping[char]:   # Check if stack empty or bracket mapping
                return False
            stack.pop()    #Removing the matched bracket

    return not stack
    # Check if stack is empty

example1 = "I { love [ the {rains}()]}"
print(validate_bracket(example1))

example1 = "I { love [ the {rains ] ()"
print(validate_bracket(example1))