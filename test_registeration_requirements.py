from testd4.registeration import Registration
######################################################################
# In a real life implementation, this class will deal with HTTP 
# requests and responses to determine successful user registration
# For the sake of this deliverable, we have mocked the expected HTTP 
# request/response values to showcase the desired functionality 
# and address the requirements

# REQUIREMENTS TESTED: 
######################################################################

#Requirement #7.1.1 - Account creation requirements 
def test_password_complexity():
    invalid_passwords = ["invalid", "password", "bad", "evil", "good", "lukewarm"]

    for password in invalid_passwords:
        reg = Registration()
        assert reg.verify_password_complexity(password) == True , "Invalid password supplied"

def test_email_validity():
    invalid_emails = ["not", "a", "valid", "email"]  

    for email in invalid_emails:
        reg = Registration()
        assert reg.verify_email(email) == True , "Invalid password supplied"
def test_phonenumber_validity():
    invalid_phone_numbers = ["asdsa", "121", "00000"]

    for phonenumber in invalid_phone_numbers:
        reg = Registration()
        assert reg.verify_phone_number(phonenumber) == True , "Invalid phone number supplied"
#Requirement 7.1.2 and 7.1.2.1
def test_oauth_auth_code_flow():
    invalid_http_responses = ["error", "invalid_credentials"]

    for response in invalid_http_responses:
        reg = Registration()
        assert reg.verify_oauth_authorization_code_flow(response) == True, "Invalid HTTP response received"

#Requirement 7.1.2.1
def test_redirect_after_login():
    invalid_redirect_uri = ["google.com", "donaldjtrump.com"]

    for response in invalid_redirect_uri:
        reg = Registration()
        assert reg.verify_oauth_authorization_code_flow(response) == "https://www.dinnerisserverdanddelivered.com", "Invalid redirect detected"
#Requirement 7.1.2.3
def test_oauth_token_received():
    invalid_http_responses = ["invalid_user", "access_denied"]

    for response in invalid_http_responses:
        reg = Registration()
        assert reg.verify_oauth_token_received(response) == True, "Invalid HTTP response received"

#Requirement 7.2.1 - Account Login
def test_login_credentials():
    invalid_credentials = {"invalid_username","invalid_password"}
    reg = Registration()
    assert reg.check_credentials(invalid_credentials) == True, "Invalid credentials, login not successful!"

#Requirement 7.2.1.1
def test_successful_login():
    reg = Registration()
    user = None 
    assert reg.successful_login(user) == True, "login not successful"

#Requirement 7.2.1.2 - can't test send password reset email functionality
def test_relogin_attempts():
    count = 6
    reg = Registration()
    assert reg.lock_account_after_5_login_attempts(count) == True, "Account not locked out after more than 5 attempts"

def test_account_locked_error_message():
    invalid_errors = ["Your account is locked", "Thou art banished from thine account"]
    for message in invalid_errors:
        reg = Registration()
        assert reg.display_locked_account_error_message(message) == True, "Account lockout error message not correct!"

#Requirement 7.2.2 - Forgotten Password
def test_forgotten_password_button():
    button = None #UI element needed here, which isn't possible 
    reg = Registration()
    assert reg.check_forgotten_password_button(button) == True, "Forgotten password button not available!"

#Requirement 7.2.3 - Reset Forgotten Password
def test_valid_email_and_phone_for_password_reset_request():
    invalid_phone_numbers = ["lalalala", "hahahaha", "blablablablabla"]
    invalid_emails = ["a@b.com" ,"d@e.com", "x@y.com"]
    for x in range(len(invalid_emails)):
        reg = Registration()
        assert reg.check_email_and_phonenumber(invalid_emails[x], invalid_phone_numbers[x]) == True, "Invalid information supplied for password reset request!"
def test_reset_password_link():
    user = None
    reg = Registration()
    assert reg.generate_password_reset_link(user) == True, "Password reset link not generated!"
