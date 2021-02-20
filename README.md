# lol-stats
A Python-Script for League of Legends Data extraction via API and RiotWatcher

for the usage of the python script i would recommend PyCharm (Community version is free and there is a educational for students) or 
anaconda (both available for windows). Anaconda (https://www.anaconda.com/products/individual) you get a shell like in linux and you 
can create environments with specific imports.

Here are a little tutorial for the script:

	1. Install anaconda (https://www.anaconda.com/products/individual)
	2. create an environment (conda create -n test_environment python=3.7)
		for more info (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
	3. use pip install to install moduls
	4. check if APIKey_file.txt is up to date
	5. cd to the directory where the script and API-Key file is
	5. run script  (python getPlayerStats.py APIKey_file.txt "THD BlackOrl" "Normal")
						filepath of API-key playername	queue	 	

Files in Directory:
            APIKey_file.txt
		    getPlayerStats.py

APIKey_file.txt:

	has only one line with the API-Key
	API-Key available at Riot Developer Site: https://developer.riotgames.com/
	when you logged in with your Riot-Account (LOL-Account)
	with the API-Key you have permission to get the data

getPlayerStats.py:

	python script for data extraction of a LOL-player in the current season in different queue
	Python Imports:
		riotwatcher (https://riot-watcher.readthedocs.io/en/latest/)
		argparser (https://docs.python.org/3/library/argparse.html)
		os (https://docs.python.org/2/library/os.html)
		sys (https://cito.github.io/byte_of_python/read/sys-module.html)

	script can used via shell with the 3 arguments:
		API-Key File location like APIKey_file.txt -> example: ./APIKey_file.txt
		Playername as String -> example: "RandomGuy"
		Queue which you want (Solo,Flex,Normal) -> example "Flex"

	Output is a table in the working directory with the columns: Playername, gameid, time in sec, champion, win, kills, deaths, assists, visionscore, goldearned and farm
	Filename ist the Playername + queue + _data
	Seperator is tabulator
	Note:
		with normal API-Keys you can only achieve 100 requests every 2 mins (https://developer.riotgames.com/) so after 96+-3 Games the 
		request get no further and the programm stopsand need like a few moments to end the request
		the season is define as 13 which is the current season 11
		the region is EUW
