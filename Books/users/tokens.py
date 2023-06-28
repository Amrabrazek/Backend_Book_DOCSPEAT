from django.contrib.auth.tokens import PasswordResetTokenGenerator  

class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            str(user.pk) + str(timestamp) + str(user.is_active)  
        )  

class PasswordTokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            str(user.pk) + str(timestamp) + str(user.is_reset)  
        )  

account_activation_token = TokenGenerator()  
password_reset_token = PasswordTokenGenerator()
