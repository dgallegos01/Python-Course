# Making emoji's with dictionaries
message = input(">")
words = message.split(' ') # this will go through a string and apply a character specified, in this case a space, and return a list
print(words) # the output will be: ['Good', 'morning', 'sunshine']

# here is the emoji dictionary
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "🙂",
    ":(": "🙁"
} 
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
# this program may not work if emoji's are not implemented in python