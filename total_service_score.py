# A program that prompts a user for x days of scores and returns the total of those scores

def main():
    days = int(input('How many days of scores? '))

    total_score = 0
    for day in range(1, days+1):
        score = int(input(f'Enter score for day {day}: '))
        total_score += score
    
    print('\nThe total score of the', days, 'days is', total_score)

main()