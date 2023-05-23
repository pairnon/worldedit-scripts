from dotenv import load_dotenv
import os
import mcrcon

class Server:

    load_dotenv()

    IP = os.getenv("IP")
    RCON_PASS = os.getenv("RCON_PASS")
    RCON_PORT = os.getenv("RCON_PORT")

    server_ip = IP
    rcon_password = RCON_PASS
    rcon_port = int(RCON_PORT)

    tls_mode = 0
    timeout = 20

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

class Pos:

    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_dcoords(self, dx, dy, dz):
        return "{x_coord},{y_coord},{z_coord}".format(x_coord=self.x+dx, y_coord=self.y+dy, z_coord=self.z+dz)
    
    def get_coords(self):
        return "{x_coord},{y_coord},{z_coord}".format(x_coord=self.x, y_coord=self.y, z_coord=self.z)
    
class Command:

    server = Server()

    def __init__(self):
        pass

    def pos1(self, pos):
        self.server.exec("//pos1 {pos}".format(pos=pos.get_coords()))

    def pos2(self, pos):
        self.server.exec("//pos2 {pos}".format(pos=pos.get_coords()))

    def d_pos1(self, pos, dx, dy, dz):
        self.server.exec("//pos1 {pos}".format(pos=pos.get_dcoords(dx, dy, dz)))

    def d_pos2(self, pos, dx, dy, dz):
        self.server.exec("//pos2 {pos}".format(pos=pos.get_dcoords(dx, dy, dz)))

    def world(self, world):
        self.server.exec("//world {world}".format(world=world))

    def set(self, pattern):
        self.server.exec("//set {pattern}".format(pattern=pattern))

    def say(self, arg):
        self.server.exec("/say {arg}".format(arg=arg))