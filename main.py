from random import randint

# Emoji representations for Rock, Paper, and Scissors
ROCK = "👊"
PAPER = "✋"
SCISSORS = "✌️"

# list of play options
t = ["rock", "paper", "scissors"]

# Counter for the number of chances
chances = 0

# Counter for the number of wins
wins = 0

# Counter for the number of ties
ties = 0
#counter for the number of loss
loss = 0

while chances < 5:
    # Assign a random play to the computer
    computer_move = t[randint(0, 2)]

    # Get player's move
    player_move = input(f"\nRock {ROCK}  Paper {PAPER} Scissors {SCISSORS} ? (Type 'exit' to quit): ").lower()
    print("Chances Left", 4 - chances)

    # Check if player wants to exit
    if player_move == "exit":
        break

    # Check if player's move is valid
    if player_move not in t:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue

    # Increment the number of chances
    chances += 1

    # Function to convert player's move to emoji representation
    def get_emoji(move):
        if move == "rock":
            return ROCK
        elif move == "paper":
            return PAPER
        elif move == "scissors":
            return SCISSORS

    print("Player:", get_emoji(player_move))
    print("Computer:", get_emoji(computer_move))

    # Check for a tie
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    # Check for winning conditions
    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or
        (player_move == "scissors" and computer_move == "paper")
    ):
        print("Player wins!")
        wins += 1
    # Player loses
    else:
      print("Computer wins!")
      loss += 1
      

# Print the final results
print("\nGame Over!")
if wins > loss:
  print('🎉 😎 Player Wins   🎉 ')
  print(f'Computer {loss} Win(s)')
  print(f'Player {wins} win(s)')
  print(f'Tie(s) {ties}')
elif wins < loss:
  print('🎉  🤖 Computer Wins  🎉')
  print(f'Computer {loss} Win(s)')
  print(f'Player {wins} Win(s)')
  print(f'Tie(s) {ties}')
else:
  print("😢 Tie")
  print(f'Computer {loss} Win(s)')
  print(f'Player {wins} Win(s)')
  print(f'Tie(s) {ties}')
  
# print("Wins:", wins)
# print("Ties:", ties)
# print("Losses:", chances - wins - ties)
