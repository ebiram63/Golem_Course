def is_valid(expr):
    stack = []
    opened_symbol = "("
    closed_symbol = ")"
    
    for ch in expr:
        if ch == opened_symbol:
            stack.append(ch)
        elif ch == closed_symbol:
            if stack == []:
                return False
            stack.pop()
    return stack == []

print(is_valid("(2 + 3)"))
print(is_valid("(2 + 3)()(())"))
print(is_valid(")2 + 3("))