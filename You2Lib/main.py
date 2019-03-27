from search import Search

API_KEY = "AIzaSyBIcgLwyQ4XPduVze13bojeZBZ5Eg14vhk"

s = Search(API_KEY)
data = s.searchFor('Minecraft')
print(data)