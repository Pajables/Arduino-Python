import time
import logging
from commanduino import CommandManager

logging.basicConfig(level=logging.INFO)

cmdMng = CommandManager.from_configfile('B:/UJ/Postgrad/Chemputer/Arduino-Python/commanduino-master/examples/commanddevices/commandanalogread/demo.json')


for i in range(300):
    print(cmdMng.A1.get_level())
    time.sleep(1)
