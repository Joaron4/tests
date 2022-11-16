OK_FORMAT = True

test = {   'name': 'q0_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert acumular(add, 0, 5, identity) == 15 ,'Tal vez sería útil usar dos variables, una que guarde el resultado y otra que haga la secuencia "
                                               "descendente'\n"
                                               ">>> assert acumular(add, 11, 5, identity) == 26,'Tal vez sería útil usar dos variables, una que guarde el resultado y otra que haga la secuencia "
                                               "descendente'\n"
                                               ">>> assert acumular(add, 11, 0, identity) == 11,'Tal vez sería útil usar dos variables, una que guarde el resultado y otra que haga la secuencia "
                                               "descendente'\n"
                                               '>>> assert acumular(add, 11, 3, square) == 25\n'
                                               '>>> assert acumular(mul, 2, 3, square) == 72\n'
                                               '>>> assert acumular(lambda x, y: x + y + 1, 2, 3, square) == 19\n'
                                               '>>> assert acumular(lambda x, y: 2 * x * y, 2, 3, square) == 576\n'
                                               '>>> assert acumular(lambda x, y: (x + y) % 17, 19, 20, square) == 16\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
