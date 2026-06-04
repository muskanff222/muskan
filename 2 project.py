# 2nd project 
# guess the number
random =__import__("random");
a=random.randint(1,500);
print("Welcome to the Guess the Number Game!");
num=int(input("Guess the number between 1 to 500: "));
while num!=a:
    if num<a:
        print("Too low! Try again.");
    else:
        print("Too high! Try again.");
    num=int(input("Guess the number between 1 to 100: "));
print("Congratulations! You guessed the number correctly: ",a);