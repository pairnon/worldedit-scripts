from dotenv import load_dotenv
import os
import mcrcon

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

rcon.connect()

def check_worldedit():
    response = rcon.command("plugins").lower()
    if("worldedit" in response):
        return True
    else:
        return False

def exec(command):
    if(command[0:1:] != "/"):
        print("error: command must start with '/'")
        return
    response = rcon.command(command[1::])
    print(response) # Print the server's response

def exit():
    rcon.disconnect()