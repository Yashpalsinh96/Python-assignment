string1 = "listen"
string2 = "silent"

if len(string1)!=len(string2):
    print("False")

else:

    if sorted(string1) == sorted(string2):
        print("True")
    else:
        print("False")
