
num = 1
while num < 102:

    f = open(fr"101\{num}\flag.txt", 'r')
    text = f.read()
    a = text.replace("Christmas{fake_flag}", "")
    if a == "":
        print(f"NO {num}")
    
    else:
        print(f"HERE! {num}")
    f.close()
    num += 1