import requests

print("Test the aaaaaaaaaabot")


r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)

print("run another file.")