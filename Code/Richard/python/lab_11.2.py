print("Rot Cipher")
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase

english = {
0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m',
13:'n', 14:'o',15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z' 
}

#lower_list = list(lower)

message = input("write a message to encode\n>")

#message = "abcNOPxyZ" #test message to get beginning, middle, and end of range values.
message = message.lower()

rot = int(input("choose offset number(1-24)\n>"))
while rot > 25: #nice try shananniganizers...
    rot -= 25

#rot = 5
#raw = list(message)

def get_key (string): #string converted to alphabet index
    message_key = []
    for char in string:
        if char in lower:
            message_key.append(lower.find(char))
        else:
            message_key.append(char)
    
    return message_key

def encode (message_key, rot): #index changed by rotational value difference and new index used for code letter
    cypher=[]
    rot_message =[]
    for num in message_key:
        num += rot
        if num > 25:
            num -= 25
        cypher.append(num)
        
    for key in cypher:
        rot_message.append(lower[key])

    return ''.join(rot_message)

this = get_key(message)
#print(this)
print(f" the coded message is:{encode(this,rot)}")