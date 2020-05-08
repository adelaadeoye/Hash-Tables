import re

def word_count(s):
   cache={}
    # Implement me.
   split= s.split()
   for item in split:
       key=''.join( c for c in item if  c not in ':;,.-+=/\\|[]{}()*^&"' )
       key=key.lower()
       if key =="":
           return {}
       elif key not in cache :
           cache[key]=1
       else:
            cache[key]+=1
   return (cache)
if __name__ == "__main__":
    print(word_count(""))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))