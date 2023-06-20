                elif self._game.collision_check(direction) == False:
                    if self._game.get_positions(KEY)==\
                       self._game.new_position(direction):
                        self._game._key.on_hit(self._game)
                        self._game.move_player(direction)
                    elif self._game.get_positions(DOOR)==\
                       self._game.new_position(direction):
                        self._game._Door.on_hit(self._game)
                        self._game.move_player(direction)
                    else:
                        self._game.move_player(direction)
                        pass
