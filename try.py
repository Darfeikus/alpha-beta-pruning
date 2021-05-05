import os
import filecmp

out = os.system("python tono.py < tc/in > out")
out2 = os.system("python main.py < tc/in > out2")

# Path of first file
file1 = "out"
  
# Path of second file
file2 = "out2"

print(filecmp.cmp("out", "out2"))

