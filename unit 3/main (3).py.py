#Implement a class called Player that represents a cricket player.  The Player class should have a method called play() which prints "The player is playing cricket.  Derive two classes, Batsman and Bowler, from thhe Player class.  Override the play() method in each derived class to print bowler is bowlin", respectively.  Write a program to create objects of bith the Batsman and Bowler classes and call the play() method for each object. #


#Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class Batsman 
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class Bowler
class Batsman(Player):
  def play(self):
    print("The bowler is bowling.")

#Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play() method for each object
batsman.play()
bowler.play()