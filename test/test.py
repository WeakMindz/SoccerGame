
class Player:
    def __init__(self, name, age, shoot, speed, stamina, passing, tackle, position,ovl):
        self.name = name 
        self.age = age
        self.shoot = shoot
        self.speed = speed 
        self.stamina = stamina
        self.passing = passing
        self.tackle = tackle 
        self.position = position.upper()
        self.ovl = ovl

  
team_selection = input("Enter the team you want to play as: ").lower()




#England Squad
pickford = Player("Jordan Pickford", 32, shoot=12, speed=65, stamina=60, passing=78, tackle=15, position="GK", ovl=83)
henderson_d = Player("Dean Henderson", 29, shoot=10, speed=62, stamina=58, passing=66, tackle=12, position="GK", ovl=80)
trafford = Player("James Trafford", 23, shoot=10, speed=60, stamina=55, passing=70, tackle=10, position="GK", ovl=77)

stones = Player("John Stones", 32, shoot=60, speed=73, stamina=82, passing=85, tackle=87, position="DF", ovl=85)
guehi = Player("Marc Guéhi", 25, shoot=50, speed=77, stamina=85, passing=74, tackle=86, position="DF", ovl=83)
konsa = Player("Ezri Konsa", 28, shoot=45, speed=79, stamina=84, passing=70, tackle=85, position="DF", ovl=81)
james = Player("Reece James", 26, shoot=72, speed=81, stamina=80, passing=82, tackle=84, position="DF", ovl=84)
burn = Player("Dan Burn", 34, shoot=52, speed=61, stamina=78, passing=68, tackle=81, position="DF", ovl=78)
livramento = Player("Tino Livramento", 23, shoot=62, speed=85, stamina=83, passing=75, tackle=79, position="DF", ovl=80)
oreilly = Player("Nico O'Reilly", 21, shoot=68, speed=78, stamina=80, passing=79, tackle=75, position="DF", ovl=77)
quansah = Player("Jarell Quansah", 23, shoot=48, speed=74, stamina=81, passing=72, tackle=82, position="DF", ovl=79)
spence = Player("Djed Spence", 25, shoot=58, speed=87, stamina=82, passing=71, tackle=76, position="DF", ovl=77)

bellingham = Player("Jude Bellingham", 22, shoot=86, speed=81, stamina=90, passing=88, tackle=78, position="MF", ovl=90)
rice = Player("Declan Rice", 27, shoot=74, speed=78, stamina=94, passing=82, tackle=86, position="MF", ovl=87)
mainoo = Player("Kobbie Mainoo", 21, shoot=72, speed=76, stamina=84, passing=83, tackle=75, position="MF", ovl=81)
rogers = Player("Morgan Rogers", 23, shoot=79, speed=83, stamina=81, passing=80, tackle=50, position="MF", ovl=79)
anderson = Player("Elliot Anderson", 23, shoot=75, speed=77, stamina=84, passing=81, tackle=68, position="MF", ovl=80)
eze = Player("Eberechi Eze", 27, shoot=82, speed=83, stamina=79, passing=85, tackle=42, position="MF", ovl=83)
henderson_j = Player("Jordan Henderson", 35, shoot=68, speed=55, stamina=75, passing=79, tackle=74, position="MF", ovl=76)

kane = Player("Harry Kane", 32, shoot=93, speed=72, stamina=83, passing=84, tackle=40, position="FW", ovl=90)
saka = Player("Bukayo Saka", 24, shoot=84, speed=89, stamina=87, passing=83, tackle=55, position="FW", ovl=87)
rashford = Player("Marcus Rashford", 28, shoot=85, speed=91, stamina=80, passing=78, tackle=41, position="FW", ovl=83)
gordon = Player("Anthony Gordon", 25, shoot=80, speed=90, stamina=86, passing=79, tackle=45, position="FW", ovl=82)
madueke = Player("Noni Madueke", 24, shoot=78, speed=87, stamina=80, passing=76, tackle=38, position="FW", ovl=80)
toney = Player("Ivan Toney", 30, shoot=84, speed=78, stamina=81, passing=74, tackle=42, position="FW", ovl=81)
watkins = Player("Ollie Watkins", 30, shoot=85, speed=86, stamina=84, passing=73, tackle=40, position="FW", ovl=83)
# --- Full Squad Array ---
england_squad = [
    pickford, henderson_d, trafford,
    stones, guehi, konsa, james, burn, livramento, oreilly, quansah, spence,
    bellingham, rice, mainoo, rogers, anderson, eze, henderson_j,
    kane, saka, rashford, gordon, madueke, toney, watkins
]



