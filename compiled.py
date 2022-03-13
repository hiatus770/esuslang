CREWMATE = input()
for AMONG_US in range(len(CREWMATE), 0, - 1):
    print(CREWMATE[AMONG_US -1], end = "")
print("")
if CREWMATE == "sus":
    print("sus check?")