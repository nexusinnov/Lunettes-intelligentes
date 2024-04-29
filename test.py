import cv2
import numpy as np

# Dictionnaire contenant les plages HSV de différentes couleurs
colors = {
   'blanc': [(0, 0, 200), (255, 30, 255)],  
    'noir': [(0, 0, 0), (255, 30, 50)],  
    'rouge': [(160, 100, 100), (180, 255, 255)], 
    'jaune': ([15, 150, 20], [35, 255, 255]),
    'bleu': ([90, 60, 0], [121, 255, 255]),
    'vert': ([35, 50, 50], [85, 255, 255]),
    'orange': ([10, 100, 20], [20, 255, 255]),
    'marron': ([10, 100, 20], [30, 255, 150]),
    'rose': ([140, 50, 50], [165, 255, 255]),
    'violet': ([125, 100, 50], [155, 255, 255])
}

# Fonction pour détecter les couleurs dans l'image
def detect_color(frame, color_name, lower, upper):
    # Convertir l'image de BGR à HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Appliquer le masque pour la couleur spécifique
    mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
    
    # Trouver les contours dans le masque
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Parcourir les contours trouvés
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Filtrer les petits contours
            # Obtenir les coordonnées du rectangle englobant
            x, y, w, h = cv2.boundingRect(contour)
            
            # Dessiner un rectangle autour de la couleur détectée
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Afficher le nom de la couleur au-dessus du rectangle
            cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Imprimer les coordonnées de la couleur détectée dans la console
            print(f"{color_name} détecté à x={x}, y={y}")
    
    return frame

# Capturer la vidéo de la webcam
video_capture = cv2.VideoCapture(0)

# Vérifier que la caméra a été ouverte
if not video_capture.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

while True:
    # Capturer une frame de la vidéo
    ret, frame = video_capture.read()

    # Vérifier si la frame a été capturée avec succès
    if not ret:
        print("Erreur: Impossible de lire la frame.")
        break

    # Détecter les couleurs définies dans le dictionnaire
    for color_name, (lower, upper) in colors.items():
        frame = detect_color(frame, color_name, lower, upper)

    # Afficher la frame avec la détection des couleurs
    cv2.imshow('Detection de couleurs', frame)

    # Si l'utilisateur appuie sur 'q', arrêter la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres OpenCV
video_capture.release()
cv2.destroyAllWindows()
