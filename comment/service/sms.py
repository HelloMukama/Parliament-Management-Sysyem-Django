from sms import send_sms

send_sms(
    'Here is the message',
    '+256778945859',
    ['+256757826294'],
    fail_silently=False
)
