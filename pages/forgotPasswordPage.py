from common.config import *
def forgotPasswordPageData():
    data={}
    data['forgotPasswordUrl']= '%s/resetPassword?email='%(mainUrl)
    data['forgotPasswordRedirectUrl']= '%s/?msg=reset-password-success'%(mainUrl)
    data['errors']= '_1luqbfTq0W7taCUy54EGCv'
    data['forgotPasswordLink']= '_33xQY66Mz9X3QKwAro3a4Q'
    data['forgotPasswordButton']= 'btn-fancy-round'
    return data