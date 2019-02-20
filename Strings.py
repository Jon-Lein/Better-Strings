import re
import sys

def is_special_name(name):
    if name.find('.') >= 0:
        if name[name.find('.'):] in extensions:
            print(name + " File Extension")
        elif name[name.find('.'):] in domains:
            print(name + " Domain Name")
        elif ip.match(name):
            print(name + " Ip Address")

    else:
        return False

    return True


# read file of extensions, create list
extensions = open('Extensions.txt', 'r')
extensions = extensions.read().split('\n')

# read file of extensions, create list
domains = open('Domains.txt', 'r')
domains = domains.read().split('\n')

# regular expressions
ip = re.compile('\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')


# vars, to be replaced with cmd line options
file_path = sys.argv[1]
min_str_len = 3

file = open(file_path, 'rb')

data = []
for i in file.read():
    data.append(i)

i = 0
while i < len(data):
    if data[i] == 0: # find null byte
        # go through data reverse until bytes arent ascii printable (32 - 126)
        save_i = i
        string = []

        i -= 1
        j = data[i]

        while j >= 32 and j <= 126:
            string.append(chr(j))

            i -= 1
            j = data[i]

        # join arry into string and reverse
        string = ''.join(reversed(string))

        if len(string) >= min_str_len:
            # print(string)
            is_special_name(string)




        # return i to the value before checking a null byte
        i = save_i
    i += 1

