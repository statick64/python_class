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
panny = names.lower()
position_of_name = 0
name_inp = input("input name: ")
for i in names:
    position_of_name += 1
    if i == name_inp:
        print(f"\n {name_inp} is positioned at {position_of_name}")