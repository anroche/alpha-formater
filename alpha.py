def layout_generator(str, color):
    special_chars = {
        "?": "-question",
        "!": "-exclamation",
        "@": "-at",
        "#": "-hash"
    }
    ret = ""
    for c in str:
        if c in special_chars:
            ret += f":{color}{special_chars[c]}:"
        elif c == " ":
            ret += "    "
        else:
            ret += f":{color}-" + c + ":"
    return ret


str = input("Veuillez entrer une chaîne de caractères : ")
color = input("Veuillez entrer la couleur d'alphabet (white ou yellow) : ")

if color == "white" or color == "yellow":
    ret = layout_generator(str, f"alphabet-{color}")
    print("Chaîne de caractères formatée : \033[31m", ret, "\033[0m")
else:
    print("Couleur d'alphabet non valide.")

