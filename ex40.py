# Notes
# dictionary
# mystuff['apples']

# module
# mystuff.apples()
# print mystuff.tangerine

# class
# thing = MyStuff()
# thing.apples()
# print thing.tangerine

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def delete_a_song():
		self.lyrics = ""
		
	def rewrite_a_song(self, lyrics):
		self.lyrics = lyrics
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["THey rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#-------------------------
# Study Drill

# 1.
love_song = Song(["This song is about love",
				  "Not only for those who are in one",
				  "But also for those who are looking",
				  "And even for those who are hurting"])
				  
love_song.sing_me_a_song()

# 2.			  
separate_variable = ["I'm using my time",
					 "To think about what to write down",
					 "It's starting to take up too much",
					 "So I just wrote anything on my mind"]
					 
my_song = Song(separate_variable)
my_song.sing_me_a_song()
