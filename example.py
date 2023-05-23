from ws import *

ws = Ws()

ws.exec("//world world")
ws.exec("//pos1 0,0,0")
ws.exec("//pos2 100,100,100")
# ws.exec("//set tinted_glass")
# ws.exec("//set air")

ws.exit()