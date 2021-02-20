from riotwatcher import LolWatcher
import argparse
import os
import sys
import csv

# for searching in a dictionary for a key
def search(myDict, lookup):
    for key, value in myDict.items():
         for v in value:
            if lookup in v:
                return key


# parse options, path,playername and queue for command line use
parser = argparse.ArgumentParser(description='Get Data of one EUWest Player of the current Season')
parser.add_argument('APIkeyFile', metavar='path', type=str, help='Filepath of the API-Key')
parser.add_argument('Playername', metavar='playername', type=str, help='Name of the Player')
parser.add_argument('Queue', type=str, default=None,
                    help='Which Queue you want to know Solo, Flex, Normal; by default all')
args = parser.parse_args()

# give option to variables
player_name = args.Playername
input_file = args.APIkeyFile
if args.Queue == 'Solo':
    queue = {420} # for the different types of modi there are numbers define
if args.Queue == 'Flex':
    queue = {440}
if args.Queue == 'Normal':
    queue = {400}

# use for right down the data
output_file_name = player_name + '_' + args.Queue + '_data.txt'

# check if APIKey file exists
if not os.path.isfile(input_file):
    print('The Path of the APIKey-File does not exist')
    sys.exit()

# champion dictionary for translation of numbers into really champion names
champ_dic = {266: 'Aatrox', 103: 'Ahri', 84: 'Akali', 12: 'Alistar', 32: 'Amumu', 34: 'Anivia', 1: 'Annie', 523: 'Aphelios', 22: 'Ashe', 136: 'Aurelion Sol', 268: 'Azir', 432: 'Bard', 53: 'Blitzcrank', 63: 'Brand', 201: 'Braum', 51: 'Caitlyn', 164: 'Camille', 69: 'Cassiopeia', 31: "Cho'Gath", 42: 'Corki', 122: 'Darius', 131: 'Diana', 36: 'Dr. Mundo', 119: 'Draven', 245: 'Ekko', 60: 'Elise', 28: 'Evelynn', 81: 'Ezreal', 9: 'Fiddlesticks', 114: 'Fiora', 105: 'Fizz', 3: 'Galio', 41: 'Gangplank', 86: 'Garen', 150: 'Gnar', 79: 'Gragas', 104: 'Graves', 120: 'Hecarim', 74: 'Heimerdinger', 420: 'Illaoi', 39: 'Irelia', 427: 'Ivern', 40: 'Janna', 59: 'Jarvan IV', 24: 'Jax', 126: 'Jayce', 202: 'Jhin', 222: 'Jinx', 145: "Kai'Sa", 429: 'Kalista', 43: 'Karma', 30: 'Karthus', 38: 'Kassadin', 55: 'Katarina', 10: 'Kayle', 141: 'Kayn', 85: 'Kennen', 121: "Kha'Zix", 203: 'Kindred', 240: 'Kled', 96: "Kog'Maw", 7: 'LeBlanc', 64: 'Lee Sin', 89: 'Leona', 127: 'Lissandra', 236: 'Lucian', 117: 'Lulu', 99: 'Lux', 54: 'Malphite', 90: 'Malzahar', 57: 'Maokai', 11: 'Master Yi', 21: 'Miss Fortune', 82: 'Mordekaiser', 25: 'Morgana', 267: 'Nami', 75: 'Nasus', 111: 'Nautilus', 518: 'Neeko', 76: 'Nidalee', 56: 'Nocturne', 20: 'Nunu & Willump', 2: 'Olaf', 61: 'Orianna', 516: 'Ornn', 80: 'Pantheon', 78: 'Poppy', 555: 'Pyke', 246: 'Qiyana', 133: 'Quinn', 497: 'Rakan', 33: 'Rammus', 421: "Rek'Sai", 58: 'Renekton', 107: 'Rengar', 92: 'Riven', 68: 'Rumble', 13: 'Ryze', 113: 'Sejuani', 235: 'Senna', 875: 'Sett', 35: 'Shaco', 98: 'Shen', 102: 'Shyvana', 27: 'Singed', 14: 'Sion', 15: 'Sivir', 72: 'Skarner', 37: 'Sona', 16: 'Soraka', 50: 'Swain', 517: 'Sylas', 134: 'Syndra', 223: 'Tahm Kench', 163: 'Taliyah', 91: 'Talon', 44: 'Taric', 17: 'Teemo', 412: 'Thresh', 18: 'Tristana', 48: 'Trundle', 23: 'Tryndamere', 4: 'Twisted Fate', 29: 'Twitch', 77: 'Udyr', 6: 'Urgot', 110: 'Varus', 67: 'Vayne', 45: 'Veigar', 161: "Vel'Koz", 254: 'Vi', 112: 'Viktor', 8: 'Vladimir', 106: 'Volibear', 19: 'Warwick', 62: 'Wukong', 498: 'Xayah', 101: 'Xerath', 5: 'Xin Zhao', 157: 'Yasuo', 83: 'Yorick', 350: 'Yuumi', 154: 'Zac', 238: 'Zed', 115: 'Ziggs', 26: 'Zilean', 142: 'Zoe', 143: 'Zyra'}

