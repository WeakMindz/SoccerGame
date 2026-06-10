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
# ==============================================================================
# FRANCE NATIONAL TEAM SQUAD
# ==============================================================================

# Goalkeepers (GK)
maignan = Player("Mike Maignan", 30, shoot=12, speed=62, stamina=66, passing=80, tackle=15, position="GK", ovl=87)
samba = Player("Brice Samba", 32, shoot=10, speed=55, stamina=60, passing=74, tackle=11, position="GK", ovl=81)
risser = Player("Robin Risser", 21, shoot=10, speed=52, stamina=58, passing=68, tackle=12, position="GK", ovl=75)

# Defenders (DF)
saliba = Player("William Saliba", 25, shoot=39, speed=82, stamina=83, passing=74, tackle=87, position="DF", ovl=87)
t_hernandez = Player("Theo Hernández", 28, shoot=72, speed=93, stamina=89, passing=78, tackle=80, position="DF", ovl=86)
kounde = Player("Jules Koundé", 27, shoot=50, speed=80, stamina=84, passing=76, tackle=85, position="DF", ovl=85)
upamecano = Player("Dayot Upamecano", 27, shoot=45, speed=82, stamina=80, passing=70, tackle=83, position="DF", ovl=83)
l_hernandez = Player("Lucas Hernández", 30, shoot=54, speed=75, stamina=82, passing=73, tackle=84, position="DF", ovl=83)
konate = Player("Ibrahima Konaté", 27, shoot=38, speed=78, stamina=79, passing=65, tackle=84, position="DF", ovl=83)
gusto = Player("Malo Gusto", 23, shoot=61, speed=86, stamina=84, passing=77, tackle=78, position="DF", ovl=81)
digne = Player("Lucas Digne", 32, shoot=65, speed=73, stamina=78, passing=79, tackle=77, position="DF", ovl=79)
lacroix = Player("Maxence Lacroix", 26, shoot=35, speed=76, stamina=78, passing=63, tackle=80, position="DF", ovl=79)

# Midfielders (MF)
tchouameni = Player("Aurélien Tchouaméni", 26, shoot=72, speed=74, stamina=88, passing=81, tackle=84, position="MF", ovl=85)
rabiot = Player("Adrien Rabiot", 31, shoot=75, speed=76, stamina=86, passing=80, tackle=79, position="MF", ovl=83)
kante = Player("N'Golo Kanté", 35, shoot=66, speed=74, stamina=86, passing=75, tackle=82, position="MF", ovl=82)
zaire_emery = Player("Warren Zaïre-Emery", 20, shoot=72, speed=78, stamina=85, passing=81, tackle=76, position="MF", ovl=81)
m_kone = Player("Manu Koné", 25, shoot=68, speed=75, stamina=82, passing=76, tackle=78, position="MF", ovl=79)

# Forwards (FW)
mbappe = Player("Kylian Mbappé", 27, shoot=90, speed=97, stamina=83, passing=81, tackle=37, position="FW", ovl=91)
dembele = Player("Ousmane Dembélé", 29, shoot=88, speed=91, stamina=76, passing=83, tackle=50, position="FW", ovl=90)
olise = Player("Michael Olise", 24, shoot=80, speed=78, stamina=85, passing=84, tackle=50, position="FW", ovl=86)
thuram = Player("Marcus Thuram", 28, shoot=81, speed=86, stamina=82, passing=74, tackle=40, position="FW", ovl=83)
barcola = Player("Bradley Barcola", 23, shoot=75, speed=88, stamina=75, passing=74, tackle=30, position="FW", ovl=80)
doue = Player("Désiré Doué", 21, shoot=74, speed=85, stamina=78, passing=79, tackle=38, position="FW", ovl=80)
cherki = Player("Rayan Cherki", 22, shoot=75, speed=80, stamina=72, passing=83, tackle=28, position="FW", ovl=79)
mateta = Player("Jean-Philippe Mateta", 28, shoot=80, speed=75, stamina=77, passing=66, tackle=35, position="FW", ovl=79)
akliouche = Player("Maghnes Akliouche", 24, shoot=72, speed=78, stamina=74, passing=78, tackle=32, position="FW", ovl=77)

france_squad = [
    maignan, samba, risser, saliba, kounde, upamecano, t_hernandez, l_hernandez,
    konate, gusto, digne, lacroix, tchouameni, rabiot, zaire_emery, kante,
    m_kone, mbappe, dembele, olise, thuram, barcola, doue, cherki, mateta, akliouche
]


# ==============================================================================
# IRAQ NATIONAL TEAM SQUAD
# ==============================================================================

