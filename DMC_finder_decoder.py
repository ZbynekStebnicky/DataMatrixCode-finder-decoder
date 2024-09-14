import cv2
from pylibdmtx import pylibdmtx

# Načtení obrázku z lokálního souboru
image_path = r'C:\Users\stebn\Documents\Ch\DMC\images.jpg'  # Nahraď cestou k obrázku
image = cv2.imread(image_path)

# Konverze obrázku na odstíny šedi
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Použití pylibdmtx pro dekódování DataMatrix kódu
decoded_objects = pylibdmtx.decode(gray)

# Výpis dekódovaných dat a zvýraznění oblasti
if decoded_objects:
    for obj in decoded_objects:
        # Získání dekódovaných dat
        decoded_data = obj.data.decode('utf-8')
        print(f"Decoded Data: {decoded_data}")
        
        # Získání souřadnic rohů DataMatrix kódu
        points = obj.rect
        
        # Vykreslení obdélníku kolem detekované oblasti
        x, y, w, h = points[0], points[1], points[2], points[3]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Vložení dekódovaného textu do obrázku
        cv2.putText(image, decoded_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
else:
    print("Kód nebyl dekódován.")

# Zobrazení obrázku s detekovanými obdélníky
cv2.imshow('Decoded DataMatrix', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
