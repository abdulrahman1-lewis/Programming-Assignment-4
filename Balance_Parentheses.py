def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                # Closing parenthesis with nothing to match
                return False
            stack.pop()

    # Balanced only if every opening paren was matched (stack is empty)
    return len(stack) == 0


if __name__ == "__main__":
    balanced_examples = [
        "(a(b+c)(d+(fg)h)d)",
        "(((ab)))",
        "(a)(b)()()((())())"
    ]

    unbalanced_examples = [
        "(ab(c)(d)())",
        "()())",
        "(()()"
    ]

    print("Balanced examples:")
    for expr in balanced_examples:
        print(f"  {expr!r:35} -> {is_balanced(expr)}")

    print("\nUnbalanced examples:")
    for expr in unbalanced_examples:
        print(f"  {expr!r:35} -> {is_balanced(expr)}")