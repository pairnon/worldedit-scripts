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

rcon = mcrcon.MCRcon(server_ip, rcon_password, rcon_port)

rcon.connect()

command = "time set day"
response = rcon.command(command)
print(response) # Print the server's response

rcon.disconnect()