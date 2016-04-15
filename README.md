# 2clever

## Overview
2clever is a python program that interfaces with cleverbot. It includes 3 python files:
  1. 2cleverchat.py
  2. cleverchat.py
  3. clever.py

#### 2cleverchat.py
Makes two cleverbots talk to eachother.

#### cleverchat.py
Allows you to chat with a cleverbot.

#### clever.py
A python module that allows you to talk with a cleverbot. Some example code:
```python
cleverbot = mkbot()
response = cleverbot.say("Never gonna give you up")
print(response) # Probably "Never gonna let you down"
killbot() # Closes bot process
```

#### Dependencies
clever.py requires:
*   Selenium Webdriver
*   phantomjs binary
