import os
import sys
import time
import requests
import api_keys


HEADER = {'Authorization': f'token {api_keys.GITHUB_API_KEY}'}


def hard_work(a_url):
    sys.stdout.write(f'{__name__}/{os.getppid()}/{os.getpid()} gets data from {a_url}\n')
    r = requests.get(a_url, headers=HEADER)
    time.sleep(3)
    sys.stdout.write('Done')
    return [(contrib['login'], contrib['contributions'],
             contrib['html_url']) for contrib in r.json()]


if __name__ == '__main__':
    sys.stdout.write(str(hard_work(sys.argv[1])))
