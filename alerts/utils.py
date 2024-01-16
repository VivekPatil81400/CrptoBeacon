from django.core.mail import send_mail

def send_welcome_email(user_email, username):
    subject = 'Welcome to Your App'
    message = f'Hello {username},\n\nThank you for joining Cryptobeacon!\n\nBest regards,\nCryptobeacon Team'
    from_email = 'Cryptobeacon@gmail.com'
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
