from mapbook_lib.controller import user_info, add_user, remove_users, update_users, get_map
from mapbook_lib.model import users

def main():
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

if __name__=="__main__":
    main()

