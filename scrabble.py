letters = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O",
     "P", "Q", "R", "S", "T",
     "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#Use zip() on letters and points arrays to create a dictionary that will map each letter to a point, save to a new variable
letters_points = {letter: point for letter, point in zip(letters, points)}
#print(letters_points)

#Some scrabble tiles can be blanks, add a key:value to letter_points to reflect this
letters_points[" "] = 0
#print(letters_points)

#loop thru letters array, for each letter, add the corresponding point value from letters_points to a new total
def score_tracker(word):
    total_per_letter = 0
    for letter in word:
        total_per_letter += letters_points.get(letter, 0)
    return total_per_letter
#Test function
#print(score_tracker("INUENDO"))

#Create a new dictionary that lists players and the words they played
words_per_player = {}
words_per_player.update({
    "Jonah": ["CELLPHONE", "APPLE", "SOCCER", "OPEN"],
    "Alexis": ["CALLER", "EMAIL", "ANNOYED", "DOCUMENT"],
    "Dictionary_guy": ["VAGARY", "GUMPTION", "DIATRIBE", "KINDRED"],
    "Professor": ["SIMULTANEOUS", "ANGER", "EXIT", "AREOPLANE"]
})
#print(words_per_player)

#new dictionary that will list each player and their total points, see for loop
players_points = {}

#Iterate thru words_per_player dictionary to get each player and the words they played. 
#Create a new variable with a value of 0. This variable will store each player's points
for player, words in words_per_player.items():
    points_per_player = 0
    #Inner loop that iterates words values and performs score_tracker() on each. 
    for word in words:
        points_per_player+= score_tracker(word)
    #make each player a key in players_points with the value being points in points_per_player
    players_points["player"] = points_per_player
    #print(points_per_player)
    print(players_points)

