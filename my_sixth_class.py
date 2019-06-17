name = """Emma
Olivia
Ava
Isabella
Sophia
Charlotte
Mia
Amelia
Harper
Evelyn
Abigail
Emily
Elizabeth
Mila
Ella
Avery
Sofia
Camila
Aria
Scarlett
Victoria
Madison
Luna
Grace
Chloe
Penelope
Layla
Riley
Zoey
Nora
Lily
Eleanor
Hannah
Lillian
Addison
Aubrey
Ellie
Stella
Natalie
Zoe
Leah
Hazel
Violet
Aurora
Savannah
Audrey
Brooklyn
Bella
Claire
Skylar
Lucy
Paisley
Everly
Anna
Caroline
Nova
Genesis
Emilia
Kennedy
Samantha"""
names = name.split("\n")
name_of_search = input("Enter name ")
name_not_search = True
for i in names:
    if i == name_of_search:
        print(f"{i} is available")
        name_not_search = False
        break
if name_not_search == True:
    print("not available")