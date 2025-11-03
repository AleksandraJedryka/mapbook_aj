import requests
from bs4 import BeautifulSoup
users:list=[
    {"name":'Kasia','location':'Warszawa','posts':3,"img_url":""},
    {"name":'Karolina','location':'Kraków','posts':5,"img_url":""},
    {"name":'Sylwia','location':'Wrocław','posts':2,"img_url":""},
]
def user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował tyle {user['posts']} postów ')


def add_user(users_data:list)->None:
    name:str=input("Podaj imie nowego znajomego: ")
    location:str=input("Podaj nazwe miejscowosci: ")
    posts:int=int(input("Podaj liczbę postów: "))
    img_url:str=input("Wprowadz adres url zdjęcia: ")
    users_data.append({"name":name,"location":location,"posts":posts, 'img_url':img_url})

def remove_users(users_data:list)-> None:
        tmp_name: str = input("podaj imie użytkownika do usuniecia ze znajomych: ")
        for user in users_data:
            if user["name"] == tmp_name:
                user.remove(user)

def update_users(users_data:list)->None:
    tmp_name:str=input("podaj imie użytkownika do aktualizacji: ")
    for user in users_data:
        if user["name"]==tmp_name:
            user['name']=input("podaj nowe imie uzytkownika: ")
            user['location']=input("podaj nowa miejscowos")
            user['posts']=input("podaj nowe miejscowos")


def get_coordinates(city_name:str)->list:
    url:str=f"https://pl.wikipedia.org/wiki/{city_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0.0.0 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    #print(response.text)
    response_html=BeautifulSoup(response.text,"html.parser")
    #print(response_html.prettify())
    response_html.select(".latitude")
    latitude=float(response_html.select(".latitude")[1].text.replace(',','.'))
   # print(latitude)
    longitude=float(response_html.select(".longitude")[1].text.replace(',','.'))
   # print(longitude)
    return[latitude,longitude]
#print(get_coordinates("Wrocław"))

def get_map(users_data:list)->None:

    import folium
    m=folium.Map(location=[52.23,21.0], zoom_start=6)

    for user in users_data:

        folium.Marker(
            location=get_coordinates(user["location"]),
            tooltip="Click me!",
            popup=f"<h4>user: {user["name"]}</h3> {user["location"]} {user["posts"]},<img src={user['img_url']}alt='1'/>",
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("notatnik.html")

while True:
  print("=================menu=================")
  print("0. Wyjście z programu")
  print("1. Wyświetlanie aktywności znajomych")
  print("2. Dodaj znajomego")
  print("3. Wyjście z programu")
  print("4. Wyjście z programu")
  print("5. Generuj mape")
  print("======================================")
  tmp_choice:int=int(input("wybierz opcje menu:"))
  if tmp_choice==0:
      break
  if tmp_choice==1:
        print("wybrano funkcje wyswietlania aktywnosci znajomych")
        user_info(users)
  if tmp_choice==2:
       print("wybrano funkcje dodawania znajomych")
       add_user(users)
  if tmp_choice==3:
     print("wybrano funkcje usuwania znajomych")
     remove_users(users)
  if tmp_choice==4:
      print("wybrano funkcje aktualizacje danych znajomych")
      update_users(users)
  if tmp_choice==5:
      print("wybrano funkcje wyświetlania mapy")
      get_map(users)



