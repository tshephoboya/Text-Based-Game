from random import choice
from string import ascii_lowercase

possible_escapes = list(ascii_lowercase)
rooms = [ ['room1', 'air', 'The air is being sucked out'],
          ['room2', 'fire', 'The room get hotter'],
          ['room3', 'ceiling', 'The ceiling is caving in'],
          ['room4', 'snake', 'You are stuck in a room with a snake'],
          ['room5', 'Carbon Monoxide', 'The room is filling with carbon monoxide']]
class room:
    room_number = 0
    def __init__(self, name, danger, description, safety):
        self.name = name
        self.danger = danger
        self.description = description
        self.safety = safety

    def guess_safety(self):
        count = 10
        while count > 0:
            count -= a
            if input('Guess escape mode: ').lower() != self.safety:
                print("The guess is wrong.", count, 'Guesses Left')
            else:
                print("Hoooray, Your guess is correct!!")
                return True
        else:
            print("You are out off guesses", 'You have DIED :)')
            return False
        

def start_game():
    room_obj = room(rooms[room.room_number][0],  rooms[room.room_number][1], rooms[room.room_number][2], choice(possible_escapes))
    print(room_obj.description, room_obj.danger, sep=' - ')
    if room_obj.guess_safety() == True and room.room_number < 4:
        del room_obj
        room.room_number += 1
        start_game()
    else:
         if input("Play again y/n: ").lower() ==  'y':
            del room_obj
            room.room_number = 0
            start_game()
                      
start_game()
