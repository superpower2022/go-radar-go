import re
dir = "RM_Client_UI.py"
with open(dir, 'rt') as f:
    s = f.read()
with open(dir, 'wt') as f:
    f.write(re.sub(r"\[String", "[c_char_p", s))
    