# update the dictionary when new champions get introduced
with open('./champion.txt', 'r') as file:
    file_content = csv.reader(file, delimiter='\t')
    next(file_content)  # skip header
    for line in file_content:
       champ_dic.update({int(line[1]): line[0]})

# read API-Key File
with open(input_file, 'r') as file:
    api_key = file.read()

# use the riotwatcher modul to get access to the API
# for more informations use: https://riot-watcher.readthedocs.io/en/latest/
lol_watcher = LolWatcher(api_key)

# region set to euw
region = 'euw1'

# the current season not 11 but 13
season = {13}

# print details for check point
print(player_name, api_key, region, season)

# get the data of one player with a specific name and region and then use acccount id, queue and season to
# get the player stats. the queue  should be set of str but only works with a single number
player_record = lol_watcher.summoner.by_name(region, player_name)
player_stats = lol_watcher.match.matchlist_by_account(region,
                                                      encrypted_account_id=player_record['accountId'], queue=queue,
                                                      season=season)

# create output for further analysis
# the extract data is gameid, time, champ, win , kill, death, assists, visionscore, goldearned and farm
f = open(output_file_name, 'w')
f.write('Playername\tgameid\ttime\tchamp\twin\tkills\tdeaths\tassists\tvisionscore\tgoldearned\tfarm\n')
f.close()
# first you go to all matches the player played mostly like the last 100
for i in range(0, len(player_stats['matches'])):
    # then you get the through the match-id the match data
    game_data = lol_watcher.match.by_id(region, player_stats['matches'][i]['gameId'])
    print('math_ind: %i\t' % i)
    # in a match-data there are 10 participants and you search the playername in this match
    for participant_number in range(0, 10):
        game_data_participants = game_data['participants'][participant_number]
        # get the champion-name from the champion dictionary to get the really name
        if game_data_participants['championId'] == player_stats['matches'][i]['champion']:
            champ_name = champ_dic[game_data_participants['championId']]
            with open(output_file_name, 'a') as file:
                file.write('%s\t%i\t%i\t%s\t%s\t%i\t%i\t%i\t%i\t%i\t%i\n' % (player_name,
                                                                             player_stats['matches'][i]['gameId'],
                                                                             game_data['gameDuration'],
                                                                             champ_name,
                                                                             game_data_participants['stats']['win'],
                                                                             game_data_participants['stats']['kills'],
                                                                             game_data_participants['stats']['deaths'],
                                                                             game_data_participants['stats']['assists'],
                                                                             game_data_participants['stats']['visionScore'],
                                                                             game_data_participants['stats']['goldEarned'],
                                                                             game_data_participants['stats']['totalMinionsKilled']))
