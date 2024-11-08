from pakudex import Pakudex

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                print("Please enter a valid size.")
                continue
            break
        except ValueError:
            print("Please enter a valid size.")
    
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    pakudex = Pakudex(capacity)

    while True:
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        
        try:
            choice = input("\nWhat would you like to do? ")
            
            if choice == "1":  # List Pakuri
                species_array = pakudex.get_species_array()
                if species_array is None:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri In Pakudex:")
                    for i, species in enumerate(species_array, 1):
                        print(f"{i}. {species}")
                        
            elif choice == "2":  # Show Pakuri
                species = input("Enter the name of the species to display: ")
                stats = pakudex.get_stats(species)
                if stats is None:
                    print("Error: No such Pakuri!")
                else:
                    print(f"\nSpecies: {species}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")
                    
            elif choice == "3":  # Add Pakuri
                if pakudex.get_size() >= pakudex.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    species = input("Enter the name of the species to add: ")
                    if pakudex.add_pakuri(species):
                        print(f"Pakuri species {species} successfully added!")
                    else:
                        print("Error: Pakudex already contains this species!")
                        
            elif choice == "4":  # Evolve Pakuri
                species = input("Enter the name of the species to evolve: ")
                if pakudex.evolve_species(species):
                    print(f"{species} has evolved!")
                else:
                    print("Error: No such Pakuri!")
                    
            elif choice == "5":  # Sort Pakuri
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")
                
            elif choice == "6":  # Exit
                print("Thanks for using Pakudex! Bye!")
                break
                
            else:
                print("Unrecognized menu selection!")
                
        except ValueError:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()