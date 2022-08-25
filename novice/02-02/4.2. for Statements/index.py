# words = ["anggur", "apel", "jeruk"]
# for i in words:
#     print(i)

users = {'Nisfi': 'setengah', 'Nuur': 'cahaya', 'Lailatin': 'malam'}
for user, status in users.copy().items():
    if status == 'cahaya':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'setengah':
        active_users[user] = status

print(users)
print(active_users)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)