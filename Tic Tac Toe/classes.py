class board():
    def __init__(self):
        self.boxes = [" ", " ", " ", " ", " ", " ", " ", " ", " "," "]
    
    def display(self):
        print("")
        print("      %s | %s | %s " %(self.boxes[1], self.boxes[2], self.boxes[3]))
        print("     ===========")
        print("      %s | %s | %s " %(self.boxes[4], self.boxes[5], self.boxes[6]))
        print("     ===========")
        print("      %s | %s | %s " %(self.boxes[7], self.boxes[8], self.boxes[9]))
        print("                                                          ")
    
    def update_box(self, box_no, player):
        if self.boxes[box_no] == " ":
            self.boxes[box_no] = player
    
    def winner(self, player):
        if self.boxes[1] == player and self.boxes[2] == player and self.boxes[3] == player:
            return True
        if self.boxes[4] == player and self.boxes[5] == player and self.boxes[6] == player:
            return True
        if self.boxes[7] == player and self.boxes[8] == player and self.boxes[9] == player:
            return True
        if self.boxes[1] == player and self.boxes[4] == player and self.boxes[7] == player:
            return True
        if self.boxes[2] == player and self.boxes[5] == player and self.boxes[8] == player:
            return True
        if self.boxes[3] == player and self.boxes[6] == player and self.boxes[9] == player:
            return True
        if self.boxes[1] == player and self.boxes[5] == player and self.boxes[9] == player:
            return True
        if self.boxes[3] == player and self.boxes[5] == player and self.boxes[7] == player:
            return True
        return False
    
    def tie(self):
        used_boxs = 0
        for box in self.boxes:
            if box != " ":
                used_boxs +=1
        if used_boxs == 9:
            return True
        else:
            return False   
    def reset(self):
        self.boxes = [" ", " ", " ", " ", " ", " ", " ", " ", " "," "]


