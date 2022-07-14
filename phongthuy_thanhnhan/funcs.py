
def check_login(re):
    userExist = ''
    try:
        userExist = re.session['admin']
    except:
        pass
    #go
    if userExist == 'admin':
        return True
    else:
        return False