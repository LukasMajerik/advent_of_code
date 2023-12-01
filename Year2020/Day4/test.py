import re

pattern = re.compile("^#[a-f0-9]+")

hcls = ["#18171d","#be1503",'#ca97a6']

for hcl in hcls:
    print(pattern.fullmatch(hcl))
    if not (pattern.fullmatch(hcl) and len(hcl) == 7):
        print("hcl", hcl)