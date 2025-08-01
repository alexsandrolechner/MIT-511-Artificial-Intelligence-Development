# ================================
# pip install ultralytics opencv-python deepface matplotlib tf-keras
# ================================

import os
import cv2
from ultralytics import YOLO
from deepface import DeepFace
import matplotlib.pyplot as plt

# Caminho das imagens
DIRETORIO_IMAGENS = "imagens" 

# Carregar modelo YOLO para detecção de rostos
modelo_yolo = YOLO("yolov8n.pt") 

# Verifica se a pasta existe
if not os.path.exists(DIRETORIO_IMAGENS):
    raise Exception(f"Pasta '{DIRETORIO_IMAGENS}' não encontrada.")

# Loop pelas imagens da pasta
for arquivo in os.listdir(DIRETORIO_IMAGENS):
    caminho_img = os.path.join(DIRETORIO_IMAGENS, arquivo)
    img = cv2.imread(caminho_img)

    if img is None:
        continue

    img = cv2.resize(img, (640, 480))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # =======================
    # DETECÇÃO DE ROSTOS COM YOLO
    # =======================
    resultados = modelo_yolo.predict(img_rgb, verbose=False)
    caixas = resultados[0].boxes.xyxy.cpu().numpy()  # Coordenadas dos rostos

    if len(caixas) == 0:
        print(f"[INFO] Nenhum rosto detectado em {arquivo}")
        continue

    # Loop por cada rosto detectado
    for i, box in enumerate(caixas):
        x1, y1, x2, y2 = map(int, box)
        face = img_rgb[y1:y2, x1:x2]

        # =======================
        # ANÁLISE DE EMOÇÃO COM DEEPFACE
        # =======================
        resultado = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
        emocoes = resultado[0]['emotion']
        dominante = resultado[0]['dominant_emotion']

        print(f"Imagem: {arquivo} | Rosto {i+1} | Emoção dominante: {dominante}")

        # =======================
        # PLOT IMAGEM + GRÁFICO
        # =======================
        x = list(emocoes.values())
        y = list(emocoes.keys())

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        ax1.imshow(face)
        ax1.set_title(f"Emoção: {dominante}", fontsize=12)
        ax1.axis("off")

        ax2.barh(y, x, color="skyblue")
        ax2.set_title("Distribuição de Emoções", fontsize=12)
        ax2.tick_params(labelsize=10)
        plt.tight_layout()
        plt.show()
