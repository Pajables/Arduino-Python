import time
import logging
from commanduino import CommandManager

logging.basicConfig(level=logging.INFO)


cmdMng = CommandManager.from_configfile('B:/UJ/Postgrad/Chemputer/Arduino-Python/commanduino-master/examples/commanddevices/commanddigitalread/demo.json')


for i in range(300):
    print(cmdMng.D1.get_state())
    time.sleep(1)
