n = int(input())

company = {}

for i in range(n):
    name, state = input().split()
    if state == "enter":
        company[name] = "enter"
    else:
        del company[name]

company = sorted(company.keys(), reverse=True)

for name in company:
    print(name)