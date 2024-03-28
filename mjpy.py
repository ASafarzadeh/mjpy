import sys
import os
import argparse
import requests
import json
import time
import random
from urllib.parse import urlparse

APPLICATION_ID = "936929561302675456"  # Discord application ID (For Midjourney)
VERSION = "1166847114203123795"  # Version of the application (Local Discord Application id)
ID = "938956540159881230"  # ID of the bot

CHECK_IMAGES_INTERVAL = 5 # Seconds between checking to see if images are ready
MAX_IMAGE_CHECK_ROUNDS = 30 # How many times should we check for images before timeout
EACH_PROCESS_ROUND_COOLDOWN = 3 # Seconds between each process round

def parser_error(errmsg):
    print(f"Usage: python3 {sys.argv[0]} [Options] use -h for help")
    print(f"Error: {errmsg}")
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + '"cute cats playing football" -t YOUR_TOKEN_HERE')
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('prompt', help="The prompt to be used if the command is imagine")
    parser.add_argument('-g', '--guild-id', help='GUILD_ID', required=True)
    parser.add_argument('-ch', '--channel-id', help='CHANNEL_ID', required=True)
    parser.add_argument('-t', '--token', help='AUTH_TOKEN', required=True)
    parser.add_argument('-v', '--verbose', help='Enable Verbosity and display the process in realtime', nargs='?', default=False)
    parser.add_argument('-o', '--output-dir', help='Where to save the Generated images', nargs='?', default=".")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompt = args.prompt
    token = args.token
    verbose = args.verbose
    output_dir = args.output_dir
    channel_id = args.channel_id
    guild_id = args.guild_id
    seed = str(random.randint(1,4294967294))
    prompt = prompt + " --seed " + seed
    # Send Generation Command
    url = "https://discord.com/api/v9/interactions"
    data = {"type":2,"application_id":APPLICATION_ID,"guild_id":guild_id,"channel_id":channel_id,"session_id":"cannot be empty","data":{"version":VERSION,"id":ID,"name":"imagine","type":1,"options":[{"type":3,"name":"prompt","value":prompt}],"application_command":{"id":ID,"application_id":APPLICATION_ID,"version":VERSION,"default_member_permissions":None,"type":1,"nsfw":False,"name":"imagine","description":"Create images with Midjourney","dm_permission":True,"contexts":None,"options":[{"type":3,"name":"prompt","description":"The prompt to imagine","required":True}]},"attachments":[]},}
    headers = {
        'Authorization': token, 
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, json=data)
    if verbose:
        print("Generation Command Sent.")
    if(response.status_code != 204):
        print(f"Error in Command Execution: {response.text}")
        exit()
    time.sleep(10)
    headers = {
        'Authorization': token,
        "Content-Type": "application/json",
    }
    done = False
    for i in range(MAX_IMAGE_CHECK_ROUNDS):
        if done:
            break
        time.sleep(CHECK_IMAGES_INTERVAL)
        try:
            response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=headers)
            messages = response.json()
            for i in range(0,len(messages)):
                if('--seed ' in messages[i]['content']):
                    content = messages[i]['content']
                    content = content.split("--seed ")[1]
                    content = content.split("**")[0]
                    content = content.replace(" ","")
                    if(content == seed):
                        if(len(messages[i]['components']) > 0):
                            if(verbose):
                                print("TASK READY")
                            message_id = messages[i]['id']
                            choice_image_url = messages[i]['attachments'][0]['proxy_url']
                            components = messages[i]['components'][0]['components']
                            buttons = [comp for comp in components if comp.get('label') in ['U1', 'U2', 'U3', 'U4']]
                            custom_ids = [button['custom_id'] for button in buttons]
                            done = True
                        else:
                            if(verbose):
                                print("Task identified, but not ready")
                            continue
        except Exception as e:
            print(f"Error: {e}")
            exit()
    for custom_id in custom_ids:
        time.sleep(1)
        url = "https://discord.com/api/v9/interactions"
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        data = {"type":3,"guild_id":guild_id,"channel_id":channel_id,"message_flags":0,"message_id":message_id,"application_id":APPLICATION_ID,"session_id":"cannot be empty","data":{"component_type":2,"custom_id":custom_id,}}
        response = requests.post(url, headers=headers, data=json.dumps(data))
    time.sleep(3)
    final_urls = []
    try:
        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=10', headers=headers)
        messages = response.json()
        for i in range(0,len(messages)):
            try:
                if(messages[i]['referenced_message']['id'] == message_id):
                    if(len(messages[i]['components']) > 0):
                        image_url = messages[0]['attachments'][0]['proxy_url'] 
                        final_urls.append(image_url)
            except Exception as e:
                print(f"Error: {e}")
                exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()
    for final_url in final_urls:
        url = urlparse(final_url)
        img_data = requests.get(final_url).content
        with open(os.path.join(output_dir,os.path.basename(url.path)), 'wb') as handler:
            handler.write(img_data)
        if verbose:
            print(f"Saved Generation result to {os.path.join(output_dir,os.path.basename(url.path))}")
    if verbose:
        print("Generation Done.")
    exit()

if __name__ == "__main__":
    main()