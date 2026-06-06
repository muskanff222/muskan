# # guess the number game part 2
# random =__import__("random");
# a=random.randint(1,500);
# print("Welcome to the Guess the Number Game!");
# count=0;
# for b in range(5):
#     num=int(input("Guess the number between 1 to 500: "));
#     count=count+1;
#     if num>a:
#         print("Too high! Try again.");
#     elif num<a:
#         print("Too low! Try again.");
#     elif num==a:
#         print("Congratulations! You guessed the number correctly: ",a);
#         print("You guessed the number in ",count," attempts.");
#         break;  
#     else:   
#         print("Game Over! The correct number was: ",a);
# print("if you want to play again press 1 else press 0");
# play_again=int(input("Enter your choice: "));
# if play_again==1:
#     a=random.randint(1,5000);
#     print("Welcome to the Guess the Number Game!");
#     num=int(input("Guess the number between 1 to 5000: "));
#     count=0;
#     for b in range(5):
#         num=int(input("Guess the number between 1 to 5000: "));
#         count=count+1;
#         if num>a:
#             print("Too high! Try again.");
#         elif num<a:
#             print("Too low! Try again.");
#         elif num==a:
#             print("Congratulations! You guessed the number correctly: ",a);
#             print("You guessed the number in ",count," attempts.");
#             break; 
#         else: 
#             print("Game Over! The correct number was: ",a);
# print("if you want to play again press 1 else press 0");
# play_again=int(input("Enter your choice: "));

# part 3 of it
random =__import__("random");
a=random.randint(1,5000);
score=0;
count=0;
print("Welcome to the Guess the Number Game!");
for b in range(5):
    num=int(input("Guess the number between 1 to 5000: "));
    count=count+1;
    if num>a:
        print("Too high! Try again.");
        score=score-1;
    elif num<a:
        print("Too low! Try again.");
        score=score-1;
    elif num==a:
        print("Congratulations! You guessed the number correctly: ",a);
        score=score+5;
        print("Your score is: ",score);
        print("You guessed the number in ",count," attempts.");
        print("your score is: ",score);
        break; 
print("Game Over! The number was: ",a);
print("if you want to play again press 1 else press 0");
play_again=int(input("Enter your choice: "));
if play_again==1:
    a=random.randint(1,10000);
score=0;
count=0;
print("Welcome to the Guess the Number Game!");
print("your previous score is: ",score);
for b in range(5):
    num=int(input("Guess the number between 1 to 10000: "));
    count=count+1;
    if num>a:
        print("Too high! Try again.");
        score=score-1;
    elif num<a:
        print("Too low! Try again.");
        score=score-1;
    elif num==a:
        print("Congratulations! You guessed the number correctly: ",a);
        score=score+5;
        print("Your score is: ",score);
        print("You guessed the number in ",count," attempts.");
        print("your score is: ",score);
        break;
print("Game Over! The number was: ",a);
print("if you want to play again press 1 else press 0");
play_again=int(input("Enter your choice: "));
if play_again==1:
    a=random.randint(1,5000);
score=0;
count=0;
print("Welcome to the Guess the Number Game!");
print("your previous score is: ",score);
for b in range(5):
    num=int(input("Guess the number between 1 to 5000: "));
    count=count+1;
    if num>a:
        print("Too high! Try again.");
        score=score-1;
    elif num<a:
        print("Too low! Try again.");
        score=score-1;
    elif num==a:
        print("Congratulations! You guessed the number correctly: ",a);
        score=score+5;
        print("Your score is: ",score);
        print("You guessed the number in ",count," attempts.");
        print("your score is: ",score);
        break;
print("Game Over! The number was: ",a);
print("if you want to play again press 1 else press 0");
play_again=int(input("Enter your choice: "));   
if play_again==1:
    a=random.randint(1,10000);

