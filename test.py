from decouple import config

Password = config("Password", default="oma8900")
Pin = config("Pin", cast=int)

print(Password)
print(Pin, type(Pin))