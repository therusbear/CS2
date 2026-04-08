import random

#lists of current loadout for both ct and t side

ct_primary_weapons = {"AWP": 4750,
                       "M4A4": 2900, 
                       "M4A1-S": 2900, 
                       "FAMAS": 1950, 
                       "SSG-08": 1700, 
                       "NOVA": 1050, 
                       "XM1014": 2000, 
                       "MP9": 1250, 
                       "UMP-45": 1200, 
                       "MAG-7": 1300
                        }  
terrorist_primary_weapons = {"AWP": 4750, 
                             "AK-47": 2700, 
                             "GALIL AR": 1800, 
                             "SSG-08": 1700, 
                             "SG 553": 3000, 
                             "NEGEV": 1700, 
                             "NOVA": 1050, 
                             "XM1014": 2000, 
                             "MAC-10": 1050, 
                             "UMP-45": 1200, 
                             "SAWED-OFF": 1100
                            }   
ct_secondary_weapons = {"USP": 200, 
                        "DUAL-BERETTAS": 300, 
                        "P250": 300,
                        "FIVE-SEVEN": 500, 
                        "DESERT EAGLE": 700
                        }
terrorist_secondary_weapons = {"GLOCK-18": 200, 
                               "DUAL-BERETTAS": 300, 
                               "P250": 300, 
                               "TEC-9": 500, 
                               "DESERT EAGLE": 700
                                }
armor = {"NO-ARMOR": 0, "KEVLAR": 650, "HELMET AND KEVLAR": 1000}
utility = {"FLASHBANG": 200, "SMOKE": 300, "MOLOTOV/INCENDIARY": 400, "HIGH-EXPLOSIVE": 300, "DECOY": 50}
ct_only_kit = {"NO DEFUSE KIT": 0, "DEFUSE KIT": 300}
zeus = {"NO ZEUS": 0, "ZEUS": 200}

#two functions - one for randomizing the kit chance and one randomizing primary,secondary, armor, and utility
def generate_kit_chance():
    return random.choice(list(ct_only_kit))

def generate_zeus_chance():
    return random.choice(list(zeus))

def generate_random_loadout(team_input):
    if team_input in ["CT", "COUNTER TERRORIST", "COUNTER-TERRORIST"]:
        random_ct_primary = random.choice(list(ct_primary_weapons))
        random_ct_secondary = random.choice(list(ct_secondary_weapons))
        random_armor = random.choice(list(armor))
        k = random.randint(1, min(4, len(utility)))
        random_utility = random.sample(list(utility), k = k)
        print(f"Primary: {random_ct_primary}")
        print(f"Secondary: {random_ct_secondary}")
        print(f"Armor: {random_armor}")
        print(f"Utility: {random_utility}")
        print(f"Kit: {generate_kit_chance()}")
        print(f"Zeus: {generate_zeus_chance()}")
    elif team_input in ["T", "TERRORIST"]:
        random_terrorist_primary = random.choice(list(terrorist_primary_weapons))
        random_terrorist_secondary = random.choice(list(terrorist_secondary_weapons))
        random_armor = random.choice(list(armor))
        k = random.randint(1, min(4, len(utility)))
        random_utility = random.sample((utility), k = k)
        print(f"Primary: {random_terrorist_primary}")
        print(f"Secondary: {random_terrorist_secondary}")
        print(f"Armor: {random_armor}")
        print(f"Utility: {random_utility}")
        print(f"Zeus: {generate_zeus_chance()}")
    else:
        print("Invalid team. Enter what team you're on.")

def generate_loadout_balance(team_input, balance):
    if team_input in ["CT", "COUNTER TERRORIST", "COUNTER-TERRORIST"]:
        remaining = balance
        loadout = {}

        items_to_buy = ["primary", "secondary", "armor", "utility", "kit", "zeus"]
        
        for item in items_to_buy:
            if item == "primary":
                affordable = {name: price for name, price in ct_primary_weapons.items() if price <= remaining}

            elif item == "secondary":
                affordable = {name: price for name, price in ct_secondary_weapons.items() if price <= remaining}
                
            elif item == "armor":
                affordable = {name: price for name, price in armor.items() if price <= remaining}
                
            elif item == "utility":
                affordable = {name: price for name, price in utility.items() if price <= remaining}
            
                if not affordable:
                    break
                k = random.randint(1, min(4, len(affordable)))
                chosen_utility = random.sample(list(affordable), k = k)

                for u in chosen_utility:
                    if utility[u] <= remaining:
                        remaining -= utility[u]
                    else:
                        chosen_utility.remove(u)

                loadout[item] = chosen_utility
                continue
            elif item == "kit":
                affordable = {name: price for name, price in ct_only_kit.items() if price <= remaining}

            elif item == "zeus":
                affordable = {name: price for name, price in zeus.items() if price <= remaining}

            if not affordable: 
                print("Cannot buy any more items!")
                break

            choice = random.choice(list(affordable))
            remaining -= affordable[choice]
            loadout[item] = choice

        print("Loadout:")
        for item, choice in loadout.items():
            if item == "utility":
                print(f"Utility: {', '.join(choice)}")
            else:
                print(f"{item.capitalize()}: {choice}")
        print(f"Remaining balance: ${remaining}")

    elif team_input in ["T", "TERRORIST"]:
        remaining = balance
        loadout = {}

        items_to_buy = ["primary", "secondary", "armor", "utility", "zeus"]
        
        for item in items_to_buy:
            if item == "primary":
                affordable = {name: price for name, price in terrorist_primary_weapons.items() if price <= remaining}

            elif item == "secondary":
                affordable = {name: price for name, price in terrorist_secondary_weapons.items() if price <= remaining}
                
            elif item == "armor":
                affordable = {name: price for name, price in armor.items() if price <= remaining}
                
            elif item == "utility":
                affordable = {name: price for name, price in utility.items() if price <= remaining}
                if not affordable:
                    break
                k = random.randint(1, min(4, len(affordable)))
                chosen_utility = random.sample(list(affordable), k = k)
                for u in chosen_utility:
                    if utility[u] <= remaining:
                        remaining -= utility[u]
                    else:
                        chosen_utility.remove(u)
                loadout[item] = chosen_utility
                continue
            elif item == "zeus":
                affordable = {name: price for name, price in zeus.items() if price <= remaining}

            if not affordable: 
                print("Cannot buy any more items!")
                break

            choice = random.choice(list(affordable))
            remaining -= affordable[choice]
            loadout[item] = choice
            
        print("Loadout:")
        for item, choice in loadout.items():
            if item == "utility":
                print(f"Utility: {", ".join(choice)}")
            else:
                print(f"{item.capitalize()}: {choice}")
        print(f"Remaining balance: ${remaining}")

#main while loop that asks for initial startup and asks for team
while True:
        team_input = input("Enter what team you're on: ").strip().upper()
        mode: str = input("Random or budget loadout?: ").strip().upper()
    
        if mode == "RANDOM":
            generate_random_loadout(team_input) #team_input goes into generate_random_loadout under the variable "team"
        elif mode == "BUDGET":
            balance: int = int(input("How much money do you have?: "))
            generate_loadout_balance(team_input, balance)
        else:
            print("type random or budget")


