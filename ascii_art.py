class Logo:

    def __init__(self):
        self.logo = '''
     /$$      /$$                                         
    | $$$    /$$$                                         
    | $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  
    | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ 
    | $$  $$$| $$| $$  \ $$| $$  \__/|  $$$$$$ | $$$$$$$$ 
    | $$\  $ | $$| $$  | $$| $$       \____  $$| $$_____/ 
    | $$ \/  | $$|  $$$$$$/| $$       /$$$$$$$/|  $$$$$$$ 
    |__/     |__/ \______/ |__/      |_______/  \_______/ 
                                                          '''

        self.bye = '''
         /$$$$$$$                      /$$
        | $$__  $$                    | $$
        | $$  \ $$ /$$   /$$  /$$$$$$ | $$
        | $$$$$$$ | $$  | $$ /$$__  $$| $$
        | $$__  $$| $$  | $$| $$$$$$$$|__/
        | $$  \ $$| $$  | $$| $$_____/    
        | $$$$$$$/|  $$$$$$$|  $$$$$$$ /$$
        |_______/  \____  $$ \_______/|__/
                   /$$  | $$              
                  |  $$$$$$/              
                   \______/               
                     '''
    def print_logo(self):
        return print(self.logo)

    def print_bye(self):
        return print(self.bye)