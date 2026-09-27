def make_palindrome(txt):
    """Builds an even-length palindrome from txt."""
    reversed_txt = ""
    for i in range(len(txt) - 1, -1, -1):
        reversed_txt = reversed_txt + txt[i]
    return txt + reversed_txt


def is_palindrome(txt):
    """Checks if txt is already a palindrome."""
    reversed_txt = ""
    for i in range(len(txt) - 1, -1, -1):
        reversed_txt = reversed_txt + txt[i]
    return txt == reversed_txt


if __name__ == "__main__":
    print("Palindrome Generator:")
    for txt in ["abc", "hello", "a", "", "race"]:
        print(f"  txt = {txt!r:10} -> palindrome = {make_palindrome(txt)!r}")

    print("\nPalindrome Tester:")
    for txt in ["fababaf", "fabaabaf", "aaa", "aa", "abc", "caac"]:
        print(f"  txt = {txt!r:12} -> is_palindrome: {is_palindrome(txt)}")