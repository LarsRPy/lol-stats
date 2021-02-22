from riotwatcher import LolWatcher

# read the line in the APIKey File
with open("./APIKey_file.txt", 'r') as file:
    api_key = file.read()

lol_watcher = LolWatcher(api_key)

region = 'euw1'

# a list with all champions-names in LOL, must be updated manually
champ_names = (
    'Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir', 'Bard'
    , 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'Chogath', 'Corki', 'Darius', 'Diana',
    'DrMundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank',
    'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV',
    'Jax', 'Jayce', 'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn',
    'Kennen', 'Khazix', 'Kindred', 'Kled', 'KogMaw', 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Lucian',
    'Lulu',
    'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus',
    'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy',
    'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', 'RekSai', 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze',
    'Samira',
    'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',
    'Soraka',
    'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle',
    'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vi', 'Viego',
    'Viktor',
    'Vladimir', 'Volibear', 'Warwick', 'MonkeyKing', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi',
    'Zac',
    'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra')

versions = lol_watcher.data_dragon.versions_for_region(region)
# print(versions)
champions_version = versions['n']['champion']
print(champions_version)

# get the current champion list from the API
current_champ_list = lol_watcher.data_dragon.champions(champions_version)

champ_table_name = 'champion.txt'
file = open(champ_table_name, 'w')
file.write('championname\tchmapionid')
file.close()

# write file for champion-dictionary with the champion name and the champion index in LOL
for champ in champ_names:
    # print(current_champ_list['data'][champ])
    with open(champ_table_name, 'a') as file:
        file.write('\n%s\t%s' % (current_champ_list['data'][champ]['name'], current_champ_list['data'][champ]['key']))
