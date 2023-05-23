from dotenv import load_dotenv
import os
import mcrcon

class Ws:

    load_dotenv()

    IP = os.getenv("IP")
    RCON_PASS = os.getenv("RCON_PASS")
    RCON_PORT = os.getenv("RCON_PORT")

    server_ip = IP
    rcon_password = RCON_PASS
    rcon_port = int(RCON_PORT)

    tls_mode = 0
    timeout = 10

    rcon = mcrcon.MCRcon(server_ip, rcon_password, rcon_port, tls_mode, timeout)

    operation_counter = 0

    def __init__(self):
        if(self.check_worldedit() == False):
            print("ERROR: WorldEdit not present on selected server")
        else:
            print("successfully found server with WorldEdit")

    def get_operations(self):
        return self.operation_counter
    
    def exec(self, command):
        if(command[0:1:] != "/"):
            print("ERROR: command must start with '/'")
            return
        self.rcon.connect()
        response = self.rcon.command(command[1::])
        print(response) # Print the server's response

    def check_worldedit(self):
        self.rcon.connect()
        response = self.rcon.command("plugins").lower()
        if("worldedit" in response):
            return True
        else:
            return False

    def exit(self):
        self.rcon.disconnect()