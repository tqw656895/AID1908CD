try:
    f = open("hello.py","a",buffering=-1)
    print(f)
except Exception as e:
    print(e)
