# apps/testing/utils.py
import os
import joblib
import pandas as pd
from django.conf import settings

def load_model(filename):
    model_path = os.path.join(settings.BASE_DIR, 'apps', 'testing', 'model', filename)
    return joblib.load(model_path)

def clean_dataframe(df, expected_columns):
    df = df.copy()

    # 1. Ambil kolom yang sesuai
    df = df[expected_columns]

    # 2. Ubah semua ke lowercase kolom
    df.columns = [col.lower() for col in df.columns]

    # 3. Pastikan kolom numerik bisa dibaca (coerce to NaN jika tidak valid)
    for col in df.columns:
        # Anggap semua kolom numerik (kalau tahu kolom kategorikal bisa dikecualikan)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Opsional: isi NaN dengan nilai default (median/model siap handle ini)
    df.fillna(0, inplace=True)

    return df