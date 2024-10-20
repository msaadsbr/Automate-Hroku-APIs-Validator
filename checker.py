import subprocess
import sys

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
,"yellow")

# Reading API keys from a file provided as a command-line argument
with open(sys.argv[1], "r") as reader:
    lines = reader.readlines()
    for line in lines:
        api_key = line.strip().split()[-1]
        if api_key.startswith("HRKU-"): api_key = api_key[5:]
        print(f"<------------- Key: {api_key} ------------------>")

        key1 = f"HRKU-{api_key}"

        # First curl request with the modified key
        result1 = subprocess.run(
            ['curl', '-X', 'POST', 'https://api.heroku.com/apps',
            '-H', 'Accept: application/vnd.heroku+json; version=3',
            '-H', f'Authorization: Bearer {key1}'],
            capture_output=True, text=True
        )

        # Second curl request with the original key
        result2 = subprocess.run(
            ['curl', '-X', 'POST', 'https://api.heroku.com/apps',
            '-H', 'Accept: application/vnd.heroku+json; version=3',
            '-H', f'Authorization: Bearer {api_key}'],
            capture_output=True, text=True
        )

        output1 = result1.stdout
        output2 = result2.stdout


        # Check for unauthorized status in both outputs
        if "unauthorized" in output1 and "unauthorized" in output2:
            print_colored("[-] Your Key Is Invalid!", "red")
        else:
            print("[+] Possibly Your Key is Valid!!", "green")
            if "unauthorized" not in output1:
                print(output1)
                print("\n")
            else:
                print(output2)
                print("\n")
