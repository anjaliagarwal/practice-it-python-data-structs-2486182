from collections import deque

def check_palindrome(word):
  d = deque(word)
  while len(d) > 1:
    if d.pop() != d.popleft():
      return False
  return True

def main():
    #add code here
    word = "abba"
    print(check_palindrome(word))
    return

if __name__ == "__main__":
    main()