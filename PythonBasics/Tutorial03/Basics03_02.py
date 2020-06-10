def banner(msg, brd = '-'):
    line = brd * len(msg)
    print(line)
    print(msg)
    print(line)

banner("Testowy Napis")
banner("Inny border niż default", '@')
banner(brd=">", msg= "zmieniona kolejność parametrów")