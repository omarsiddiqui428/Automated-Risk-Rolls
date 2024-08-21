import random

def main():
    print("Note: This program assumes a fight to the death. \nIt assumes that both the attacker and defender will keep rolling the maximum number of rolls possible until one of them is dead.")

    attacker_starting_soldiers = int(input("\nAttacker, how many soldiers do you have? "))
    if attacker_starting_soldiers < 2:
        exit("Attacker does not have enough soldiers to attack.")
    soldiers_left = int(input("Attacker, how many soliders do you want to retain if you can't win? "))

    defender_starting_soldiers = int(input("Defender, how many soldiers do you have? "))
    if defender_starting_soldiers < 1:
        exit("Defender does not have enough soldiers to defend.")

    attacker_current_soldiers = attacker_starting_soldiers
    defender_current_soldiers = defender_starting_soldiers

    while defender_current_soldiers > 0 and attacker_current_soldiers > soldiers_left:
        attacker_dice = min(3, attacker_current_soldiers - 1)
        defender_dice = min(2, defender_current_soldiers)

        attacker_rolls = sorted([random.randint(1, 6) for _ in range(attacker_dice)], reverse=True)
        defender_rolls = sorted([random.randint(1, 6) for _ in range(defender_dice)], reverse=True)

        for i in range(min(attacker_dice, defender_dice)):
            if attacker_rolls[i] > defender_rolls[i]:
                defender_current_soldiers -= 1
            else:
                attacker_current_soldiers -= 1

    if defender_current_soldiers == 0:
        print("\nAttacker wins! Attacker has conquered a new territory.")
        attacker_remaining_soldiers = attacker_current_soldiers
        print("\nAttacker remaining soldiers: " + str(attacker_remaining_soldiers))
        print("Defender remaining soldiers: 0")
    else:
        print("\nDefender wins! Defender has successfully retained their territory.")
        print("\nAttacker remaining soldiers: " + str(attacker_current_soldiers))
        print("Defender remaining soldiers: " + str(defender_current_soldiers))


if __name__ == "__main__":
    main()