# Goalkeepers (GK)
j_hassan = Player("Jalal Hassan", 35, shoot=15, speed=35, stamina=40, passing=50, tackle=15, position="GK", ovl=68)
f_talib = Player("Fahad Talib", 31, shoot=10, speed=48, stamina=59, passing=61, tackle=11, position="GK", ovl=71)
a_basil = Player("Ahmed Basil", 33, shoot=10, speed=45, stamina=56, passing=59, tackle=12, position="GK", ovl=69)

# Defenders (DF)
h_ali = Player("Hussein Ali", 24, shoot=52, speed=78, stamina=79, passing=66, tackle=71, position="DF", ovl=73)
m_doski = Player("Merchas Doski", 26, shoot=48, speed=76, stamina=81, passing=68, tackle=72, position="DF", ovl=73)
r_sulaka = Player("Rebin Sulaka", 34, shoot=38, speed=60, stamina=72, passing=62, tackle=74, position="DF", ovl=72)
z_tahseen = Player("Zaid Tahseen", 25, shoot=35, speed=68, stamina=74, passing=58, tackle=72, position="DF", ovl=70)
m_younis = Player("Manaf Younis", 29, shoot=34, speed=65, stamina=75, passing=55, tackle=71, position="DF", ovl=69)
f_putros = Player("Frans Putros", 32, shoot=44, speed=63, stamina=70, passing=64, tackle=70, position="DF", ovl=69)
m_saadoon = Player("Mustafa Saadoon", 25, shoot=50, speed=77, stamina=78, passing=63, tackle=68, position="DF", ovl=69)
a_yahya = Player("Ahmed Yahya", 29, shoot=42, speed=70, stamina=73, passing=61, tackle=68, position="DF", ovl=68)
a_hashem = Player("Akam Hashem", 27, shoot=33, speed=64, stamina=71, passing=54, tackle=67, position="DF", ovl=66)

# Midfielders (MF)
a_al_ammari = Player("Amir Al-Ammari", 28, shoot=62, speed=65, stamina=75, passing=68, tackle=60, position="MF", ovl=67)
z_iqbal = Player("Zidane Iqbal", 23, shoot=60, speed=68, stamina=72, passing=68, tackle=55, position="MF", ovl=68)
i_bayesh = Player("Ibrahim Bayesh", 26, shoot=69, speed=79, stamina=85, passing=71, tackle=64, position="MF", ovl=74)
a_sher = Player("Aimar Sher", 23, shoot=62, speed=72, stamina=78, passing=73, tackle=68, position="MF", ovl=71)
k_yakob = Player("Kevin Yakob", 25, shoot=66, speed=71, stamina=75, passing=72, tackle=58, position="MF", ovl=70)
a_qasim = Player("Ahmed Qasim", 21, shoot=65, speed=76, stamina=72, passing=68, tackle=48, position="MF", ovl=68)
z_ismail = Player("Zaid Ismail", 23, shoot=58, speed=68, stamina=74, passing=65, tackle=66, position="MF", ovl=66)

# Forwards (FW)
a_hussein = Player("Aymen Hussein", 30, shoot=74, speed=65, stamina=70, passing=55, tackle=30, position="FW", ovl=71)
a_jassim = Player("Ali Jassim", 22, shoot=62, speed=67, stamina=68, passing=62, tackle=22, position="FW", ovl=62)
a_al_hamadi = Player("Ali Al-Hamadi", 24, shoot=75, speed=82, stamina=76, passing=64, tackle=32, position="FW", ovl=73)
y_amyn = Player("Youssef Amyn", 22, shoot=70, speed=83, stamina=74, passing=67, tackle=38, position="FW", ovl=72)
m_ali = Player("Mohanad Ali", 25, shoot=74, speed=78, stamina=72, passing=60, tackle=28, position="FW", ovl=71)
m_farji = Player("Marko Farji", 22, shoot=68, speed=77, stamina=71, passing=66, tackle=34, position="FW", ovl=68)
a_yousef = Player("Ali Yousef", 29, shoot=70, speed=72, stamina=70, passing=59, tackle=27, position="FW", ovl=67)

iraq_squad = [
    j_hassan, f_talib, a_basil, h_ali, m_doski, r_sulaka, z_tahseen, m_younis,
    f_putros, m_saadoon, a_yahya, a_hashem, a_al_ammari, z_iqbal, i_bayesh, a_sher,
    k_yakob, a_qasim, z_ismail, a_hussein, a_jassim, a_al_hamadi, y_amyn, m_ali,
    m_farji, a_yousef
]


# ==============================================================================
# NORWAY NATIONAL TEAM SQUAD
# ==============================================================================

