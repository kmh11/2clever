import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( name = "2clever",
       version = "0.1",
       description = "A progam for making 2 cleverbots talk to eachother",
       executables = [Executable("2cleverchat.py", base=base)])
