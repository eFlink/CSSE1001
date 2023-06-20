"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{erik flink}} ({{s4626744}})"
__email__ = "s4626755@uqconnect.edu.au"
__date__ = ""

# Write your code here

class Entity(object):
    """
    Constructor of the Generic Entity base.

    """
    def __init__(self):
        """
        Constructor of the Generic Entity base.

        """        
        return None
                
    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """  
        return str("Entity")

    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """  
        return str('Entity')

    def set_collide(self, Collidable):
        """
        Sets the collide condition of Entity.

        Parameters:
            bool:collide condition
            
        """  
        self._collidable=Collidable
        return None        
    
    def can_collide(self):
        """
        Returns the collide state to True(collidable)
        unless programmed to do otherwise

        Returns:
            collide state: bool
        """ 
        try:
            return bool(self._collidable)
        except:
            return True
        
    def __str__(self):
        """
        Returns beginning building block of ID presented on board the board
        for Entity subclasses and 

        Returns:
            String of Entity Name and ID in NAME('ID') layout  
        """ 
        return str("{0}('{1}')".format(self.get_name(),self.get_id()))

    def __repr__(self):
        """
        Returns __str__(self) 

        Returns:
            String of Entity Name and ID in NAME('ID') layout  
        """ 
        return self.__str__()

class Wall(Entity):
    """
    Constructor of the non-changing, non-collidable Entity base.

    """
    def __init__(self):
        """
        Returns None   
        """ 
        return None
    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """         
        return str(WALL)

    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """ 
        return str('Wall') 