# Goalkeepers (GK)
nyland = Player("Ørjan Nyland", 35, shoot=12, speed=51, stamina=61, passing=72, tackle=14, position="GK", ovl=78)
selvik = Player("Egil Selvik", 28, shoot=10, speed=48, stamina=58, passing=65, tackle=11, position="GK", ovl=73)
tangvik = Player("Sander Tangvik", 23, shoot=10, speed=50, stamina=56, passing=62, tackle=12, position="GK", ovl=70)

# Defenders (DF)
ajer = Player("Kristoffer Ajer", 28, shoot=48, speed=74, stamina=80, passing=71, tackle=81, position="DF", ovl=80)
ryerson = Player("Julian Ryerson", 28, shoot=64, speed=80, stamina=90, passing=73, tackle=80, position="DF", ovl=80)
ostigard = Player("Leo Østigård", 26, shoot=55, speed=68, stamina=79, passing=62, tackle=80, position="DF", ovl=78)
wolfe = Player("David Møller Wolfe", 24, shoot=50, speed=82, stamina=84, passing=70, tackle=75, position="DF", ovl=76)
pedersen = Player("Marcus Holmgren Pedersen", 25, shoot=46, speed=86, stamina=83, passing=67, tackle=74, position="DF", ovl=75)
bjorkan = Player("Fredrik André Bjørkan", 27, shoot=52, speed=81, stamina=80, passing=69, tackle=73, position="DF", ovl=74)
heggem = Player("Torbjørn Heggem", 27, shoot=38, speed=69, stamina=76, passing=63, tackle=74, position="DF", ovl=72)

# Midfielders (MF)
odegaard = Player("Martin Ødegaard", 27, shoot=79, speed=68, stamina=88, passing=88, tackle=67, position="MF", ovl=87)
berge = Player("Sander Berge", 28, shoot=68, speed=72, stamina=86, passing=79, tackle=78, position="MF", ovl=80)
thorstvedt = Player("Kristian Thorstvedt", 27, shoot=74, speed=68, stamina=82, passing=74, tackle=70, position="MF", ovl=77)
patrick_berg = Player("Patrick Berg", 28, shoot=65, speed=66, stamina=88, passing=76, tackle=76, position="MF", ovl=77)
vetlesen = Player("Hugo Vetlesen", 26, shoot=70, speed=73, stamina=81, passing=75, tackle=66, position="MF", ovl=76)
donnum = Player("Aron Dønnum", 28, shoot=69, speed=78, stamina=77, passing=71, tackle=54, position="MF", ovl=74)
myhre = Player("Felix Myhre", 27, shoot=62, speed=70, stamina=80, passing=72, tackle=71, position="MF", ovl=73)

# Forwards (FW)
haaland = Player("Erling Haaland", 25, shoot=91, speed=86, stamina=76, passing=70, tackle=45, position="FW", ovl=90)
sorloth = Player("Alexander Sørloth", 30, shoot=83, speed=80, stamina=82, passing=72, tackle=40, position="FW", ovl=83)
strand_larsen = Player("Jørgen Strand Larsen", 26, shoot=80, speed=76, stamina=80, passing=68, tackle=38, position="FW", ovl=79)
bobb = Player("Oscar Bobb", 22, shoot=72, speed=82, stamina=74, passing=75, tackle=40, position="FW", ovl=78)
nusa = Player("Antonio Nusa", 21, shoot=73, speed=86, stamina=74, passing=72, tackle=35, position="FW", ovl=78)
elyounoussi = Player("Mohamed Elyounoussi", 31, shoot=75, speed=74, stamina=78, passing=75, tackle=52, position="FW", ovl=76)

norway_squad = [
    nyland, selvik, tangvik, ajer, ryerson, ostigard, wolfe, pedersen,
    bjorkan, heggem, odegaard, berge, thorstvedt, patrick_berg, vetlesen, donnum,
    myhre, haaland, sorloth, strand_larsen, bobb, nusa, elyounoussi
]


# ==============================================================================
# SENEGAL NATIONAL TEAM SQUAD
# ==============================================================================

# Goalkeepers (GK)
e_mendy = Player("Édouard Mendy", 34, shoot=15, speed=40, stamina=45, passing=60, tackle=15, position="GK", ovl=82)
diaw = Player("Mory Diaw", 32, shoot=10, speed=48, stamina=58, passing=62, tackle=11, position="GK", ovl=75)
y_diouf = Player("Yehvann Diouf", 26, shoot=10, speed=53, stamina=57, passing=66, tackle=13, position="GK", ovl=76)

