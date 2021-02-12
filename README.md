# FindAKitten

# How to operate  
(ogarnę to do końca jutro rano - ściągnę to sobie na 2 komputer i zobaczę co dokładnie potrzebuje zrobić zaczynając ze stanu "nie wiem co to python")  
This project is based on  Django v. 3.1.6. & Python v. 3.8.6  
to start you need those and Pycharm installed,   
in Pycharm you need to open terminal in  main FindAKitten folder and run below commands:  
  
python manage.py makemigrations   -> will make migrations    
python manage.py migrate          -> will apply those migrations to db  
python manage.py runserver        -> will start the application  
  
then,  
open browser at http://127.0.0.1:8000/  
  
apart from the roots available from the main root (welcome page)  
you can also go to the admin panel under the root:  
http://127.0.0.1:8000/admin   
there should be created user with  
login: admin  
password: admin   
but if there is not -> please stop the server, and run a following command in the terminal:  
python manage.py createsuperuser   (and follow creator steps). Then runserver again and login on newly created user.  
After authorization you can do the admin stuff (create another users, CRUD operations on entities)  

# Możliwe że przydatna informacja dotycząca uploadu zdjęć  
pod adresem:  
FindAKitten/kotki/views.py   
znajduje się metoda new_imgae_view której argument request zawiera
