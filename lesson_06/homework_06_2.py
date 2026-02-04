# homework_06_2.py
# Ask user to enter a word that contains letter "h" or "H"
# Loop should continue until the condition is satisfied

while True:
    word = input("Enter a word containing letter 'h': ")
    if 'h' in word.lower():
        print("Correct! The word contains letter 'h'.")
        break
    else:
        print("The word does NOT contain letter 'h'. Try again.")
