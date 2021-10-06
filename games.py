class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
def ask_yes_no (question):
    responce = None
    while responce not in ("y","n"):
        responce = input(question).lower()
    return responce
def ask_number(question, low, high):
    responce = None
    while responce not in range(low, high):
        responce = int(input(question))
    return responce
if __name__ == "__main__":
    print()