# Error handling in python. In python we can handle errors using error handling techniques

def total(num1, num2):
    # an error handling template includes the try & except block to try the statements given in the try block and throw any errors if present in the
    # except block.
    try:
        return (num1/num2)
    # the error which might be faced can be included in the except by specifying it, or just giving the except keyword without naming the error,
    # is used overall no matter what the error is.
    except (TypeError, ZeroDivisionError) as err:
        print(f'Error while calculating total \n{err}')


print(total(10, 2))
print('=============================================')


def new_error():
    # The while loop ensures that the loop keeps running till the else condition is reached and it breaks out of the loop till the try and except dont pass
    while True:
        # The try block takes in the logic and returns the output. Any error faced during this is handled by the 2 except blocks. It is good to know
        # the kinds of errors in our code and handle the exceptions accordingly.
        try:
            age = int(input('Kindly enter your age : '))
            print(f'{10/age}')
            # The raise error_type() can be used to raise error instead of except block
            # raise ValueError('Hi, i am a modified version of the value error for demo purposes.')
        # If there is a Value Error, then that is handled by this except block
        except ValueError:
            print('Please enter a number')
        # If there is a Zero Division Error, then that is handled by this except block
        except ZeroDivisionError:
            print('Cannot divide by 0')
        # If neither the try nor except blocks get executed, then the else is executed and the break in the block, breaks the loop
        else:
            print('Thank you, I am now breaking the loop')
            break
        # The finally statement is executed as part of the try and except block, no matter that the output is or the code is. If there is an error,
        # then finally is executed. and even if there is no error, finally is executed. Even after the while loop breaks in the else block above,
        # the finally statement is executed and then the loop is broken. Finally can be used to print and save logs, no matter the response of the code.
        finally:
            print('This is the finally block and i will be printed no matter what')


new_error()
