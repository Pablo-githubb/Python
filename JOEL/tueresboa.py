# Python
def tueresboa():
    lletraB = [
        "XXXX.\n",
        "X...X\n",
        "XXXX.\n",
        "X...X\n",
        "XXXX.\n",
    ]

    lletraA = [
        ".XXX.\n",
        "X...X\n",
        "XXXXX\n",
        "X...X\n",
        "X...X\n",
    ]

    buit = [".....\n"] * 5

    claseA = int(input())
    claseB = int(input())

    if claseA > claseB:
        print(''.join(lletraA), end='')
    elif claseB > claseA:
        print(''.join(lletraB), end='')
    else:
        print(''.join(buit), end='')

tueresboa()
