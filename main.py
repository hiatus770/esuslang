import os
from random import random, randrange
import time

omegasus = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# File Directories #
FolderDir = "" # change this to where you cloned the github folder 
inputFile = FolderDir + "io/input.sus"
outputFile = FolderDir + "io/output.sus"
compiled = FolderDir + "compiled.py"

def readTxt():
    with open(inputFile, "r") as ipt:
        lines = ipt.readlines() 
        return lines

# Prints out the output of compiled program # 
def printFile(dir = outputFile): 
    with open(dir, "r") as ipt:
        lines = ipt.readlines() 
        for line in lines:
            print(line, end = "")
    print()

# Compiles the code # 
def compile():
    lines = readTxt() 
    with open(compiled, "w") as final:
        newLines = list()
        for l in lines:

            l = l.replace("AMOGUS", "len")
            l = l.replace("MOGUS", "print")
            l = l.replace("IMPOSTORS", "for")
            l = l.replace("SUS?", "if")
            l = l.replace("REDcrewmate", "True")
            l = l.replace("BLUEcrewmate", "False")
            l = l.replace("SUS", "=")
            l = l.replace("VENT", "input")
            l = l.replace("MEETING", "1")
            l = l.replace("IN", "+")
            l = l.replace("LAST_SEEN", "in")
            l = l.replace("WIRES", "range")
            l = l.replace("REPORTED", "-")
            l = l.replace("TRUST", "0")
            l = l.replace("VOTED", "end")
            l = l.replace("KICKED", '""')

            newLines.append(l)

        final.writelines(newLines)

def writeSelf():
    with open(inputFile, "w") as mogus:
        lines = list()
        while True:
            line = input()
            if (line == "sussify"):
                break
            lines.append(line)
        mogus.writelines(lines)

def run():
    os.system("python3 " + compiled + " > " + outputFile)

def result():
    with open(outputFile, "r") as ipt:
        lines = ipt.readlines() 
        for l in lines:
            print(l, end = "")

def bar(a,c):
    b = "["
    for i in range (a):
        b= b + "="
    if c >= a:
        b = b + "/"
    for i in range (c-a):
        b = b + " "
    b = b + "]"
    return b

def loadBar(t, message):
    a = 0
    b = 20

    while(a <= b):
        print(chr(27) + "[2J")
        print(message, bar(a, b))
        a = a + 1
        time.sleep(t)
    print(chr(27) + "[2J")

def terminal():
    dir = "esuslang:"
    while(True):

        print(dir+os.getcwd()+"$", end=" ")
        comd = input()
        if (comd == "vent"):
            print("EXITING ESUSLANG")
            break
        elif comd == "compile":
            loadBar(0.2, "COMPILING ")
            print("COMPILED") 
            compile()
        elif comd == "run":
            loadBar(0.1, "RUNNING ")
            run()
            print("OUTPUT:")
            result()
        elif comd == "crun":
            loadBar(0.025, "COMPILING ")
            print("COMPILED") 
            compile()
            loadBar(0.1, "RUNNING ")
            print("RUNNING")
            run()
            print("OUTPUT:")
            result()
        elif comd == "sussy balls":
            print(chr(27) + "[2J")
            loadBar(0.25, "Generating SUS")
            print(omegasus)
        elif comd == "sus":
            writeSelf()
            compile()
            loadBar(0.05, "WRITING DATA")
            print("DONE WRITING INPUT TO COMPILED.PY")
        elif comd == "isSus":
            print(chr(27) + "[2J")
            print("COMPILED CODE")
            printFile(compiled)
        elif comd == "isSussy":
            print(chr(27) + "[2J")
            print("INPUT CODE:")
            printFile(inputFile)
        elif comd == "help":
            help = """
            vent: exit program
            compile: write to compiled.py
            run: runs program with output
            crun: compiles then runs
            sussy balls: generates a sussy image
            sus: write ur own code for input through terminal interaction, to stop writing code type "sussify" and hit enter
            isSus: view the current compiled
            isSussy: view the current input.sus
            """
        else: 
            os.system(comd)

# Terminal() # 
terminal()

# # ## DOCUMENTATION??!?! # # #

        # AMOGUS len
        # MOGUS print
        # IMPOSTORS for
        # SUS? if
        # REDcrewmate True
        # BLUEcrewmate False
        # IN +
        # LAST_SEEN in
        # WIRES range
        # REPORT -
        # TRUST 0
        # VOTED end
        # KICKED ""
        # MEETING 1
        # SUS =
        # VENT input