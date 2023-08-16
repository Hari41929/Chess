class Gamestate():
    def __init__(self):
        self.Board = [
            ["cr", "ckn", "cb", "cq", "ck", "cb", "ckn", "cr"],
            ["cp", "cp", "cp", "cp", "cp", "cp", "cp", "cp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["sp", "sp", "sp", "sp", "sp", "sp", "sp", "sp"],
            ["sr", "skn", "sb", "sq", "sk", "sb", "skn", "sr"]
        ]
        self.movelog = []  # Corrected this line
        self.white_turn = True  # Corrected this line
