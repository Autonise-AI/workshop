import requests
import shutil

baseURL = 'https://mayank-git-hub.github.io'

res = requests.get(baseURL + '/web-scrap')

keywords = ['amir', 'aamir']
tag = 'img'
counter = 0

for line in res.text.splitlines():
	found = False

	for keyword in keywords:
		if line.find(keyword) != -1:
			if line.find('<'+tag) != -1:
				start = line.find('src="')+len('src="')
				end = line[start:].find('"') + start
				imgRes = requests.get(baseURL + line[start:end], stream=True)
				with open(f'img_{counter}.png', 'wb') as out_file:
					shutil.copyfileobj(imgRes.raw, out_file)
				counter += 1
				print(baseURL + line[start:end])

