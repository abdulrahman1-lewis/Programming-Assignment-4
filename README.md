# Chapter 2 Projects — Data Structures

This repository contains solutions to three projects from Chapter 2: Introduction to Data Structures.

---

## Project 2-1: Balanced Parentheses

**File:** `Balance_Parentheses.py`

Uses a stack to verify that a string of parentheses is balanced.

### Output

```
PS C:\Users\user\Desktop\algo\pa4> python Balance_Parentheses.py
Balanced examples:
  '(a(b+c)(d+(fg)h)d)'                -> True
  '(((ab)))'                          -> True
  '(a)(b)()()((())())'                -> True

Unbalanced examples:
  '(ab(c)(d)())'                      -> True
  '()())'                             -> False
  '(()()'                             -> False
```

> **Note:** The first "unbalanced" example `'(ab(c)(d)())'` is actually balanced (every `(` has a matching `)`), which is why the program correctly returns `True` for it — despite it being listed under "Unbalanced examples" in the test data.

---

## Project 2-2: Lexicographic Order

**File:** `Lex_order.py`

Implements `lex_insert(L, a, b)`, which inserts a tuple `(a, b)` into list `L`, keeping it sorted in ascending lexicographic order.

### Output

```
PS C:\Users\user\Desktop\algo\pa4> python Lex_order.py
[(1, 10), (2, 5), (3, 1), (8, 9), (8, 11)]
```

---

## Project 2-4: Palindrome Generator & Tester (Modified)

**File:** `Palindrom.py`

Per the professor's modified instructions, this file includes both:
- **`make_palindrome(txt)`** — builds an even-length palindrome by appending the reverse of `txt` to itself (original project spec).
- **`is_palindrome(txt)`** — checks whether an input string is already a palindrome (professor's modification).

### Output

```
PS C:\Users\user\Desktop\algo\pa4> python Palindrom.py
Palindrome Generator:
  txt = 'abc'       -> palindrome = 'abccba'
  txt = 'hello'     -> palindrome = 'helloolleh'
  txt = 'a'         -> palindrome = 'aa'
  txt = ''          -> palindrome = ''
  txt = 'race'      -> palindrome = 'raceecar'

Palindrome Tester:
  txt = 'fababaf'    -> is_palindrome: True
  txt = 'fabaabaf'   -> is_palindrome: True
  txt = 'aaa'        -> is_palindrome: True
  txt = 'aa'         -> is_palindrome: True
  txt = 'abc'        -> is_palindrome: False
  txt = 'caac'       -> is_palindrome: True
```
