import requests

url = 'https://www.aftershockpc.com/welcome/products/desktops'

r = requests.get(url)

print(r.text)

print("Status Code:")

print("\t*",r.status_code)

h = requests.head(url)

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# Display Useragent Mobile
headers = {
    'User-Agent' :'Mobile'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)



