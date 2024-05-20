import face_auth
import os

if __name__ == "__main__":
    
    name = input("Введіть ваше ім'я: ")
    
    # Шлях до зареєстрованого обличчя
    registered_face_path = f'registered/{name}.jpg'

    # Шлях до зображення аутентефікації
    test_image_path = f'auth/{name}_auth.jpg'
    
    
    if not os.path.exists(registered_face_path):
        print("Користувача з таким ім'ям не існує - зареєструйтесь.")
        face_auth.register_face(name)
    
    face_auth.capture_auth_image(name)

    
    result, image, face_locations = face_auth.recognize_face(registered_face_path, test_image_path)
    
    if result:
        face_auth.show_face_location(image, face_locations)
    