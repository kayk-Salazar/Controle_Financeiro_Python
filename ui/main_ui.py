
class MainUI:
    def __init__(
        self, 
        user_ui,
        admin_ui
        ):

        self.user_ui = user_ui
        self.admin_ui = admin_ui

    def start(self):
        while True:
    
            print("\n=== BANK SYSTEM ===")
            print("1 - Usuário")
            print("2 - Administrador")
            print("0 - Sair")

            menu_of_options = {
                "1": self.user_ui.user_menu,
                "2": self.admin_ui.admin_menu,
            } 
            option = input("Escolha: ")

            if option == "0":
                break

            get = menu_of_options.get(option)

            if get:
                get()
            else:
                print("Opção Inválida no menu")




    
  
        
            