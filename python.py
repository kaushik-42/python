class Solution:
    def reverseWords(self, str):
    words = str.split(" ")
    reverse = ''
    for word in words:
        word = word[::-1]
        if reverse == '':
            reverse = word
        else:
            reverse = reverse + " "+word
    return reverse


print(reverseWords().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
