#Just for the funðŸ˜
#Feel free to upgrade the dictionary to inculde new information. And be kind enough to send me a link to the codeðŸ˜ƒ

#When the prompt appears, input anything... The code will match it to any avenger if possible, and will give the output.


d = {
     "Ant Man" : "The guy that can shrink",
     "Black Widow" : "CQB Expert",
     "Black Panther" : "Wakandan King",
     "Iron Man" : "Billionaire Playboy and much more than that",
     "Captain America" : "First Avenger, Mr. Righteous",
     "Winter Soldier" : "Friend of Mr. Righteous",
     "Thor" : "God of Lightning",
     "Hulk" : "Big geen person. he loves to smash",
     "Hawkeye" : "Accurate",
     "War Machine" : "Big guns",
     "Star Lord" : "Crazy",
     "Quicksilver" : "Super fast",
     "Mantis" : "Mind reader and much more",
     "Drax" : "Killing machine",
     "Vision" : "Too much power for nothing",
     "Spider Man" : "Does everything a spider can",
     "Scarlet Witch" : "Mysterious",
     "Thanos" : "most dangerous villian in MCU ever",
     "Doctor Strange" : "Sorcerer Supreme",
     "Falcon" : "Wings to fly",
     "Corvus Glaive" : "Left hand of Thanos",
     "Cull Obsidian" : "The powerhouse of black order",
     "Ebony Maw" : "Right hand of Thanos",
     "Gamora" : "Adopted daughter of Thanos",
     "Groot" : "Sentient Tree",
     "Nebula" : "Adopted Cyborg daughter of Thanos",
     "Loki" : "God of mischief",
     "Ninja" : "biggest fan of MCU",
     "Shuri" : "tech genius of wakanda"
 }
try:
    input = input()
    assert len(input) != 0
except:
    print("Invalid Inputs!")
else:
    l = len(input)

    output = []
    for i in d:
        if input[:l].lower() == i[:l].lower() :
            output.append(i)
        elif len(i.split())==2:
            if input[:l].lower() == i.split()[1][:l].lower():
                output.append(i)

    if len(output) != 0:
        print("Matches Found:\n")
        for j in output:
            print("{0}\n{1}\n{0}\n{2}\n".format(len(j)*"=",j,d[j]))
    else:
        print("No Matches Found") 
