users:list=[
    {"name":'Kasia','location':'Warszawa','posts':3},
    {"name":'Karolina','location':'Warszawa','posts':5},
    {"name":'Sylwia','location':'Warszawa','posts':2},
]
for user in users:
    print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował tyle {user['posts']} postów ')
