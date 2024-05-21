import face_recognition
import cv2
import os

# Function to capture the face and save the image
def register_face(title):
    cap = cv2.VideoCapture(0)
    
    result = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('[FACE AUTH] Register Face - Press "s" to save', frame)
        
        key = cv2.waitKey(1)
        if key == ord('s'):
            os.makedirs('registered', exist_ok=True)
            cv2.imwrite(f'registered/{title}.jpg', frame)
            print(f"[FACE AUTH] Face registered as '{title}.jpg'")
            result = True
            break
        elif key == ord('q'):
            print("[FACE AUTH] Registration cancelled")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    return result

# Function to capture a auth image
def capture_auth_image(title):
    cap = cv2.VideoCapture(0)
    
    result = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('[FACE AUTH] Authentication - Press "s" to authenteficate', frame)
        
        key = cv2.waitKey(1)
        if key == ord('s'):
            os.makedirs('auth', exist_ok=True)
            cv2.imwrite(f'auth/{title}_auth.jpg', frame)
            print(f"[FACE AUTH] Auth image saved as '{title}_auth.jpg'")
            result = True
            break
        elif key == ord('q'):
            print("[FACE AUTH] Capture canceled")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    return result

# Function for face recognition
def recognize_face(known_face_path, unknown_face_path):
    # Load a known image and get its encoding
    known_image = face_recognition.load_image_file(known_face_path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    
    # Load unknown image
    unknown_image = face_recognition.load_image_file(unknown_face_path)
    rgb_image = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)

    # Detect face in unknown image
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
    
    # Compare faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
        
        if matches[0]:
            print("[FACE AUTH] Face recognized!")
            return (True, rgb_image, face_locations)
        else:
            print("[FACE AUTH] Face not recognized.")
            return (False, rgb_image, face_locations)

# Function for display a frame with a face
def show_face_location(image, face_locations):
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()