name = "VoiceofVoiceless"
#print(f"DDDD \nD   D\nD   D\nD   D\nD   D\nD   D\nDDDD ")
#print(f" OOO \nO   O\nO   O\nO   O\nO   O\nO   O\n OOO ")
#print(f"RRRR \nR   R\nR   R\nRRRR \nR R  \nR  R \nR   R")
#Is a Genius

def ascii_format(string):
    if string:
        letters = list(string)
    else:
      print("missing string")
    

    def ascii_block_letter(letters):
      for letter in letters:
        check_letter = letter.lower()
        if check_letter == "a":
            print(f"  A  \n A A \nA   A\nAAAAA\nA   A\nA   A\nA   A\n")
        elif check_letter == "b":
            print(f"BBBB \nB   B\nB   B\nBBBB \nB   B\nB   B\nBBBB ")
        elif check_letter == "c":
            print(f"")
        elif check_letter == "d":
            print(f"DDDD \nD   D\nD   D\nD   D\nD   D\nD   D\nDDDD ")
        elif check_letter == "e":
            print(f"")
        elif check_letter == "f":
            print(f"")
        elif check_letter == "g":
            print(f"")
        elif check_letter == "h":
            print(f"")
        elif check_letter == "i":
            print(f"")
        elif check_letter == "j":
            print(f"")
        elif check_letter == "k":
            print(f"")
        elif check_letter == "l":
            print(f"")
        elif check_letter == "m":
            print(f"")
        elif check_letter == "n":
            print(f"")
        elif check_letter == "o":
            print(f" OOO \nO   O\nO   O\nO   O\nO   O\nO   O\n OOO ")
        elif check_letter == "r":
            print(f"RRRR \nR   R\nR   R\nRRRR \nR R  \nR  R \nR   R")
        elif check_letter == "s":
            print(f" SSS \nS   S\nS   \n SSS \n    S\nS   S\n SSS ")
        elif check_letter == "t":
            print(f"")
        elif check_letter == "u":
            print(f"")
        elif check_letter == "v":
            print(f"")
        elif check_letter == "w":
            print(f"")
        elif check_letter == "x":
            print(f"")
        elif check_letter == "y":
            print(f"")
        elif check_letter == "z":
            print(f"")
        else:
            print("nothing")
    ascii_block_letter(letters)
    return ascii_block_letter

ascii_format(name)
  