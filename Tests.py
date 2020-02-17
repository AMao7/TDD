from car_factory import *

Test1 = print('Should print out shiny parts\n', make_parts('labour', 'metal'))
print(make_parts('labour', 'metal') == 'shiny parts')
Test2 = print('Should print out car made\n', build_car('shiny parts'))
print(build_car('shiny parts') == 'car made')