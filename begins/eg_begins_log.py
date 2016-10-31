import begin
import logging


@begin.start(auto_convert=True)
@begin.logging
def run(name='Arther', quest='Holy Grail', colour='blue', *knights):
    print("tis but a scratch!")
