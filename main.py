import random
import time

def create_deck():
    cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
    random.shuffle(cards)
    return cards

def display_board(board, revealed):
    for i in range(len(board)):
        if revealed[i]:
            print(f"[{board[i]}]", end=" ")
        else:
            print("[*]", end=" ")
    print()

def check_match(board, revealed, first, second):
    return board[first] == board[second]

def play_game():
    deck = create_deck()
    revealed = [False] * len(deck)
    attempts = 0
    pairs_found = 0
    time_limit = 60
    start_time = time.time()

    while pairs_found < len(deck) // 2:
        display_board(deck, revealed)
        print(f"Time left: {max(0, time_limit - int(time.time() - start_time))} seconds")
        
        if time.time() - start_time > time_limit:
            print("Time's up! Game over.")
            break

        try:
            first = int(input("Choose the first card (0-15): "))
            second = int(input("Choose the second card (0-15): "))
            
            if revealed[first] or revealed[second]:
                print("One or both cards are already revealed. Try again.")
                continue
            
            revealed[first] = True
            revealed[second] = True
            attempts += 1
            
            if check_match(deck, revealed, first, second):
                print("It's a match!")
                pairs_found += 1
            else:
                print("Not a match. Try again.")
                revealed[first] = False
                revealed[second] = False
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 15.")

    if pairs_found == len(deck) // 2:
        print("Congratulations! You've matched all pairs!")
    display_board(deck, revealed)

if __name__ == "__main__":
    play_game()
