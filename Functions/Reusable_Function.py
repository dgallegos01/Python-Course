# we are gonna convert our Emoji program into a function
# Here is the original code:
"""
message = input(">")
words = message.split(' ') 
print(words) 

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
"""

# Now here is the code as the function:
def emoji_converter(meeage):
    words = message.split(' ') 
    print(words) 

    message = input(">")
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    } 
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))