# print("Hello world")
# for i in range(7):
#     print("#"*i)
# for i in range(8):

#     for i in range(8):
#         print("*",end=" ")
#     print("\n")
def greet(first_name, last_name):
    greeting = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '!'
    return greeting

# Replace with your first and last name.
# That is, unless your name is already James Bond.
print(greet("James","Bond"))