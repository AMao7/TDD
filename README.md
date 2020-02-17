# Brioche factory

## Unit test
Tests singular and unitary pieces of code

## Integration test
Tests code from beginning to end

## TDD- Test driven development
First write a test and then code, code the minimum amount to pass the test.

## Basics of a test
Known inputs and known outputs. All you do is an assertion.
Then you have testing frameworks that help you do this.

## __name__
Identifies where its bening called from.
If its being called directly, therefore not imported, __name__ will become main.
If its being imported it will have the file name of where it's being called from.

### Brioche factories known inputs and outputs
inputs: 
- Water
- Flour
- Eggs

outputs:
- dough

### Bake function
input:
- dough

output:

- brioche

