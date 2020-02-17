from car_factory import *
while True:
    Help = input('Press 1 to build a car or 2 to test').strip()
    if Help == '1':
        first_stage = input("What is the car made out of ? ").strip()
        second_stage = input("What is the second thing the car is made out of ? ").strip()
        newest_car = make_parts(first_stage, second_stage)
        newest_car1 = build_car(newest_car)
        print(run_factory(newest_car, first_stage, second_stage))


    elif Help == '2':
        Test1 = print('Should print out shiny parts\n', make_parts('labour', 'metal'))
        print(newest_car == 'shiny parts')
        Test2 = print('Should print out car made\n', build_car('shiny parts'))
        print(newest_car1 == 'car made')

    else:
        'Incorrect input, please try again'