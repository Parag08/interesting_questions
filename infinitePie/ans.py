pie = "314159265358979323846264"
fav_strings = ["314","15926","53589","793238","46264","314","1592653589793","23846264"]
count = 0
divided_pie = ""
i = 0

while i < len(pie):
    #select the sting to start with
    found = False
    maxlen = 0
    j = 0
    for fav_string in fav_strings:
        if (fav_string[j] == pie[i]) & (maxlen < len(fav_string)):
            found = True
            maxlen = len(fav_string)
    if (found):
        divided_pie = divided_pie +  pie[i:i+maxlen] + " "
        count = count + 1
        i = i + maxlen
    else:
        print("don't know what to do")
        break

print(count, divided_pie)
