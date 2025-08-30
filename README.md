# Predicción de Precios de Casas  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)  
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellowgreen?logo=pandas&logoColor=white)  
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Status-Completado-brightgreen)  

Proyecto de Machine Learning para predecir el **precio de casas** a partir de variables como superficie, habitaciones, baños, garage y antigüedad.  

---

## Dataset
- **Fuente**: Datos inventados para fines educativos.  
- **Variables**:
  - `superficie` (m²)  
  - `habitaciones`  
  - `banos`  
  - `garage`  
  - `antiguedad` (años)  
  - `precio` (target a predecir)  

---

## Resultados
Ejemplos de salidas del modelo:  

📌 **Matriz de correlación**  
![Correlación](reports/correlacion.png)  

📌 **Importancia de variables**  
![Importancia](reports/importancia_variables.png)  

---

## Tecnologías utilizadas
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## Cómo usar este proyecto
```bash
git clone https://github.com/usuario/house-prices-ml.git
cd house-prices-ml
pip install -r requirements.txt
jupyter notebook notebooks/modelo_prediccion.ipynb
```

---

## Licencia
Este proyecto se distribuye bajo licencia **MIT**.
