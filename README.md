# 2clever

## Overview
2clever is a python program that interfaces with cleverbot. It includes 3 python files:
  1. 2cleverchat.py
  2. cleverchat.py
  3. cleverbot_io.py

#### 2cleverchat.py
Makes two cleverbots talk to eachother.

#### cleverchat.py
Allows you to chat with a cleverbot.

#### cleverbot_io.py
A python module that allows you to talk with a cleverbot. It uses [cleverbot.io](cleverbot.io). Some example code:
```python
bot = Cleverbot()
response = bot.say("Never gonna give you up")
print(response) # Probably "Never gonna let you down"
```

## Dependencies
All files require:
*   Python 3.X

2cleverchat.py and cleverchat.py require:
*   Tcl/Tk libraries (Linux/Mac OSX)
