import cx_Freeze
import sys
import os
#os.environ['TCL_LIBRARY'] = r'C:\\ProgramData\\Anaconda3\\envs\\ch2_venv\\tcl\\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\\ProgramData\\Anaconda3\\envs\\ch2_venv\\tcl\\tk8.6'
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
import time
base = None

#if sys.platform =='win32':
#    base="Win32GUI"


executabl=[cx_Freeze.Executable("function_dynamic_hedging_strategy.py",base=base)]
os.environ['TCL_LIBRARY'] = r'C:\Python\Python38\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python\Python38\tcl\tk8.6'

cx_Freeze.setup(name="dynamic_hedging",
    options={"build_exe": {
    "includes":["tkinter","pandas","numpy","datetime","openpyxl","openpyxl.utils.dataframe","os","tkinter.filedialog","sys","time"],
           'include_files': [r"C:\Python\Python38\DLLs\tcl86t.dll",
                             r"C:\Python\Python38\DLLs\tk86t.dll"]
       }},
    version="0.1",
    description="Dynamic hedging model for dutch gas market",
    executables=executabl
)
