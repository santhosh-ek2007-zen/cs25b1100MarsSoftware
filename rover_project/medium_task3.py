def encrytred_message(message):
    message=message.upper()
    i=0
    e_message=""
    for ch in message:
        i=i+1
        e_message += chr(ord(ch)-i)
        
    return e_message    
message="ncuw"
print(encrytred_message(message))
