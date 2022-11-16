OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> podar_abajo(t)\n'
                                               '>>> assert str(t) == str(Tree(5, [Tree(4, [Tree(3), Tree(4), Tree(5)])]))\n'
                                               ">>> assert id(t) == id(b),'Recuerda que estas mutando un árbol, no tienes que reemplazarlo' \n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
