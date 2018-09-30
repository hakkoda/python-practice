import test
#import lib.rock
from lib.rock import Rock as ROCK

my_test = test.Test("fun stuff")
my_test.say_phrase()

#my_rock = lib.rock.Rock()
#my_rock = Rock()
my_rock = ROCK()
my_rock.say_phrase()
