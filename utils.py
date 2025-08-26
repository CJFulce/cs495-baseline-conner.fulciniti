def main():
    print("Directions: Enter a string to find its first unique char.\n")
    userInput = input("Enter string: ")
    result = first_unique_char(userInput)
    print(result)

def first_unique_char(userInput):
    charDict = {}
    firstUniqueIndex = -1
    for char in userInput:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    print("String processed.\n")
    print("Searching for first unique character...\n")
    
    for index in range(len(userInput)):
        candidateChar = userInput[index]
        if charDict[candidateChar] == 1:
            firstUniqueIndex = index
            break
    if firstUniqueIndex == -1:
        return("No unique character found within string.")
    else:
        return(firstUniqueIndex)
        
if __name__ == "__main__":
    main()