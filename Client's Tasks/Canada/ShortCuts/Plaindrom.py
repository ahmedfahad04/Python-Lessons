def isPalindrome(word):
    n = len(word)  # length of 'word'
    flag = 1

    if n >= 3:      # check if the words' length is more or equal than 3
        for i in range(0, n // 2):
            if word[i] != word[n - i - 1]:  # checking for palindrome
                flag = 0
                break
    else:
        flag = 0

    return flag