#Brazil Squad ---

# Goalkeepers (GK)
alisson = Player("Alisson Becker", 33, shoot=10, speed=62, stamina=60, passing=85, tackle=12, position="GK", ovl=89)
ederson_m = Player("Ederson", 32, shoot=15, speed=64, stamina=62, passing=93, tackle=15, position="GK", ovl=87)
weverton = Player("Weverton", 38, shoot=10, speed=50, stamina=52, passing=72, tackle=10, position="GK", ovl=78)

marquinhos = Player("Marquinhos", 32, shoot=55, speed=76, stamina=83, passing=79, tackle=89, position="DF", ovl=87)
gabriel_m = Player("Gabriel Magalhães", 28, shoot=62, speed=74, stamina=84, passing=70, tackle=87, position="DF", ovl=86)
danilo_l = Player("Danilo Luiz", 34, shoot=68, speed=72, stamina=80, passing=78, tackle=82, position="DF", ovl=80)
bremer = Player("Bremer", 29, shoot=50, speed=78, stamina=82, passing=65, tackle=85, position="DF", ovl=83)
alex_sandro = Player("Alex Sandro", 35, shoot=65, speed=70, stamina=75, passing=77, tackle=79, position="DF", ovl=78)
ibanez = Player("Roger Ibañez", 27, shoot=48, speed=80, stamina=81, passing=68, tackle=82, position="DF", ovl=80)
douglas_s = Player("Douglas Santos", 32, shoot=60, speed=75, stamina=82, passing=76, tackle=78, position="DF", ovl=78)
leo_pereira = Player("Léo Pereira", 30, shoot=54, speed=71, stamina=80, passing=72, tackle=80, position="DF", ovl=77)

casemiro = Player("Casemiro", 34, shoot=73, speed=63, stamina=82, passing=80, tackle=87, position="MF", ovl=84)
bruno_g = Player("Bruno Guimarães", 28, shoot=76, speed=75, stamina=89, passing=86, tackle=80, position="MF", ovl=86)
paqueta = Player("Lucas Paquetá", 28, shoot=80, speed=77, stamina=84, passing=85, tackle=68, position="MF", ovl=83)
fabinho = Player("Fabinho", 32, shoot=65, speed=66, stamina=80, passing=79, tackle=82, position="MF", ovl=80)
ederson_a = Player("Éderson (Atalanta)", 26, shoot=72, speed=79, stamina=91, passing=78, tackle=83, position="MF", ovl=81)
danilo_s = Player("Danilo Santos", 25, shoot=68, speed=76, stamina=85, passing=77, tackle=76, position="MF", ovl=78)

vini_jr = Player("Vinícius Júnior", 25, shoot=89, speed=97, stamina=88, passing=84, tackle=31, position="FW", ovl=91)
neymar = Player("Neymar Jr", 34, shoot=87, speed=80, stamina=74, passing=90, tackle=35, position="FW", ovl=88)
raphinha = Player("Raphinha", 29, shoot=84, speed=89, stamina=87, passing=83, tackle=50, position="FW", ovl=85)
endrick = Player("Endrick", 19, shoot=83, speed=87, stamina=81, passing=74, tackle=38, position="FW", ovl=82)
martinelli = Player("Gabriel Martinelli", 24, shoot=81, speed=91, stamina=86, passing=77, tackle=42, position="FW", ovl=83)
cunha = Player("Matheus Cunha", 27, shoot=82, speed=83, stamina=82, passing=78, tackle=45, position="FW", ovl=81)
luiz_henrique = Player("Luiz Henrique", 25, shoot=78, speed=88, stamina=80, passing=75, tackle=39, position="FW", ovl=80)
igor_thiago = Player("Igor Thiago", 24, shoot=80, speed=81, stamina=83, passing=70, tackle=40, position="FW", ovl=79)
rayan = Player("Rayan", 19, shoot=77, speed=84, stamina=78, passing=71, tackle=35, position="FW", ovl=76)

brazil_squad = [
    alisson, ederson_m, weverton,
    marquinhos, gabriel_m, danilo_l, bremer, alex_sandro, ibanez, douglas_s, leo_pereira,
    casemiro, bruno_g, paqueta, fabinho, ederson_a, danilo_s,
    vini_jr, neymar, raphinha, endrick, martinelli, cunha, luiz_henrique, igor_thiago, rayan
]



