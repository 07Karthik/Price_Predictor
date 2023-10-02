# this is for to run in our local env
import os
import subprocess
_081_ = os.getcwd() + "/" + "app1.py"
subprocess.Popen(["streamlit", "run", _081_])