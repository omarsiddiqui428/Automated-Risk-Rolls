#Risk to the death rolls program
#Assumption: both the attacker and defender keep rolling the max rolls that they can until there is a victor

import random

def main():
    print("Note: This program assumes a fight to the death. \nIt assumes that both the attacker and defender will keep rolling the maximum number of rolls possible until one of them is dead.")
    attacker_starting_soliders = int(input("\nAttacker, how many soliders do you have? "))
    if attacker_starting_soliders < 2:
        exit("Attacker does not have enough soldiers to attack.")
    defender_starting_soliders = int(input("Defender, how many soldiers do you have? "))
    if defender_starting_soliders < 1:
        exit("Defender does not have enough soldiers to defend.")

    attacker_starting_rolls = attacker_starting_soliders - 1
    attacker_current_rolls = attacker_starting_rolls
    defender_current_rolls = defender_starting_soliders
    attacker_wins = 0
    defender_wins = 0

    while defender_current_rolls and attacker_current_rolls != 0:
        if defender_current_rolls >= 2:
            sorted_defender_array = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)

            if attacker_current_rolls >= 3:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
                for i in [0,1]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -=1
                    else: #sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

            if attacker_current_rolls == 2:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)
                for i in [0, 1]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1
                    else:  # sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

            if attacker_current_rolls == 1:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(1)], reverse=True)
                for i in [0]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1
                    else:  # sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

        else: #defender current_rolls == 1
            sorted_defender_array = sorted([random.randint(1, 6) for _ in range(1)], reverse=True)

            if attacker_current_rolls >= 3:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
                for i in [0, 1]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1
                    else:  # sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

            if attacker_current_rolls == 2:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)
                for i in [0, 1]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1
                    else:  # sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

            if attacker_current_rolls == 1:
                sorted_attacker_array = sorted([random.randint(1, 6) for _ in range(1)], reverse=True)
                for i in [0]:
                    if sorted_attacker_array[i] > sorted_defender_array[i]:
                        attacker_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1
                    else:  # sorted_attacker_array[i] < sorted_defender_array[i]
                        defender_wins += 1
                        attacker_current_rolls -= 1
                        defender_current_rolls -= 1

    if defender_current_rolls == 0:
        print("\nAttacker wins! Attacker has conquered a new territory")
        attacker_remaining_soliders = attacker_starting_soliders = defender_wins
        print("\nAttacker remaining soliders: " + str(attacker_remaining_soliders))
        print("Defender remaining soliders: 0")

    else: #attacker_current_rolls == 0
        print("\nDefender wins! Defender has successfully retained their terrority")
        print("\nAttacker remaining soliders: 1")
        defender_remaining_soliders = defender_starting_soliders - attacker_wins
        print("Defender remaining soliders: " + str(defender_remaining_soliders))

if __name__ == "__main__":
    main()
