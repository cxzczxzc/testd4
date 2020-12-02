import re
class Registration:
    #not implemented
    def create_account(self, email, name, password):
        return None 
    
    def verify_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(regex, email):
            return True
        else:
            return False
    
    def verify_password_complexity(self, password):
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            return True
        else:
            return False 
    def verify_phone_number(self,phonenumber):
        regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        if re.search(regex, phonenumber):
            return True
        else:
            return False

    def sign_up_with_google(self, email):
        return None
    
    def verify_google_login_linked_successfully(self, returncode):
        if returncode == 200:
            return True
        else:
            return False

    ##############################################################
    # THE METHODS BELOW IMPLEMENT THE LINKING WITH GOOGLE USING  #
    # OAuth 2.0 Authorization Grant Flow with OpenID Connect     #
    ##############################################################

    #STEP 1 - Get grant code
    def verify_oauth_authorization_code_flow(self, HTTPresponse):
        success_auth = "code" #in case of successful login the HTTP response will contain a key called 'code' 
        if success_auth in HTTPresponse:
            return True
        else:
            return False
   
    #STEP 2 - redirect to login page (OIDC = OpenID Connect)
    def verify_redirect_from_OIDC(self, HTTPresponse):
        redirect_uri = "https://www.dinnerisserverdanddelivered.com"
        if redirect_uri in HTTPresponse:
            return "Redirect to homepage was successful"
        else:
            return "Return to homepage was not successful, OIDC failed"

    #STEP 3 - receive the OAuth 2.0 access token
    def verify_oauth_token_received(self, HTTPresponse):
        token = "access-token"
        if token in HTTPresponse:
            return "Access token received"
        else:
            return "Access token not received"

    ##############################################################
    # THE METHODS BELOW IMPLEMENT THE LOGIN RELATED FUNCTIONS    #
    ##############################################################

    def check_credentials(self, credentials):
        db_table_with_valid_credentials = {"valid_username": "valid_password"} # database not implemented
        if credentials == db_table_with_valid_credentials:
            return True
        else:
            return False
    #Not possible to implement at all as it requires UI interaction
    def successful_login(self, user):
        return NotImplementedError 
    #Not possible to implement as it requires UI interaction
    def lock_account_after_5_login_attempts(self, count):
        return NotImplementedError
    #Not possible to implement as it requires UI interaction
    def display_locked_account_error_message(self, message):
        return NotImplementedError 
    #Not possible to implement as it requires UI interaction
    def check_forgottem_password_button(self, button):
        return NotImplementedError 

    def check_email_and_phonenumber(self, email, phonenumber):
        valid_email = "big@boss.com" #email and phone number would come from the database, which aren't implemented
        valid_phone = "(905)305-8508"
        if email == valid_email and phonenumber == valid_phone:
            return True
        else:
            return False
    #this method should generate a password reset link for a user
    #user object will be used to do so
    #not implemented because user object doesn't exist
    def generate_password_reset_link(self, user):
        return NotImplementedError
