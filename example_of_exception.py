"""
.. exception handling ?
Python provides a way to handle the exception so that the code can be executed without any interruption.
If we do not handle the exception, the interpreter doesn't execute all the code
that exists after the exception.
try:
except:
else
finally:"""
"""1.compile time error---worng output
Missing brackets (})
Printing the value of variable without declaring it
Missing semicolon (terminator)

2.logical error
logical errors are comes under bugs--These bugs may simply be in the test suite,

3.Which of the following is a run-time error?

A. Attempting to divide by 0.
B. Forgetting a colon at the end of a statement where one is required.
C. Forgetting to divide by 100 when printing a percentage amount.
what are the types:
A. The programmer.
B. The interpreter.
C. The computer.
D. The teacher / instructor
"""
# this program can cause zerodivision error
y = 0
print(y/0)

#In detailed we can see
try:
  a = int(input("Enter the value: "))
  print(10/a)
except ZeroDivisionError:
  print("0 can't divid by any number")
except ValueError:
  print("a is only contain numbers")
finally:
  print("Thank you")

#Type Error
try:
  s = {1, 2, 3}
  print(s[1])  #no index order in set
except TypeError:
  print("Set is not slicing")
