import begin


@begin.start(env_prefix='CAMELOT_')
def run(name='Arther', quest='Holy Grail', colour='blue', *knights):
    print(name, quest)
