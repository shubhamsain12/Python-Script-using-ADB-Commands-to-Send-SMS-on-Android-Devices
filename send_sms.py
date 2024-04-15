
import subprocess
import time

def send_sms(phone_number, message):  
    
    escaped_message = message.replace('$', r'\$').replace('"', r'\"')


    adb_commands = [ 
        f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number}',
        f'adb shell input text "{escaped_message}"',
        'adb shell input keyevent 66',  # Send the message by pressing Enter key
        'adb shell input keyevent 22',  # Move the focus to the send button
        'adb shell input keyevent 22',  # Move the focus to the send button
        'adb shell input keyevent 66',  # Press Enter key to send the message
        # 'adb shell input keyevent 66',
    ]


    for cmd in adb_commands:
        try:
            print(f"Executing command: {cmd}")
            subprocess.run(cmd, shell=True, check=True)
         
            time.sleep(4)  # Increased delay to 2 seconds
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {cmd}")
            print(e)


recipient_number = '+918890066621'  # Replace with the recipient's phone number
sms_text = 'HELLO'  
send_sms(recipient_number, sms_text)




