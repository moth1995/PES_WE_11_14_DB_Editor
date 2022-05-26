from .stat import Stat

class PlayerCallname:
    def __init__(self, player):
        self.callname = Stat(player, 1, 0, 0xFFFF, "Call Name");
    
    """
    Resta agregar algun metodo para leer los callnames desde el archivo y ademas poder editarlos
    """
    def __iter__(self):
        return iter(
            [
                self.callname,
            ]
        )
    
    def __call__(self):
        return [callname() for callname in self.__iter__()]