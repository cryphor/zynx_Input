from re import X
import requests
import time
import random
import string

console.clear()

banner = """
  ____  _   _ ____  _____ ____  _   _    __        __         _     ____  _   _ 
 / ___|| | | |  _ \| ____|  _ \| | | |   \ \      / /__  _ __| | __/ ___|| | | |
 \___ \| |_| | |_) |  _| | |_) | |_| |    \ \ /\ / / _ \| '__| |/ /\___ \| |_| |
  ___) |  _  |  __/| |___|  __/|  _  |     \ V  V / (_) | |  |   <  ___) |  _  |
 |____/|_| |_|_|   |_____|_|   |_| |_|      \_/\_/ \___/|_|  |_|\_\|____/|_| |_|
                                                                                    
"""
print(banner)

x = {x: f"{x}. View Offsets" for x in range(1, 2)}

input(f"[$] Choose: ")


if x == "1":
    print(requests.get("https://offsets.ntgetwritewatch.workers.dev/offsets.hpp").text)