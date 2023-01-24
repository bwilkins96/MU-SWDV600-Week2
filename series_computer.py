# A program that calculates the total score of three games

def series_computer():
    score = 0
    
    for i in range(1, 4):
        game_score = int(input(f'Enter the score for game {i}: '))
        score += game_score
        
    print(f'\nYour total score was {score}!')

series_computer()
