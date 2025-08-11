s={"name":"aryan","age":16,"marks":90}
print(s)
print(s.keys())
print(s.values())
print(s.get("name"))
print(s.get("address", "Not found"))
s["address"]="MSEB road karad"
print(s)
s.update({"higher school":"SGM Karad"})
print(s)
