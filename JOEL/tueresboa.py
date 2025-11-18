def tueresboa():
    lletraA = {'X' 'X' 'X' 'X' '.'
               'X' '.' '.' '.' 'X'
               'X' 'X' 'X' 'X' '.'
               'X' '.' '.' '.' 'X'
               'X' 'X' 'X' 'X' '.'
               }

    lletraB = {'.' 'X' 'X' 'X' '.' 
               'X' '.' '.' '.' 'X'
               'X' 'X' 'X' 'X' 'X'
               'X' '.' '.' '.' 'X'
               'X' '.' '.' '.' 'X'
    }

    buit = {'.' '.' '.' '.' '.'
            '.' '.' '.' '.' '.'
            '.' '.' '.' '.' '.'
            '.' '.' '.' '.' '.'
            '.' '.' '.' '.' '.'}


    matriu = [5]
    for i in range(len(matriu)):
        for j in range(matriu[i]):
            print("*" * matriu[i])

tueresboa()