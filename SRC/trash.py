"""print(nemy)
    print()
    print(goblin_one)

    fight_round = 1
    print("========FIGHT========")
    while nemy.get_health() != 0 and goblin_one.get_health != 0:
        print(f"Round {fight_round}")
        nemy_attack = nemy.damage()*randint(1, 3)
        goblin_one.take_damage(nemy_attack)
        if(goblin_one.get_health() == 0):
            print("Goblin has died.")
            break
        else:
            print(f"Goblin has {goblin_one.get_health()} hp left.")
            goblin_attack = goblin_one.damage()*randint(1, 3)
            nemy.take_damage(goblin_attack)
            print(f"Nemy has {nemy.get_health()} hp left.")
            if(nemy.get_health() == 0): print("Nemy has died!")
        fight_round += 1
    if(nemy.get_health() == 0): print("The Goblin won!")
    else: print("Nemy has won!")"""