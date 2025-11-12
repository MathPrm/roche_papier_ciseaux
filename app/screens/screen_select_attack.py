import random
from app.utils import (validate_choice)
from app.display import (clear_terminal)
from app.utils import (press_enter)

def player_choose_attack(username: str) -> str:
    '''
    This function allows user to choose an attack.
    '''
    
    rock: str = "👊 roche"
    paper: str = "✋️ papier"
    scissors: str = "✌️  ciseaux"
    init_turn: int = 0
    player_continue_playing: bool = True
    attacks: list[str] = [rock, paper, scissors]
    scores: dict = {"player": 0, "computer": 0}
    
    
    def turn_winner():
        if attack == computer_attack_str:
            print(f"\nGeorges a joué : {computer_attack_str}")
            print("\nEgalité entre les 2 joueurs !\n")
        elif (attack == rock and computer_attack_str == paper) or (attack == scissors and computer_attack_str == rock) or (attack == paper and computer_attack_str == scissors):
            print(f"\nGeorges a joué : {computer_attack_str}")
            print("\nGeorges le Malin remporte le tour !\n\n")
            scores["computer"] += 1
        else:
            print(f"\nGeorges a joué : {computer_attack_str}")
            print("\nTu as remporté le tour !\n")
            scores["player"] += 1
    
    while player_continue_playing:
        print(f"Tour n° {init_turn}")
        print(f"{username}: {scores["player"]} VS Georges: {scores["computer"]}")
        print("\n")
        computer_attack: list[str] = random.choices(attacks, k=1)
        computer_attack_str: str = computer_attack[0]
        attack: str = validate_choice(attacks, "Choisis une attaque :\n")
        turn_winner()
        user_choice: str = validate_choice(["Rejouer un tour", "Finir la partie"],"Veux-tu rejouer un tour ?\n")
        clear_terminal()
        if user_choice == "Finir la partie":
            print(f"{username}: {scores["player"]} VS Georges: {scores["computer"]}")
            if scores["player"] > scores["computer"]:
                print(f"Félicitations {username} ! Tu as gagné ! 🥳")
                player_continue_playing = False
            elif scores["player"] == scores["computer"]:
                print(f"Ça, c'est une sacrée égalité {username} ! 😵‍💫")
                player_continue_playing = False
            else:
                print("Georges t'as vaincu ! 🤣🫵")
                player_continue_playing = False
        init_turn += 1
    return attack
    