# Goalkeepers (GK)
e_martinez = Player("Emiliano Martínez", 33, shoot=12, speed=63, stamina=60, passing=81, tackle=15, position="GK", ovl=87)
rulli = Player("Gerónimo Rulli", 34, shoot=10, speed=58, stamina=55, passing=72, tackle=12, position="GK", ovl=81)
musso = Player("Juan Musso", 32, shoot=10, speed=60, stamina=56, passing=68, tackle=10, position="GK", ovl=79)

# Defenders (DF)
romero = Player("Cristian Romero", 28, shoot=55, speed=77, stamina=85, passing=71, tackle=90, position="DF", ovl=88)
l_martinez = Player("Lisandro Martínez", 28, shoot=60, speed=76, stamina=84, passing=82, tackle=87, position="DF", ovl=86)
otamendi = Player("Nicolás Otamendi", 38, shoot=58, speed=53, stamina=68, passing=68, tackle=82, position="DF", ovl=80)
molina = Player("Nahuel Molina", 28, shoot=67, speed=84, stamina=86, passing=77, tackle=79, position="DF", ovl=82)
tagliafico = Player("Nicolás Tagliafico", 33, shoot=62, speed=73, stamina=81, passing=75, tackle=81, position="DF", ovl=81)
montiel = Player("Gonzalo Montiel", 29, shoot=61, speed=77, stamina=83, passing=72, tackle=80, position="DF", ovl=79)
balerdi = Player("Leonardo Balerdi", 27, shoot=48, speed=72, stamina=80, passing=69, tackle=81, position="DF", ovl=79)
medina = Player("Facundo Medina", 27, shoot=52, speed=74, stamina=82, passing=74, tackle=82, position="DF", ovl=80)
pezzzella = Player("Germán Pezzella", 34, shoot=40, speed=55, stamina=70, passing=65, tackle=78, position="DF", ovl=77)

# Midfielders (MF)
de_paul = Player("Rodrigo De Paul", 32, shoot=76, speed=75, stamina=92, passing=83, tackle=79, position="MF", ovl=84)
mac_allister = Player("Alexis Mac Allister", 27, shoot=81, speed=72, stamina=88, passing=87, tackle=76, position="MF", ovl=86)
enzo_f = Player("Enzo Fernández", 25, shoot=79, speed=70, stamina=85, passing=89, tackle=77, position="MF", ovl=85)
paredes = Player("Leandro Paredes", 31, shoot=74, speed=61, stamina=78, passing=84, tackle=78, position="MF", ovl=81)
palacios = Player("Exequiel Palacios", 27, shoot=73, speed=73, stamina=86, passing=81, tackle=79, position="MF", ovl=81)
lo_celso = Player("Giovani Lo Celso", 30, shoot=77, speed=72, stamina=79, passing=84, tackle=65, position="MF", ovl=81)
guido_r = Player("Guido Rodríguez", 32, shoot=60, speed=58, stamina=80, passing=75, tackle=81, position="MF", ovl=78)

# Forwards (FW)
messi = Player("Lionel Messi", 38, shoot=91, speed=78, stamina=72, passing=94, tackle=35, position="FW", ovl=91)
l_martinez_fw = Player("Lautaro Martínez", 28, shoot=89, speed=81, stamina=85, passing=74, tackle=45, position="FW", ovl=88)
alvarez = Player("Julián Álvarez", 26, shoot=86, speed=85, stamina=90, passing=80, tackle=52, position="FW", ovl=86)
n_gonzalez = Player("Nicolás González", 28, shoot=78, speed=85, stamina=86, passing=76, tackle=58, position="FW", ovl=80)
almada = Player("Thiago Almada", 25, shoot=79, speed=84, stamina=80, passing=82, tackle=41, position="FW", ovl=81)
dybala = Player("Paulo Dybala", 32, shoot=85, speed=80, stamina=75, passing=86, tackle=35, position="FW", ovl=84)
correa = Player("Angel Correa", 31, shoot=81, speed=82, stamina=80, passing=78, tackle=44, position="FW", ovl=81)

argentina_squad =[
    e_martinez, rulli, musso, romero, l_martinez, otamendi, molina, tagliafico, montiel, balerdi, medina, ,
    de_paul, mac_allister, enzo_f, paredes, palacios, lo_celso, guido_r, messi, l_martinez_fw, alvarez, n_gonzalez, almada, dybala, correa
]


#Team Input and selection
























print("\n==================================================")
print("                PLAYER RATING SYSTEM              ")
print("==================================================")
print(f"{'Name':<20} | {'Age':<3} | {'Pos':<3} | {'Calculated OVL':<14}")
print("-" * 50)

if team_selection == "england":
    for player in england_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")
if team_selection == "brazil":
    for player in brazil_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")