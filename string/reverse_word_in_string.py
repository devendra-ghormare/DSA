def reverseWordInString(s:str):

    ls = s.split()
    return " ".join(ls[::-1])


print(reverseWordInString("the sky is blue"))