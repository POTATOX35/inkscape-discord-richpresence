def find(list, item):
    output = []
    for element in list:
        if (element.find("item") >= 0):
            output.append(element)
    return output

deneme=[
    "patates",
    "patatesi severiz"
    "ekmek arası patates"
    "patats kötü",
    "lahmacun pattissiz gitmez"
]

print(find(deneme, "patates"))