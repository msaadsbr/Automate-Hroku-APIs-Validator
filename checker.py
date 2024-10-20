import subprocess, sys

with open(sys.argv[1], "r") as reader:
        lines = reader.readlines()
        for line in lines:
                key = "HRKU-"+line.split()[-1]
                result = subprocess.run([f'curl -X POST https://api.heroku.com/apps -H "Accept: application/vnd.heroku+json; version=3" -H "Authorization: Bearer {key}"'], shell=True)
                print(f"{key}: ")
                result.stdout
