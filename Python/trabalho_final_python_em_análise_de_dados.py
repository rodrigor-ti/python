# -*- coding: utf-8 -*-
"""Trabalho Final - Python em Análise de Dados

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xFRVBv1Xc4sRNAsNfNraJJIPkjgU7xM1

Grupo 06: Rodrigo Rodrigues, Samyr, Nilo Marques, Juracy Barbosa e Nyashi Nunes

 Colab: https://colab.research.google.com/drive/1xFRVBv1Xc4sRNAsNfNraJJIPkjgU7xM1?usp=sharing

💻💻Trabalho final Python em Análise de Dados💻💻

Passo 1 - Importar os dados Dataset

Dataset about distinguishing genuine and forged banknotes. Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. A Wavelet Transform tool was used to extract features from these images.

Tradução:

Conjunto de dados sobre a distinção entre notas genuínas e falsificadas. Os dados foram extraídos de imagens obtidas de espécimes semelhantes a notas genuínas e falsificadas. Para a digitalização foi utilizada uma câmera industrial normalmente utilizada para inspeção de impressão. As imagens finais têm 400x 400 pixels. Devido à lente do objeto e à distância do objeto investigado, foram obtidas imagens em escala de cinza com resolução de cerca de 660 dpi. Uma ferramenta Wavelet Transform foi usada para extrair características dessas imagens.

Attribute Information

V1. variance of Wavelet Transformed image (continuous)

V2. skewness of Wavelet Transformed image (continuous)

V3. curtosis of Wavelet Transformed image (continuous)

V4. entropy of image (continuous)

Class (target). 0 for genuine and 1 for forged

Fonte: https://datahub.io/machine-learning/banknote-authentication

Importando o arquivo do Drive
"""

import pandas as pd
notas_data_frame = pd.read_csv("https://drive.google.com/uc?id=1QIpzPDW6gQxrFqA917MTq3gEpuDgmsPW")
notas_data_frame.head(20)

"""Features e Rótulos"""

X = notas_data_frame[["Variance", " Skewness", " Curtosis", " Entropy"]]
y = notas_data_frame[" Class"]

"""Separação/Treino"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Treinamento da máquina"""

from sklearn.ensemble import RandomForestClassifier

random_forest_clf = RandomForestClassifier()
random_forest_clf.fit(X_train, y_train)

y_pred = random_forest_clf.predict(X_test)

print(y_pred)

"""Matriz de confusão"""

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()

print(tp, fp, tn, fn)
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))