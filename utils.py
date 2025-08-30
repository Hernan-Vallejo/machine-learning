import pandas as pd
from sklearn.model_selection import train_test_split

def cargar_datos(path: str) -> pd.DataFrame:
    """Carga dataset de casas desde CSV"""
    return pd.read_csv(path)

def dividir_datos(df: pd.DataFrame, target: str):
    """Divide en features y target + train/test"""
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)
