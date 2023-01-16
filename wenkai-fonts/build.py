#!/usr/bin/python3
import os
import shlex
import subprocess
import sys

font_path = ""

if sys.platform == "win32":
    font_path = r"..\fonts\ttf"
elif sys.platform == "linux" or sys.platform == "darwin":
    font_path = r"../fonts/ttf"

if not os.path.exists(font_path):
    os.makedirs(font_path)
    print(f"Created {font_path}")

for file in os.listdir("."):
    if file.endswith(".ufoz"):
        # convert ufoz to ufo
        subprocess.run(["python3", "extract_ufoz.py", file])
        subprocess.run(
            shlex.split(
                "fontmake {} --keep-overlaps --keep-direction --no-generate-GDEF --no-production-names -o ttf --output-dir {}".format(
                    file.strip("z"), font_path
                )
            )
        )
print("complete the ttf of LxgwWenKai font build")

subprocess.run(shlex.split(f"python3 fix_mono.py {font_path}"))
print("complete the fix_mono of LxgwWenKai font build")
