import requests, json,random

'''
:q -> query words| type -> List
'''
headers = {'content-type': 'application/json'}
q = {'q': ['a', 'b']}
#q = {'q':list(map(lambda x:random.choice(['a','b','c','d','e'])+x,['{}'.format(i) for i in range(1000)]))}

res = requests.post("http://47.97.120.25:5550/query", data=json.dumps(q), headers=headers)
print(res.text)
