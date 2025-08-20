def form(username,password):
    if isinstance(username, str) and (len(password) > 8):
        return True
    else:
        return False
    

