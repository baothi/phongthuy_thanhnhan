
def check_login(re):
    userExist = ''
    try:
        userExist = re.session['admin']
    except:
        pass
    print('userExist==========',userExist)
    #go
    if str(userExist) == 'admin':
        return True
    else:
        return False