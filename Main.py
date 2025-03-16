import random
moves = ["Scissors", "Rock", "Paper"]

bot_move = random.choice(moves)
user_move = input("Rock, Paper, Scissors! \n")
print(f"Bot: {bot_move}")
if bot_move == "Scissors" and user_move == "Rock": print("You win!")
elif bot_move == "Rock" and user_move == "Paper": print("You win!")
elif bot_move == "Paper" and user_move == "Scissors": print("You win!")
elif bot_move == user_move: print("It's a tie!")
else: print("You lose!")