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
longest_name = max(len(i) for i in names)
for i in names:
        if len(i) == longest_name:
                print(i, end=" and ")