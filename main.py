users:list=[
    {"name":'Kasia','location':'Warszawa','posts':3},
    {"name":'Karolina','location':'Warszawa','posts':5},
    {"name":'Sylwia','location':'Warszawa','posts':2},
]
def user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował tyle {user['posts']} postów ')

while True:
  tmp_choice:int=int(input("wybierz opcje menu:"))
  if tmp_choice==0:
      break
  if tmp_choice==1:
        print("wybrano funkcje wyswietlania aktywnosci znajomych")
        user_info(users)
  if tmp_choice==2:
       print("wybrano funkcje dodawania znajomych")
  if tmp_choice==3:
     print("wybrano funkcje aktualizowania znajomych")




