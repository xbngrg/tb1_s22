"""§1 FUNCTIONS"""

"""§1.1 Function syntax"""

def hello_world():
    """Prints 'Hello, world!', each time on a new line."""
    print("Hello, world!\n")  # \n is the newline character.


"""
Every function definition begins with the keyword 'def', followed by the name
you wish to give the function. Function names are written in lower_case
(no spaces!), e.g. function1 or hello_world. The name is followed by a pair of
brackets (see §1.3). The first line of the function ends with a colon. This is
the result (the description is not obligatory):
"""

def function():
    """Does nothing."""
    pass


"""§1.1.1 Indentation"""

"""In Python, indentation is used to determine the structure of code.
Every indentation level is somehow conditioned by the level(s) above."""

# 1st level: no indentation, the "main" block of the code;

def hello_range():
    """Prints "Hello again, world!" 3 times and "Goodbye, world!" once."""
    for i in range(0, 3):  # 2nd level: 4 spaces
        print("Hello again, world!\n")  # 3rd level: 8 spaces, and so on.
    print("Goodbye, world!\n")  # L2, outside of for-loop, still in function
# 1st level again, function ends here!


hello_range()  # code nested within function -> runs only at function call

"""
The lines belonging to the function are indented at least once (4 spaces or 1
tab right).  In our example, 'print("Hello, world!")' is nested inside
of 'for i in range(0, 3):', which stands for "do the nested action(s) 3 times".
Therefore, "Hello again, world!" will be printed 3 times. On the contrary, since
'print("Goodbye, world!")' is not nested within the 'for'-loop, "Goodbye, world!"
will only be printed once. Furthermore, all this code is nested within a function,
which means that it will only run when we call the function with 'hello_range()'.
Functions can be called on any indentation level.
"""

"""§1.1.1.1 Ending a function"""

def f():  # function 'f' begins here
    def g():  # function 'g' begins here
        return 1
    return g  # function 'g' ends here (nothing to do w/ the 'return' keyword)
# functions 'f' ends here


"""
As a rule of thumb, a function ends when the interpreter reaches the first
line that is at the same indent level as the 'def' keyword opening the function.
In other programming languages, code blocks are evidentiated by curly brackets.
Here is the same code, written in JavaScript, if you're curious ;)

function f(){               # opens 'f'
    function g(){           # opens 'g'
        return 1;
    }                       # closes 'g'
    return g();
}                           # closes 'f'

This might seem unnecessarily complicated for now, but it's actually a vital
part of code's logic, as you'll learn along the way.
"""

"""§1.1.1.2 Bad Indentation"""


def bad_indentation(n):
    """Prints integers between 0 and n-1, then prints n."""
for i in range(0, n):
    print(i)
        print(n)


bad_indentation(3)

"""
This programmer is well-intentioned but the program exits with an IndentationError.
The interpreter stops at the line where it finds the error and reads no further.
See if you can correct this code. The output should be:

0
1
2
3
"""


"""§1.1.2 Parameters"""


def hello_params(n, m):
    """Prints "Hello, world!" 'n' times, then returns 'm'."""
    print("Hello, world!\n" * n)
    return m


"""
Functions can be assigned any number of parameters. Parameters are defined inside
of the brakets between the function name and the colon at the end of the line.
They can fulfill various roles within the function.

In the example above, the parameter 'n' determines how many times "Hello, world!"
is printed, while the parameter 'm' is simply "returned" at the end of the function.
Parameters are placeholders for other values. They are are "passed" at "function
call" as "arguments" - the following sections explain what that means.
"""


"""§1.1.3 The Function Call"""


hello_world  # -> <function 'hello_world' at some memory address>
hello_world()  # -> "Hello, world!"


"""
'Calling' a function is what we do when we wish to run the code inside said function.
The function is called using a pair of brackets '()' after the function name.
Leaving out the brackets will only return a reference to the function's address in
memory.
"""


"""§1.1.4 Arguments"""

hello_params(3, 1)  # n = 3, m = 1


"""
If a function has any parameters, the interpreter expects these to be fulfilled
at function call. This is achieved by calling the function with the corresponding
'arguments' inside of the brackets, also known as 'passing' them. The arguments
then take the place of the parameters as the function is run.

One must pass as many arguments as there are parameters. It is not possible to
pass arguments to functions that have no parameters; conversely, it is also not
possible to call a function that has parameters without passing all appropriate
arguments.

In the example above, the function 'hello_params' has two parameters, the first
being 'n' and the second being 'm'. At function call, it is necessary to pass
two arguments, the first of which will take the place of 'n', and the second,
the place of 'm'.

Calling a function with an incorrect number (and sometimes order) of arguments
will cause the program to exit with an error (your code will not run!).
"""


"""§1.1.5 The 'return' keyword"""

def multiply(n, m):
    """Multiplies n by m."""
    p = 1
    return n * m


result = multiply(2, 5)  # result == 10


"""
Function calls always produce some output: this is what the function "returns".
The return value of a function substitutes the function call at runtime: this
means that every function is a "placeholder" for its own return value; in the
example above, 'multiply(2, 5)' is a placeholder for '2 * 5'. So the value of
'result' is not the function 'multiply' itself, but only its output given
'n == 2' and 'm == 5'.

The 'return' keyword tells the interpreter which values to output at the end of
a function call. Note that the function 'multiply' contains a variable 'p' which
is not returned. This variable exists only inside the limited, "local scope" of
'multiply' - it is not known to the rest of the code.
"""


"""§1.1.5.2 Functions as arguments"""

def multiply(n, m):
    """Multiplies n by m."""
    return n * m


def square(x):
    """Squares 'x'."""
    return x ** 2


result = square(multiply(2, 5))

"""
What happens when we pass a function as an argument to another? Let's take the
example of 'result = square(multiply(2, 5))'.

tl;dr:
result = square(multiply(2, 5))  # What is 'multiply(2, 5)'?
result = square(10)  # What is 'square(10)'?
result = 100  # Done!


Explanation:
First, the interpreter reaches the variable instantiation 'result =', at which point
it knows that a value is being assigned a name, but it does not know what the value is.
This value is on the right-hand side, namely 'square(multiply(2, 5))'. In other
words, the value of 'result' will be 'square(multiply(2, 5))'. At the moment, this
is an ambiguous value - the job of the interpreter is to calculate the result of
the two functions in order to produce the final value of 'result'.

The first function call is 'square()', which takes one parameter 'x'. The value of
'x' will be 'multiply(2, 5)', which is itself a function call with '2' and '5'
standing for the paramters 'n' and 'm'. This means: We need to know what the return
value of 'multiply(2, 5)' is before we can calculate 'square(multiply(2, 5))'.

Since the return value of 'multiply' is 'n * m', the value of 'multiply(2, 5)' is
10. If 'multiply(2, 5)' returns 10, the value of the argument 'x' in the function call
of 'square' will be 10. Therefore, the next function call will be 'square(10)'.
Ultimately, the value of 'result' will be 'square(10)'. The return value of 'square'
is 'x ** 2', here 100. The final value of 'result' is 100.
"""
