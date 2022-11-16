OK_FORMAT = True

test = {   'name': 'q0_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert mario_maneras(' P P ') == 1  \n"
                                               ">>> assert mario_maneras(' P P  ')   == 1\n"
                                               ">>> assert mario_maneras('   P P ') == 2\n"
                                               ">>> assert mario_maneras(' P PP ') == 0 , 'Mario no puede saltar dos platas. Game Over 😢'\n"
                                               ">>> assert mario_maneras('   P    P P   P  P P    P     P ') == 180\n"
                                               ">>> assert mario_maneras('    P    ') == 9\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
