
def make_parts(args1, args2):
    if args1 == 'labour' and args2 == 'metal':
        return 'shiny parts'
    else:
        'you dont have the correct parts'

def build_car(arg):
    if arg == 'shiny parts':
        return 'car made'
    else:
        'not correct'

def run_factory(arg, args1, args2):
    built_car = make_parts(args1, args2)
    new_car1 = build_car(built_car)
    return new_car1

