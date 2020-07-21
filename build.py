import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("discordrpc-gui.py", base=base, icon="kc.ico")]

cx_Freeze.setup(
    name = "ADRPC",
    options = {"build_exe": {"packages":["tkinter","pypresence"], "include_files":["kc.ico"]}},
    version = "v1",
    description = "Advanced Discord RPC",
    executables = executables
    )
