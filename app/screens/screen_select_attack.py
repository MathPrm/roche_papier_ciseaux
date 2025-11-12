import random
from app.utils import (validate_choice)
from app.display import (clear_terminal)
from app.utils import (press_enter)

def player_choose_attack(username: str):
    '''
    This function allows user to choose an attack.
    '''
    
    rock: str = "👊 roche"
    paper: str = "✋️ papier"
    scissors: str = "✌️  ciseaux"
    init_turn: int = 0
    player_continue_playing: bool = True
    attacks: list[str] = [rock, paper, scissors]
    scores = {"player": 0, "ordi": 0}
    
    
    def turn_winner():
        if attack == computer_attack_str:
            print("Egalité entre les 2 joueurs !")
        elif (attack == rock and computer_attack_str == paper) or (attack == scissors and computer_attack_str == rock) or (attack == paper and computer_attack_str == scissors):
            print("Georges le Malin remporte le tour !\nAppuie sur entrer pour jouer le tour suivant.")
            scores["ordi"] += 1
        else:
            print("Tu as remporté le tour !\nAppuie sur entrer pour jouer le tour suivant.")
            scores["player"] += 1
    
    while player_continue_playing:
        print(f"Tour n° {init_turn}")
        print(f"{username}: {scores["player"]} VS Georges: {scores["ordi"]}")
        print("\n")
        computer_attack = random.choices(attacks, k=1)
        computer_attack_str = computer_attack[0]
        attack = validate_choice(attacks, "Choisis une attaque :\n")
        turn_winner()
        user_choice = validate_choice(["Rejouer un tour", "Finir la partie"],"Veux-tu rejouer un tour ?\n")
        clear_terminal()
        if user_choice == "Finir la partie":
            print(f"{username}: {scores["player"]} VS Georges: {scores["ordi"]}")
            if scores["player"] > scores["ordi"]:
                print(f"Félicitations {username} ! Vous avez gagné ! 🥳")
                player_continue_playing = False
            elif scores["player"] == scores["ordi"]:
                print(f"Ça, c'est une sacrée égalité {username} ! 😵‍💫")
                player_continue_playing = False
            else:
                print("Georges t'as vaincu ! 🤣🫵")
                player_continue_playing = False
        init_turn += 1
    return attack
    