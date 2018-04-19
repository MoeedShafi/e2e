def logInData():
    logIn={}
    logIn['email'] = "AdnanGhaffar@gmail.com"
    logIn['invalidEmail'] = "AdnanGhaffargmail.com"
    logIn['password'] = "TestPassword"
    logIn['invalidPassword'] = "Password"
    logIn['sqlInjectionEmail'] = "'or''='"
    logIn['sqlInjectionPassword'] = "'or''='"
    logIn['longEmail'] = "AdnanGhaffarAdnanGhaffarAdnanGhaffarAdnanGhaffarAdnanGhaffar@gmail.com"
    return logIn
