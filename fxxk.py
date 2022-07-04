# *- encode: utf-8 *-#

import json
import re

import requests

cookies = 'lv=1; fid=1731; _uid=122949003; uf=b2d2c93beefa90dc2c46d4bf8df48760dc07ffb438a63da819ee9a7bae05c0022de67a422d2222a58929ca06b7c918e0913b662843f1f4ad6d92e371d7fdf644d12592c48efd7260fd68be96b6183b1ab7823ef79f0e66fca52a2c1113b9d071fc48188056b524b0; _d=1656946723162; UID=122949003; vc=1E2A1D7B0181457264DF839EBE9A59BD; vc2=FB3E82B6E4470FDF22DC133E8D40D3E9; vc3=Y9svTTgTz7DVlQB7iroNQyCLrYApq1M2JwWI2Vj9lCKP/gdzpxDZM/0E1h2cvjzUziH/WSeCZI+vufbgokpF0O1Z2XWjS6Ac/iPwIOrMSEPmn9mYpAyFJt59yz/TjM9AmNrV587lsxCh7upH6HKrglmIUrxq9ijn5xifQxilRgc=18b097746ba155adc337e547ff00105a; xxtenc=ce5279638a2585f9242021d889e6a0c2; DSSTASH_LOG=C_38-UN_491-US_122949003-T_1656946723164; source=""; spaceFid=1731; spaceRoleId=3; tl=1; INGRESSCOOKIE=1656946749.142.43376.259811; route=9a367df5abdf1b9752160e078f1dbaf0'
g = re.match(r'.*fid=(\d*);.*_uid=(\d*);.*', cookies)
fid, uid = g.group(1), g.group(2)

headers = {
    'cookie':
    cookies,
    'Host':
    'newes.chaoxing.com',
    'Referer':
    f'http://newes.chaoxing.com/newesReception/ratedHome?uid={uid}&formid=0&roleid=3&rolename=%E5%AD%A6%E7%94%9F&state=1731',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

resp = requests.get(
    f'http://newes.chaoxing.com/newesReception/ratedHome?uid={uid}&formid=0&roleid=3&rolename=%E5%AD%A6%E7%94%9F',
    headers=headers)

resp = requests.get(
    f'http://newes.chaoxing.com/newesReception/ajaxRatedHome?uId={uid}&fid={fid}&questionnaireType=0&courseInfo=&currentPage=2',
    headers=headers)
data = resp.content.decode('utf-8')
items = re.findall(r'questionnaireInfo\((\d*),(\d*),(\d*)\)', data)

pc = 4
for i in range(1, int(pc)):
    resp = requests.get(
        f'http://newes.chaoxing.com/newesReception/ajaxRatedHome?uId={uid}&fid={fid}&questionnaireType=0&courseInfo=&currentPage={pc+1}',
        headers=headers)
    print(resp.content.decode('utf-8'))
    data = json.loads(resp.content.decode('utf-8'))['html']
    items.append(re.findall(r'questionnaireInfo\((\d*),(\d*),(\d*)\)', data))

for item in items:
    try:
        alreadyId, grantId, questionnaireId = item[0], item[1], item[2]
        d = {
            'uId': (None, uid),
            'fid': (None, fid),
            'questionnaireId': (None, questionnaireId),
            'alreadyId': (None, alreadyId),
            'grantId': (None, grantId),
            'groupTargetIds': (None, '573048'),
            '573048_type': (None, '1'),
            '573048_chooseSetUp': (None, '1'),
            '573048': (None, '1_1.0'),
            'groupTargetIds': (None, '573049'),
            '573049_type': (None, '1'),
            '573049_chooseSetUp': (None, '1'),
            '573049': (None, '1_1.0'),
            'groupTargetIds': (None, '573050'),
            '573050_type': (None, '1'),
            '573050_chooseSetUp': (None, '1'),
            '573050': (None, '1_1.0'),
            'groupTargetIds': (None, '573051'),
            '573051_type': (None, '1'),
            '573051_chooseSetUp': (None, '1'),
            '573051': (None, '1_1.0'),
            'groupTargetIds': (None, '573052'),
            '573052_type': (None, '1'),
            '573052_chooseSetUp': (None, '1'),
            '573052': (None, '1_1.0'),
            'groupTargetIds': (None, '573053'),
            '573053_type': (None, '1'),
            '573053_chooseSetUp': (None, '1'),
            '573053': (None, '1_1.0'),
            'groupTargetIds': (None, '573054'),
            '573054_type': (None, '1'),
            '573054_chooseSetUp': (None, '1'),
            '573054': (None, '1_1.0'),
            'groupTargetIds': (None, '573055'),
            '573055_type': (None, '1'),
            '573055_chooseSetUp': (None, '1'),
            '573055': (None, '1_1.0'),
            'groupTargetIds': (None, '573056'),
            '573056_type': (None, '1'),
            '573056_chooseSetUp': (None, '1'),
            '573056': (None, '1_1.0'),
            'groupTargetIds': (None, '573057'),
            '573057_type': (None, '1'),
            '573057_chooseSetUp': (None, '1'),
            '573057': (None, '1_1.0'),
            'groupTargetIds': (None, '573058'),
            '573058_type': (None, '1'),
            '573058_chooseSetUp': (None, '-1'),
            '573058': (None, '1'),
            'groupTargetIds': (None, '573059'),
            '573059_type': (None, '4'),
            '573059_chooseSetUp': (None, '1'),
            'jumpInfo': (None, ''),
            '573059': (None, '%E6%97%A0'),
            'saveType': (None, '2'),
        }
        response = requests.post(
            'http://newes.chaoxing.com/newesReception/saveQuestionnaire',
            files=d,
            headers=headers)
        print(f'{response.status_code}: {response.content.decode("utf-8")}')
    except Exception as err:
        pass
