# Script for Analysis of the output of getPlayerStats.py

# set Path to the directory where the script + output lays
setwd("./")

filename <- "RandomGuy_flex_data.txt"

player_df <- read.table(file = filename, sep = "\t", header = TRUE)

# sort out remakes; time < 4min (240 sec)

player_df <- player_df[which(player_df$time>240),]

number_games <- nrow(player_df)

distribution <- as.data.frame(table(player_df$champ))[which(as.data.frame(table(player_df$champ))$Freq > number_games/20),]

distribution$Freq <- distribution$Freq*100/number_games

rest <- 100 - sum(distribution$Freq)

# create a separate window with a pie plot for visualisation of the champs played
x11()
pie(x = c(distribution$Freq,rest),border = 1, labels = paste(round(c(distribution$Freq,rest),2),"%"), main = paste(filename), col = rainbow(length(c(distribution$Freq,rest))))
legend("topright", c(as.character(distribution$Var1),"Rest"), fill = rainbow(length(c(distribution$Freq,rest))) )
