
# n = int(input("Enter the lenght of array: "))

# arr = []
# for i in range (n):
#     arr.append(int(input()))

# hash = 13 * [0]
# for i in range(n):
#     hash[arr[i]] += 1

# q = int(input("Enter how many numbers to query: "))

# while (q>0):
#     numb = int(input("Enter number: "))
#     print(hash[numb])
#     q -=1
    
    
    
################## for string


s = str(input("Enter the string: "))

hash = 26 * [0]

for i in range(len(s)):
    hash[ord(s[i])- ord('a')] += 1

q = int(input("Enter the num of character to search: "))

while (q > 0):
    ch = str(input("Enter char to search: "))
    print(hash[ord(ch) - ord('a')])
    q-=1