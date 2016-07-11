from firebase import firebase


f = firebase.FirebaseApplication('https://glowing-fire-3217.firebaseio.com/')

result = f.get('music', 2)

t = {"type": ".jpg"}

f.post

print(result)

