import  random
def signUpData():
    signUp={}
    signUp['username'] = "Adnan Ghaffar"
    signUp['email'] = "AdnanGhaffar%s@gmail.com"%(random.random())
    signUp['password'] = "TestPassword"
    signUp['invalidEmail'] = "AdnanGhaffar.com"
    signUp['shortPassword'] = "asdf"
    signUp['longPassword'] = "TestPasswordTestPasswordTestPassword"
    return signUp
