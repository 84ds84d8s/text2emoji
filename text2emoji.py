def main():
    string=input()
    lib1="❗eeeeeeeee➕e➖ee⿠⿡⿢⿣⿤⿥⿦⿧⿨⿩eee🟰e❓e🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿eeeeee🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"
    for char in string:
        if ord(char)<158:
            x=lib1[ord(char)-33]#as 33 char !in lib1
            if x!="e":
                print(x, end=" ")
            else:#when char unincluded
                print(char, end=" ")
        elif ord(char)==158:
            print("✖", end=" ")
        elif ord(char)==246:
            print("➗", end=' ')
        else:
            print(char, end=" ")
    u = input("Press 1 to continue, any other key to exit: ")
    if u == "1":
        main()
main()
