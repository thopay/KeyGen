import time, random, string
print("""Formatting:
Numbers    :  ?
Uppercase  :  &
Lowercase  :  .
a-z|A-Z|0-9:  *
Any Symbol :  %""")
qty = int(input("\nNumber of Keys: "))
keyFormat = input("Key Format: ")
output = "output.txt"
output = input("Output File Name: ")
start = time.time()
keys = []
e = string.ascii_letters + '0123456789'
f = '}\/!$%&+-,=(){'
while len(keys) < qty:
    a = ''
    for b in keyFormat:
        if b == "?":
            a += str((random.randint(0,9)))
        elif b == "&":
            a += (random.choice(string.ascii_uppercase))
        elif b == ".":
            a += (random.choice(string.ascii_lowercase))
        elif b == "*":
            a += (random.choice(e))
        elif b == "%":
            a += (random.choice(f))
        else:
            a += (b)
    keys.append(a)
end = time.time()
with open(output, 'w+') as f:
    for key in keys:
        f.write("%s\n" % key)
print("\nFinished in {ftime}".format(ftime=(end - start)))