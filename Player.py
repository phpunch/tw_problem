import random
class Player:
    def __init__(self, name: str):
        self.is_predictor = False
        self.name = name
    def guess() -> str:
        pass

class Human(Player):
    def validate_input(self, string: str):

        chars = ["C", "O"]
        
        if (self.is_predictor):
            if (len(string) != 3):
                print("Bad input: correct input should be of the form CC3, where the first two letters indicate [O]pen or [C]losed state for each hand, followed by the prediction (0-4).")
                return False
            elif (string[0] not in chars or string[1] not in chars):
                print("Bad input: correct input should be of the form CC3, where the first two letters indicate [O]pen or [C]losed state for each hand, followed by the prediction (0-4).")
                return False
            elif (not string[2].isdigit()):
                print("Bad input: prediction should be a number in the range of 0-4")
                return False
            elif (int(string[2]) > 4 or int(string[2]) < 0):
                print("Bad input: prediction should be in the range of 0-4")
                return False
        else:
            if (len(string) == 3):
                if (not string[2].isdigit()):
                    print("Bad input: no prediction expected, you are not the predictor.")
                else :
                    print("Bad input: correct input should be of the form CC, where the two letters indicate [O]pen or [C]losed state for each hand")
                return False
            elif (len(string) != 2):
                print("Bad input: correct input should be of the form CC, where the two letters indicate [O]pen or [C]losed state for each hand")
                return False
            elif (string[0] not in chars or string[1] not in chars):
                print("Bad input: correct input should be of the form CC, where the two letters indicate [O]pen or [C]losed state for each hand")
                return False
            
        return True
        
    def guess(self) -> str:
        if (self.is_predictor):
            print("You are the predictor. What's your input?")
        else:
            print("AI is the predictor. What's your input?")
        
        string = str(input(">> "))
        if self.validate_input(string):
            return string
        else:
            raise Exception

class Bot(Player):
    def randomHand(self, num) -> str:
        string = ""
        for i in range(num):
            string += random.choice(["C", "O"])
        return string

    def randomNumber(self) -> str:
        return str(random.randint(0, 4))

    def randomInput(self) -> str:
        if (self.is_predictor):
            return self.randomHand(2) + self.randomNumber()
        else:
            return self.randomHand(2)

    def guess(self) -> str:
        output = self.randomInput()
        print("Bot guess:",output)
        return output
