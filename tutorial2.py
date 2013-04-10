import sys

message = "Your number multiplied by 2 is: "

print("Please type a number and press return: ")
input_num = int(sys.stdin.readline())
input_num = input_num * 2

print(message + str(input_num))

