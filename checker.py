import sys
import requests

def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)

print_colored(
"""
██████╗ ██╗   ██╗██╗     ██╗  ██╗     █████╗ ██████╗ ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██║   ██║██║     ██║ ██╔╝    ██╔══██╗██╔══██╗██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║     █████╔╝     ███████║██████╔╝██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔══██║██╔═══╝ ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝███████╗██║  ██╗    ██║  ██║██║     ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""", "blue"
)
print_colored(
"                                                                                                 made by msaadsbr"
, "yellow")

# Reading API keys from a file provided as a command-line argument
with open(sys.argv[1], "r") as reader:
    lines = reader.readlines()
    for line in lines:
        api_key = line.strip().split()[-1]
        if api_key.startswith("HRKU-"): api_key = api_key[5:]
        print(f"<------------- Key: {api_key} ------------------>")

        key1 = f"HRKU-{api_key}"

        # Set common headers for the requests
        headers1 = {
            'Accept': 'application/vnd.heroku+json; version=3',
            'Authorization': f'Bearer {key1}'
        }

        headers2 = {
            'Accept': 'application/vnd.heroku+json; version=3',
            'Authorization': f'Bearer {api_key}'
        }

        # First POST request with modified key
        response1 = requests.post('https://api.heroku.com/apps', headers=headers1)
        output1 = response1.text

        # Second POST request with original key
        response2 = requests.post('https://api.heroku.com/apps', headers=headers2)
        output2 = response2.text

        # Check for unauthorized status in both outputs
        if "unauthorized" in output1 and "unauthorized" in output2:
            print_colored("[-] Your Key Is Invalid!", "red")
        else:
            print_colored("[+] Possibly Your Key is Valid!!", "green")
            if "unauthorized" not in output1:
                print(output1)
                print("\n")
            else:
                print(output2)
                print("\n")
