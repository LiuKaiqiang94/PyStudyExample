
def main():
    print("This program coverts a sequence of Unicode numbers into")
    print("the string of text that it reptrsents.\n")

    inString = input("Please enter the Unicode-encoded message:")
    chars = []
    for numStr in inString.split():
        codeNum=int(numStr)
        chars.append(chr(codeNum))

    message="".join(chars)
    print("\nThe decoded message is:",message)

main()
