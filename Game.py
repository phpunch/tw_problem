class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.num_players = len(self.players)
        self.predictor_index = 0

    def check_play_again(self):
        print("Do you want to play again? [Press Y]")
        string = str(input(">> "))
        if (string == 'Y'):
            return True
        else:
            print("OK, Bye!")
            return False

    def check_hands(self, output: str, predicted_num: int) -> bool:
        count = 0
        for char in output:
            if (char == "O"): count += 1
        return True if (predicted_num == count) else False

    def select_predictor(self):
        # set to default
        for i in range(self.num_players):
            self.players[i].is_predictor = False
        
        # only one can be a predictor
        self.players[self.predictor_index % self.num_players].is_predictor = True

    def play(self):
        while True:
            self.select_predictor()

            hand_output = ""
            predicted_num = -1

            # guess the hands
            for index, player in enumerate(self.players):
                while (True): # receive inputs until a user enters the correct one
                    try:
                        output = player.guess()
                        break
                    except Exception:
                        continue
                hand_output += output
                if (index == self.predictor_index % self.num_players): predicted_num = int(output[2])

            # check_hands
            is_correct = self.check_hands(hand_output, predicted_num)
            if (is_correct):
                print("{} WIN".format(self.players[self.predictor_index % self.num_players].name))
                break
            else:
                print("No Winner")

            self.predictor_index += 1
            

        
        