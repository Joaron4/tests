OK_FORMAT = True

test = {   'name': 'q0_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> w = [2, 6, 3, 3]\n'
                                               '>>> v = [1, 5, 3, 3]\n'
                                               ">>> assert mochila(w, v, 6) == 6,'el máximo peso que puedes tomar es 6'\n"
                                               '>>> assert mochila(w, v, 10) == 8\n'
                                               ">>> assert mochila(w, v, 0) == 0 ,'si no tienes espacio en la mochila no puedes robar nada, piensa en el caso base'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
