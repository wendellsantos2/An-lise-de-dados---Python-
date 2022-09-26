from controller.CepController import CepController
from model.DbUtil import DbUtil
 
class Main():
    
    def __init__(self):
        Main.menu_de_leitura()
         
    @staticmethod
    def menu_de_leitura():
        CepController.menu()
    
if __name__ == "__main__":
    app = Main()
                