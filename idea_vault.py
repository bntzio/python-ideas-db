from sys import argv
import datetime
# from os.path import exists

script, filename = argv

mylist = [] 
today = str(datetime.date.today())
mylist.append(today)

print "================================"
print "* Welcome to Idea Vault (beta) *"
print "================================"
print "The vault is: %s (where the ideas you type in will be stored)" % filename
print "Today is %s" % mylist
print "======================================================================="

# print "Does the idea database file exists? " % exists(filename)

target = open(filename, 'a')

idea = raw_input("What's your big idea? \n")

print "Hit ENTER to save the idea, or CTRL + C to cancel."
raw_input('> ')

target.write('\n')
target.write("===================================================")
target.write('\n')
target.write(idea + '\n' + today)
target.write('\n')
target.write("===================================================")
target.write('\n')

print "Done! it's saved."
print "The actual file %s is %d bytes long." % (filename, len(filename))

see_ideas = raw_input("Would you like to see your stored ideas? (yes/no) ")

if see_ideas == "yes":
	target.close()
	open_db = open(filename, 'r')
	read_ideas = open_db.read()
	print read_ideas
	open_db.close()
else:
	print "Ok! See you later!"
	target.close()

# despues agregar date and time (datetime())