class Item(Entity):
    """
    Class base for collidable items within the game.

    """ 
    def __init__(self):
        """
        returns None

        """ 
        return None
    
    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """  
        return str('Item')

    def on_hit(self, game):
        """
        Returns name of the Entity.

        Parameters:
            GameApp() state

        Returns:
            Impemented Error type
        """  
        raise NotImplementedError

class Key(Item):
    """
    Key subclass of items.

    """ 
    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """  
        return str(KEY)
    
    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """  
        return str('Key')

    def on_hit(self, game):
        """
        Removes the key item from the board and adds it to the players
        inventory.

        Parameters:
            GameApp() state
            
        Returns:
            None
        """  
        position=game.get_positions(KEY)[0]
        game._player.add_item(game._game_information[position])
        game._game_information.pop(position)
        

class MoveIncrease(Item):
    """
    MoveIncrease subclass of items.

    """ 
    def __init__(self, moves=5):
        """
        A standard increase of 5 moves is added to the move count

        Returns:
            None
        """
        self._moves=moves

    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """  
        return str(MOVE_INCREASE)

    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """  
        return str('MoveIncrease')

    def on_hit(self, game):
        """
        Removes the MoveIncrease item from the board and the moves in the
        move count increase are added to the players move count.
        
        Parameters:
            GameApp() state
            
        Returns:
            None
        """  
        position=game.get_positions(MOVE_INCREASE)[0]
        game._player.change_move_count(self._moves)
        game._game_information.pop(position)
        

class Door(Entity):
    """
    Collidable Entity.

    """
    def __init__(self):
        """
        Only requires self as an input, not changing any variables.

        """
        return None
    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """  
        return str(DOOR)

    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """ 
        return str('Door')
    
    def on_hit(self,game):
        """
        Changes the winning output depending on whether Key() item is
        in the players inventory or not.

        Parameters:
            GameApp() state     

        Returns:
            None
        """  
        position=game.get_positions(DOOR)[0]
        try:
            "Key('K')" == str(game._player.get_inventory()[0])
            game.set_win(True)
        except:
            game.set_win(False)
            print("You don't have the key!")
        

class Player(Entity):
    """
    Entity of the controllable board piece

    """
    def __init__(self, move_count):
        """
        sets the move count and creates item list.

        Parameters:
            int(move_count)
        
        """  
        self._moves=move_count
        self._items=[]
        
    def get_id(self):
        """
        Returns ID of the Entity .

        Returns:
            String of Entity ID    
        """  
        return str(PLAYER)

    def get_name(self):
        """
        Returns name of the Entity.

        Returns:
            String of Entity name
        """ 
        return str('Player')

    def set_position(self, position):
        """
        Sets the position of the player.

        Parameters:
            int(x,y)
        """ 
        self._position=position

    def get_position(self):
        """
        Gets the position of the player.

        Returns:
            position of the player if present.
            
        """ 
        try:
            return self._position
        except:
            return None

    def change_move_count(self, number):
        """
        Changes the players move count by added means

        Parameters:
            int(number)
            
        """ 
        self._moves+=number

    def moves_remaining(self):
        """
        Returns the players move count

        Returns:
            int(moves)
            
        """ 
        return self._moves

    def add_item(self, item):
        """
        Adds said item into players inventory
            
        """ 
        self._items.append(item)

    def get_inventory(self):
        """
        Returns the players items in inventory

        Returns:
            list(items)
            
        """ 
        return self._items


class GameLogic:
    """
    Contains all the information on the game with class functions from
    entity being used.
        
    """ 
    def __init__(self, dungeon_name="game1.txt"):
        """Constructor of the GameLogic class.

        Parameters:
            dungeon_name (str): The name of the level.
        """
        self._moves=GAME_LEVELS[dungeon_name]
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)

        #you need to implement the Player class first.
        self._player = Player(GAME_LEVELS[dungeon_name])

        #you need to implement the init_game_information() method for this.
        self._game_information = self.init_game_information()

        self._win = False

    def get_positions(self, entity):
        """ Returns a list of tuples containing all positions of a given Entity
             type.

        Parameters:
            entity (str): the id of an entity.

        Returns:
            )list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))

        return positions

    def get_dungeon_size(self):
        """
        Returns the players items in inventory

        Returns:
            int(dungeon width)
            
        """ 
        return self._dungeon_size

    def init_game_information(self):
        """
        Returns the position with corresponding Entity and sets position of
        player entity.

        Returns:
            dict((x,y):Entity.__str__(),)
            
        """ 
        self.game_information={}
        
        position=(self.get_positions(PLAYER)[0])
        self._player.set_position(position)
        #Goes through the dungeon layour and finds the correspoding entity.
        for pos in self.get_positions(KEY):
            self.game_information[pos]=Key()
        for pos in self.get_positions(DOOR):
            self.game_information[pos]=Door()
        for pos in self.get_positions(WALL):
            self.game_information[pos]=Wall()
        try:
            for pos in self.get_positions(MOVE_INCREASE):
                self.game_information[pos]=MoveIncrease(5)
        except:
            None
        return self.game_information


    def get_game_information(self):
        """
        Returns the game layout information

        Returns:
            dict((x,y):Entity.__str__(),)
            
        """ 
        return self._game_information

    def get_player(self):
        """
        Returns player within the game

        Returns:
            Player().__str__()
            
        """ 
        return self._player

    def get_entity(self,position):
        """
        Returns the Entity in entered position.

        Parameters:
            int(position)

        Returns:
            Entity subclass type
            
        """ 
        if position in self._game_information:
            return self._game_information[position]
        else:
            return None

    def get_entity_in_direction(self, direction):
        """
        Returns the Entity in direction of player position.

        Parameters:
            str(direction)

        Returns:
            Entity subclass type
            
        """ 
        x,y=DIRECTIONS[direction]
        x1,y1=self._player.get_position()
        position=(x+x1,y+y1)
        return self.get_entity(position)
        
    def collision_check(self, direction):
        """
        Determines whether or not Entity in direction is collidable or not.

        Parameters:
            str(direction)

        Returns:
            True or False
            
        """ 
        if str(self.get_entity_in_direction(direction)) == "Wall('#')":
            return True
        elif str(self.get_entity_in_direction(direction)) in [
            str(Key()),str(Door()),str(MoveIncrease(5))]:
            return False
        elif self.get_entity_in_direction(direction) == None:
            return False

        
    def new_position(self, direction):
        """
        Returns the new position of player in direction of player.

        Parameters:
            str(direction)

        Returns:
            int(x,y)
        """ 
        x,y=DIRECTIONS[direction]
        x1,y1=self._player.get_position()
        return (x+x1,y+y1)

    def move_player(self, direction):
        """
        Returns the new position of player in direction of player.

        Parameters:
            str(direction)
        """ 
        position=self.new_position(direction)
        self._player.set_position(position)
        return None

    def check_game_over(self):
        """
        Stays True as long as the player has 1 or more moves.

        Returns:
            True or False
        """ 
        if self._player._moves<=0:
            return True
        else:
            return False

    def set_win(self, win):
        """
        changes win state

        Parameters:
            bool(win)
        """ 
        self._win_state=bool(win)
        return None

    def won(self):
        """
        Checks the game state

        Returns:
            game state(True or False)
        """ 
        try:
            return bool(self._win_state)
        except:
            return self.check_game_over()

        

            
    
