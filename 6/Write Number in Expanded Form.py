def expanded_form(num):
    x = list(str(num))
    lenght = len(x)
    ls = []
    for _ in range(lenght):
        d = x.pop(0)
        if d != "0":
            ls.append(d + "0" * len(x))

    return " + ".join(ls)


print(expanded_form(70304))