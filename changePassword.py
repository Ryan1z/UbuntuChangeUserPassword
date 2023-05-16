import subprocess
import random
import string
import json

def generatePassword(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def changePassword(username, newPassword):
    command = f"echo '{username}:{newPassword}' | sudo chpasswd"
    subprocess.run(command, shell=True)

def generatePasswordTable(numPasswords, passwordLength):
    passwords = {}
    for i in range(numPasswords):
        password = generatePassword(passwordLength)
        passwords[f"Password {i+1}"] = password
    return passwords

username = 'ryan'      #使用者帳號
numPasswords = 5       #密碼表內密碼組數
passwordLength = 10    #密碼長度

#生成密碼表
passwordTable = generatePasswordTable(numPasswords, passwordLength)

with open('passwd.json', 'w', encoding='utf-8') as fp:
    json.dump(passwordTable, fp, indent=4, ensure_ascii=False)

#生成密碼
selectedPassword = random.choice(list(passwordTable.values()))

#修改密碼
changePassword(username, selectedPassword)
result = f"已將使用者 {username} 的密碼修改為: {selectedPassword}"

#密碼修改紀錄 (path需自行調整)
with open('/home/rucker/password/passwdlog.json', 'a', encoding='utf-8') as fp:
    json.dump(result, fp, indent=4, ensure_ascii=False)