class GameApp:
    """
    Communicaater between GameLogic() and Display()
    """
    def __init__(self):
        """
        Initialises GameLogic() class into self variable
        """ 
        self._game=GameLogic()


        
    def play(self):
        """
        Handles the players interaction.
        Contains instances of GameLogic() and self.draw()
        """
        while self._game.check_game_over() == False:
            #once moves remaining is 0 the while loop ends.
            self.draw()
            action=input("Please input an action: ")
            if action in DIRECTIONS:
                self._game._player.change_move_count(-1)
                #checks whether the direction the player chose is collidable
                if self._game.collision_check(action) == True:
                    print("That's invalid.")
                    pass
                elif self._game.collision_check(action) == False:
                    #checks if the player is in an item position
                    #activating it before moving
                    if self._game.get_positions(KEY)[0]==\
                       self._game.new_position(action):
                        Key().on_hit(self._game)
                        self._game.move_player(action)
                        
                    elif self._game.get_positions(DOOR)[0]==\
                       self._game.new_position(action):
                        Door().on_hit(self._game)
                        self._game.move_player(action)
                        self._game.won()
                        if self._game.won() == True:
                            print(WIN_TEXT)
                            return None

                    elif self._game._dungeon_size >= 8:
                        #if the dungeon is higher than 8 width, that means the
                        #move increase is implemented so different if
                        #scenarios are necessary along with the old ones.
                        if self._game.get_positions(KEY)[0]==\
                           self._game.new_position(action):
                            Key().on_hit(self._game)
                            self._game.move_player(action)
                            
                        elif self._game.get_positions(DOOR)[0]==\
                           self._game.new_position(action):
                            Door().on_hit(self._game)
                            self._game.move_player(action)
                            self._game.won()
                            if self._game.won() == True:
                                print(WIN_TEXT)
                                return None
                            
                        elif self._game.get_positions(MOVE_INCREASE)[0]==\
                           self._game.new_position(action):
                            MoveIncrease().on_hit(self._game)
                            self._game.move_player(action)

                        else:
                            self._game.move_player(action)
                            pass

                            
                    else:
                        self._game.move_player(action)
                        pass
            elif action == HELP:
                print(HELP_MESSAGE.format(VALID_ACTIONS))

            elif action.split(' ')[0]==INVESTIGATE:
                if action.split(' ')[1] in DIRECTIONS:
                    self._game._player.change_move_count(-1)
                    print(self._game.get_entity_in_direction(
                        action.split(' ')[1]),'is on the {0} side.'.format(
                            action.split(' ')[1]))
                else:
                    print("That's invalid.")
                    None
            elif action == QUIT:
                option=input("Are you sure you want to quit? (y/n): ")
                if option == 'y':
                    return
                if option == 'n':
                    None
            else:
                print("That's invalid.")
                None
        print(LOSE_TEST)
         
    
    def draw(self):
        """
        Displays the dungeon entities and remaining moves
        Contains instances of GameLogic() and Display
        """
        self._draw=Display(self._game._game_information,\
                           self._game.get_dungeon_size())
        return self._draw.display_game(self._game._player.get_position()),\
               self._draw.display_moves(self._game._player.moves_remaining())
    


        

        
        



def main():
    GameApp()

if __name__ == "__main__":
    main()
