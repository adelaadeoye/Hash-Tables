cache={}
word=""
def no_dups(s):
    # Implement me.
    words= s.split()
    for item in words:
        if item not in cache:
            cache[item]=item
        break
    return(' '.join(list(cache)))

    

            


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))