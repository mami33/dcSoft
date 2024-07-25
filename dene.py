d = dict()
co=""

for i in range(5):
    co = co + (d.get("se") or "a")
    d.update({"se": co})




print(d)