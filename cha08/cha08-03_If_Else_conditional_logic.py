grade = 40
if grade >= 70:
    print("You passed the class!")

if grade < 70:
    print("You did NOT pass the class :(")

print("Thank you for attending.")

# Using 'else:':
grade = 85
if grade >= 70:
    print("You passed the class!")
else:
    print("You did NOT pass the class :(")
print("Thank you for attending")

# Using 'elif'
grade = 96
if grade >= 90:
    print("You passed the class with an A.")
elif grade >= 80:
    print("You passed the class with a B")
elif grade >= 70:
    print("You passed the class with a C")
else:
    print("YOu did NOT pass the class :(")
print("thank you for attending.")

# 12ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss12
# Using nested if statments:
# below, three vesions of a program that simulate detemine the player that is the
# winner of a baskeball or golf game based on the score provisioned:
sport = input("Enter sport: ")
player_1_score = int(input("Player #1 score: "))
player_2_score = int(input("Player #2 score: "))

# version 1:
if sport.lower() == "basketball":
    if player_1_score == player_2_score:
        print(
            f"version 1: The {sport} game is a draw, both players have same score: \
{player_1_score}"
        )
    elif player_1_score > player_2_score:
        print(
            f"version 1: Player #1 is the winner of the {sport} game!!!!!! \
 {player_1_score} to {player_2_score}"
        )
    else:
        print(
            f"version 1: Player #2 is the winner of the {sport} game!!!!!! \
{player_2_score} to {player_1_score}."
        )
elif sport.lower() == "golf":
    if player_1_score < player_2_score:
        print(
            f"version 1: Player #1 is the winner of the {sport} game!! \
 {player_1_score} to {player_2_score}."
        )
    elif player_2_score < player_1_score:
        print(
            f"version 1: Player #2 is the winner of the {sport} game!! \
 {player_2_score} to {player_1_score}"
        )
    else:
        print(
            f"version 1: The {sport} game is a draw, both players have same score\
 {player_2_score} and {player_1_score}"
        )
else:
    print(f"version 1: <<<{sport}>>> is not a participating sport.")

# version 2:
if sport.lower() in ("basketball", "golf"):
    if player_1_score == player_2_score:
        print(f"** version 2: The {sport} game is a draw")
    elif sport.lower() == "basketball":
        if player_1_score > player_2_score:
            print(
                f"** version 2: Player #1 is the winner of the {sport} game! \
    {player_1_score} to {player_2_score}"
            )
        else:
            print(
                f"** version 2: Player #2 is the winner of the {sport} game! \
     {player_2_score} to {player_1_score}"
            )
    elif sport.lower() == "golf":
        if player_1_score < player_2_score:
            print(
                f"** version 2: Player #1 is the winner of the {sport} game! \
    {player_1_score} to {player_2_score}"
            )
        else:
            print(
                f"** version 2: Player #2 is the winner of the {sport} game! \
    {player_2_score} to {player_1_score}"
            )
else:
    print(f"** version 2: <<<{sport}>>> is not a participating sport")

# version # 3:
if sport.lower() in ("basketball", "golf"):
    if player_1_score == player_2_score:
        print(f"-- version 3: The {sport} game is a draw.")
    else:
        player_1_won_basketball = (
            sport.lower() == "basketball" and player_1_score > player_2_score
        )
        player_1_won_golf = sport.lower() == "golf" and player_1_score < player_2_score
        if player_1_won_basketball or player_1_won_golf:
            print(
                f"-- version 3: Player #1 is the winner of the {sport} game\
 {player_1_score} to {player_2_score}"
            )
        else:
            print(
                f"-- version 3: Player #2 is the winner of the {sport} game\
 {player_2_score} to {player_1_score}"
            )
else:
    print(f"-- version 3: <<<{sport}>>> is not a participating sport")
