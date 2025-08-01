
## 📌 README.md

```markdown
# MIT-511 Artificial Intelligence Development - Reconhecimento de Emoções

Este projeto foi desenvolvido como parte do curso **MIT-511 - Artificial Intelligence Application Development**.  
O objetivo é criar um sistema de **Reconhecimento de Emoções em Imagens Faciais** utilizando **YOLOv8** para detecção de rostos e **DeepFace** para classificação de emoções.

---

## 🎯 Objetivo do Projeto

- Detectar rostos em imagens usando **YOLOv8**.
- Classificar a emoção dominante de cada rosto (ex.: feliz, triste, neutro, raiva, surpresa).
- Exibir as imagens processadas com gráficos mostrando a distribuição das emoções.

---

## 🧠 Tecnologias Utilizadas

- **Python 3.12**
- **OpenCV** (processamento de imagens)
- **YOLOv8 (Ultralytics)** (detecção de rostos)
- **DeepFace** (classificação de emoções)
- **Matplotlib** (visualização)
- **TensorFlow/Keras**

---

## 📂 Estrutura do Projeto

```
├── imagens/                # Pasta com imagens de teste
├── main.py                 # Script principal do projeto
├── yolov8n.pt              # Pesos YOLOv8 (modelo pré-treinado)
├── README.md               # Este arquivo
└── .venv/                  # Ambiente virtual Python

````

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/alexsandrolechner/MIT-511-Artificial-Intelligence-Development.git
cd MIT-511-Artificial-Intelligence-Development
````

### 2️⃣ Criar ambiente virtual e instalar dependências

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

pip install ultralytics opencv-python deepface matplotlib tf-keras
```

### 3️⃣ Adicionar imagens para teste

* Coloque suas imagens na pasta `imagens/`.

### 4️⃣ Rodar o script

```bash
python main.py
```

---

## 📊 Saídas do Projeto

* A cada imagem processada, o sistema:

  * Detecta os rostos com **YOLOv8**.
  * Classifica as emoções usando **DeepFace**.
  * Exibe a imagem com a emoção dominante.
  * Gera um gráfico com a distribuição de todas as emoções detectadas.

---

## 🖼️ Exemplo de Uso

```text
Imagem: pessoa1.jpg | Emoção dominante: Happy
Imagem: pessoa2.jpg | Emoção dominante: Neutral
```

![Exemplo de saída](docs/exemplo.png)

---

## 📌 Requisitos

* Python >= 3.10
* GPU CUDA (opcional, mas recomendado para melhor desempenho)
* Pacotes: `ultralytics`, `opencv-python`, `deepface`, `matplotlib`, `tf-keras`

---

## 📜 Licença

MIT License © 2025 Alexsandro Lechner

```

---

## ✅ O que inclui:
- Descrição clara do projeto
- Tecnologias usadas
- Passo a passo para rodar
- Estrutura de pastas
- Licença

---