# Defenders (DF)
koulibaly = Player("Kalidou Koulibaly", 34, shoot=45, speed=70, stamina=72, passing=64, tackle=85, position="DF", ovl=84)
niakhate = Player("Moussa Niakhaté", 30, shoot=42, speed=73, stamina=80, passing=68, tackle=80, position="DF", ovl=79)
jakobs = Player("Ismail Jakobs", 26, shoot=55, speed=87, stamina=83, passing=71, tackle=76, position="DF", ovl=77)
diatta = Player("Krépin Diatta", 27, shoot=70, speed=85, stamina=82, passing=74, tackle=72, position="DF", ovl=77)
seck = Player("Abdoulaye Seck", 34, shoot=35, speed=58, stamina=70, passing=54, tackle=76, position="DF", ovl=74)
m_sarr = Player("Mamadou Sarr", 20, shoot=38, speed=72, stamina=75, passing=64, tackle=75, position="DF", ovl=73)
mbow = Player("Moustapha Mbow", 26, shoot=33, speed=68, stamina=76, passing=58, tackle=74, position="DF", ovl=72)
e_diouf = Player("El Hadji Malick Diouf", 21, shoot=52, speed=80, stamina=78, passing=67, tackle=71, position="DF", ovl=72)
a_mendy = Player("Antoine Mendy", 22, shoot=44, speed=78, stamina=76, passing=63, tackle=72, position="DF", ovl=71)
camara_i = Player("Ilay Camara", 23, shoot=48, speed=79, stamina=75, passing=65, tackle=70, position="DF", ovl=70)

# Midfielders (MF)
p_m_sarr = Player("Pape Matar Sarr", 23, shoot=74, speed=78, stamina=85, passing=79, tackle=78, position="MF", ovl=81)
l_camara = Player("Lamine Camara", 22, shoot=72, speed=75, stamina=84, passing=78, tackle=74, position="MF", ovl=78)
h_diarra = Player("Habib Diarra", 22, shoot=70, speed=79, stamina=83, passing=75, tackle=72, position="MF", ovl=77)
p_gueye = Player("Pape Gueye", 27, shoot=67, speed=68, stamina=82, passing=74, tackle=76, position="MF", ovl=77)
g_gueye = Player("Idrissa Gana Gueye", 36, shoot=62, speed=65, stamina=78, passing=72, tackle=79, position="MF", ovl=76)
ciss = Player("Pathé Ciss", 32, shoot=64, speed=63, stamina=80, passing=71, tackle=75, position="MF", ovl=75)
b_ndiaye = Player("Bara Sapoko Ndiaye", 19, shoot=63, speed=73, stamina=76, passing=70, tackle=65, position="MF", ovl=70)

# Forwards (FW)
mane = Player("Sadio Mané", 34, shoot=80, speed=82, stamina=76, passing=78, tackle=45, position="FW", ovl=83)
jackson = Player("Nicolas Jackson", 24, shoot=81, speed=85, stamina=80, passing=74, tackle=35, position="FW", ovl=82)
i_sarr = Player("Ismaïla Sarr", 28, shoot=76, speed=89, stamina=78, passing=72, tackle=38, position="FW", ovl=79)
i_ndiaye = Player("Iliman Ndiaye", 26, shoot=75, speed=80, stamina=79, passing=76, tackle=45, position="FW", ovl=78)
c_ndiaye = Player("Chérif Ndiaye", 30, shoot=77, speed=76, stamina=75, passing=62, tackle=30, position="FW", ovl=75)
b_dieng = Player("Bamba Dieng", 26, shoot=76, speed=82, stamina=74, passing=65, tackle=28, position="FW", ovl=74)
diao = Player("Assane Diao", 20, shoot=72, speed=84, stamina=73, passing=68, tackle=35, position="FW", ovl=74)
i_mbaye = Player("Ibrahim Mbaye", 18, shoot=68, speed=83, stamina=70, passing=66, tackle=26, position="FW", ovl=71)

senegal_squad = [
    e_mendy, diaw, y_diouf, koulibaly, niakhate, jakobs, diatta, seck,
    m_sarr, mbow, e_diouf, a_mendy, camara_i, p_m_sarr, l_camara, h_diarra,
    p_gueye, g_gueye, ciss, b_ndiaye, mane, jackson, i_sarr, i_ndiaye,
    c_ndiaye, b_dieng, diao, i_mbaye
]

print("\n==================================================")
print("                PLAYER RATING SYSTEM              ")
print("==================================================")
print(f"{'Name':<20} | {'Age':<3} | {'Pos':<3} | {'Calculated OVL':<14}")
print("-" * 50)

if team_selection == "france":
    for player in france_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")
if team_selection == "iraq":
    for player in iraq_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")
if team_selection == "norway":
    for player in norway_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")
if team_selection == "senegal":
    for player in senegal_squad:
        print(f"{player.name:<20} | {player.age:<3} | {player.position:<3} | {player.ovl:^14}")

    print("==================================================\n")
formation = input("Type for formation: ")
selecec_postion = 'FW'

if formation == "4 4 2":
    for selecec_postion in player.position:
            print(player.name)