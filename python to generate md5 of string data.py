import hashlib
result1=hashlib.md5(b'Mathumitha')
print("The byte equivalent of hash is:",end="")
print(result1.digest())
result2="Mathumitha"
result=hashlib.md5(result2.encode())
print("The hexadecimal equivalent of hash is:",end=" ")
print(result.hexdigest())
© 2021 GitHub, Inc.
