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
            print(f"  A  \n A A \nA   A\nAAAAA\nA   A\nA   A\nA   A")
        elif check_letter == "b":
            print(f"BBBB \nB   B\nB   B\nBBBB \nB   B\nB   B\nBBBB ")
        elif check_letter == "c":
            print(f" CCC \nC   C\nC    \nC    \nC    \nC   C\n CCC ")
        elif check_letter == "d":
            print(f"DDDD \nD   D\nD   D\nD   D\nD   D\nD   D\nDDDD ")
        elif check_letter == "e":
            print(f"EEEEE\nE    \nE    \nEEE  \nE    \nE    \nEEEEE")
        elif check_letter == "f":
            print(f"FFFFF\nF    \nF    \nFFF  \nF    \nF    \nF    ")
        elif check_letter == "g":
            print(f" GGG \nG   G\nG    \nGGGGG\nG   G\nG   G\n GGG ")
        elif check_letter == "h":
            print(f"H   H\nH   H\nH   H\nHHHHH\nH   H\nH   H\nH   H")
        elif check_letter == "i":
            print(f"IIIII\n  I  \n  I  \n  I  \n  I  \n  I  \nIIIII")
        elif check_letter == "j":
            print(f"JJJJJ\n  J  \n  J  \n  J  \nJ J  \nJ J  \n JJ  ")
        elif check_letter == "k":
            print(f"K   K\nK  K \nK K  \nKK   \nK K  \nK  K \nK   K")
        elif check_letter == "l":
            print(f"L    \nL    \nL    \nL    \nL    \nL    \nLLLLL")
        elif check_letter == "m":
            print(f"M   M\nMM MM\nMM MM\nM M M\nM   M\nM   M\nM   M")
        elif check_letter == "n":
            print(f"N   N\nNN  N\nN N N\nN  NN\nN   N\nN   N\nN   N")
        elif check_letter == "o":
            print(f" OOO \nO   O\nO   O\nO   O\nO   O\nO   O\n OOO ")
        elif check_letter == "r":
            print(f"RRRR \nR   R\nR   R\nRRRR \nR R  \nR  R \nR   R")
        elif check_letter == "s":
            print(f" SSS \nS   S\nS   \n SSS \n    S\nS   S\n SSS ")
        elif check_letter == "t":
            print(f"TTTTT\n  T  \n  T  \n  T  \n  T  \n  T  \n  T  ")
        elif check_letter == "u":
            print(f"U   U\nU   U\nU   U\nU   U\nU   U\nU   U\n UUU ")
        elif check_letter == "v":
            print(f"V   V\nV   V\nV   V\nV   V\nV   V\n V V \n  V  ")
        elif check_letter == "w":
            print(f"W   W\nW   W\nW   W\nW W W\nWW WW\nWW WW\nW   W")
        elif check_letter == "x":
            print(f"X   X\nX   X\n X X \n  X  \n X X \nX   X\nX   X")
        elif check_letter == "y":
            print(f"Y   Y\n Y Y \n  Y  \n  Y  \n  Y  \n  Y  \n  Y  ")
        elif check_letter == "z":
            print(f"ZZZZZ\n    Z\n   Z \n  Z  \n Z   \nZ    \nZZZZZ")
        elif check_letter == " ":
            print(" ")
        else:
            print(f"No block letter for {letters}")
    ascii_block_letter(letters)
    return ascii_block_letter

ascii_format(name)
  
