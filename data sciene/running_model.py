import pandas as pd
import numpy as np
import json
import joblib 
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketing_president_project.settings')
    import django
    django.setup()
    from django.conf import settings
except Exception as e:
    print(f"Failed to set up Django environment: {e}")
    print("Please ensure you are running this script from the root of your Django project,")
    print("or adjust the sys.path.append and DJANGO_SETTINGS_MODULE accordingly.")
    sys.exit(1)

MODEL_FILES_DIR = os.path.join(settings.BASE_DIR, 'apps', 'funnel', 'model_files')
os.makedirs(MODEL_FILES_DIR, exist_ok=True)

print(f"Saving models and preprocessor to: {MODEL_FILES_DIR}")

db_url = "postgresql://marketing:12345678@localhost:5432/marketing_systems"
engine = create_engine(db_url)

print("Loading data from database...")
df_2022 = pd.read_sql("SELECT * FROM eda_2022_2023", engine)
df_2023 = pd.read_sql("SELECT * FROM eda_2023_2024", engine)
df = pd.concat([df_2022, df_2023], ignore_index=True)
print(f"Data loaded. Total rows: {len(df)}")

df["assumed_enrolled"] = ((df["ispaid"] == 1) & (df["paymentamount"] >= 2500000)).astype(int)
used_columns = ['groupreg', 'regtype', 'iddataregkhusustype', 'isregtypechanged', 'oldregtype', 'regtypechangeby',
    'is_onlinetest', 'is_onlinetest_taken', 'qty_onlinetest_taken', 'is_tryout', 'asalsekolah',
    'idschooltypedata', 'idschooljurusandata', 'graduationyear', 'highschoolcountry', 'dob',
    'age_on_register', 'idmajordata', 'idconcentrationdata', 'idmajordata2_dualdegree',
    'iddataclasstype', 'ismajorchanged', 'oldmajor', 'majorchangeby', 'ideventdata', 'nationality',
    'idcountrydata', 'iddataprovinces', 'iddataregencies', 'kelurahan', 'kecamatan', 'intl_country',
    'isaddresscheck', 'isaddresscheckedby', 'postcode', 'iddatawhyuniv', 'iddatawhymajor',
    'iddatainfouniv', 'puatscore', 'puetscore', 'finalscore', 'rank', 'isrankchanged', 'oldrank',
    'rankchangeby', 'is_raporautorank', 'is_prestasiautorank', 'is_utbkautorank', 'is_unbkautorank',
    'iddatatipelulusanprofexe', 'iddatapassingstatus', 'isrankconfirm', 'isrankedby', 'agent',
    'referralwithdrawseq', 'iddatawithdrawstatus', 'duplicatesametrack', 'duplicatedifftrack',
    'isloapublish', 'isloapublish_onlinetest', 'isloaextensionpublish', 'is_autoloaextensionpublish',
    'is_autoloapublish', 'is_autoloapublish_viawa', 'isloarepublish', 'islatpublish',
    'is_autolatpublish_viawa', 'islat2publish', 'islat3publish', 'islat4publish', 'islcdnpublish',
    'iddatamedfinalrank', 'ispaid', 'paymentamount', 'isenrolled', 'gender', 'iddatareligion',
    'pushprovince', 'pushregencies', 'ispushupdated', 'ismypushupdated', 'umur', 'age_imputed',
    'total_cicilan', 'assumed_enrolled']

missing_cols = [col for col in used_columns if col not in df.columns]
if missing_cols:
    print(f"Warning: Missing columns from DB: {missing_cols}. These columns will be created as NaN.")
    for col in missing_cols:
        df[col] = np.nan 

df = df[used_columns].copy() 
df['label_pendaftar'] = 1
df['label_bayar'] = (df['ispaid'] == 1).astype(int)
df['label_enroll'] = df['assumed_enrolled']

X = df.drop(columns=['label_pendaftar', 'label_bayar', 'label_enroll'])

if 'dob' in X.columns:
    print("Dropping 'dob' column from features as it's not supported by sparse matrices.")
    X = X.drop(columns=['dob'])

y_pendaftar = df['label_pendaftar']
y_bayar = df['label_bayar']
y_enroll = df['label_enroll']

X = X.loc[:, ~X.columns.duplicated()]

categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

categorical_cols.extend([col for col in ['nationality', 'iddataprovinces', 'iddataregencies'] if col in X.columns and col not in categorical_cols])
numerical_cols = [col for col in numerical_cols if col not in ['iddataprovinces', 'iddataregencies', 'nationality']]

all_processed_cols = set(numerical_cols + categorical_cols)
missing_from_processing = set(X.columns) - all_processed_cols
if missing_from_processing:
    print(f"Warning: Columns not included in preprocessor: {missing_from_processing}")

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))
])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=True))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ],
    remainder='passthrough' 
)

print("Fitting preprocessor...")
preprocessor.fit(X) 
print("Preprocessor fitted successfully.")

preprocessor_path = os.path.join(MODEL_FILES_DIR, 'preprocessor.pkl')
joblib.dump(preprocessor, preprocessor_path)
print(f"Preprocessor saved to {preprocessor_path}")

print("Transforming X data for model training...")
X_processed = preprocessor.transform(X)
print("X data transformed.")

def train_model(X_data_processed, y_data):
    model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42, n_jobs=-1)
    print(f"Training model for {y_data.name}...")
    model.fit(X_data_processed, y_data)
    print(f"Training for {y_data.name} completed.")
    return model

model_pendaftar = train_model(X_processed, y_pendaftar)
model_bayar = train_model(X_processed, y_bayar)
model_enroll = train_model(X_processed, y_enroll)

joblib.dump(model_pendaftar, os.path.join(MODEL_FILES_DIR, "model_pendaftar.pkl"))
joblib.dump(model_bayar, os.path.join(MODEL_FILES_DIR, "model_bayar.pkl"))
joblib.dump(model_enroll, os.path.join(MODEL_FILES_DIR, "model_enroll.pkl"))
print("Models saved successfully.")

columns_used_path = os.path.join(MODEL_FILES_DIR, "columns_used.json")
with open(columns_used_path, "w") as f:
    json.dump(list(X.columns), f) # X sudah tidak mengandung 'dob' di sini
print(f"columns_used.json saved to {columns_used_path}")

print("Generating predictions for insight files...")

df['pred_pendaftar'] = model_pendaftar.predict(X_processed)
df['pred_bayar'] = model_bayar.predict(X_processed)
df['pred_enroll'] = model_enroll.predict(X_processed)

df['iddataprovinces'] = df['iddataprovinces'].astype(str)
df['iddataregencies'] = df['iddataregencies'].astype(str)
df['nationality'] = df['nationality'].astype(str)
df['asalsekolah'] = df['asalsekolah'].astype(str)


result_province_df = df.groupby('iddataprovinces').agg(
    total_pendaftar=('label_pendaftar', 'sum'),
    total_pembayar=('label_bayar', 'sum'),
    total_enroll=('label_enroll', 'sum'),
    pred_pendaftar=('pred_pendaftar', 'sum'),
    pred_bayar=('pred_bayar', 'sum'),
    pred_enroll=('pred_enroll', 'sum')
).round(0)
result_province_dict = result_province_df.to_dict(orient='index')
province_insight_path = os.path.join(MODEL_FILES_DIR, 'insight_province_agg.json')
with open(province_insight_path, "w") as f:
    json.dump(result_province_dict, f)
print(f"insight_province_agg.json saved to {province_insight_path}")


result_regency_df = df.groupby('iddataregencies').agg(
    total_pendaftar=('label_pendaftar', 'sum'),
    total_pembayar=('label_bayar', 'sum'),
    total_enroll=('label_enroll', 'sum'),
    pred_pendaftar=('pred_pendaftar', 'sum'),
    pred_bayar=('pred_bayar', 'sum'),
    pred_enroll=('pred_enroll', 'sum')
).round(0)
result_regency_dict = result_regency_df.to_dict(orient='index')
regency_insight_path = os.path.join(MODEL_FILES_DIR, 'insight_regency_agg.json')
with open(regency_insight_path, "w") as f:
    json.dump(result_regency_dict, f)
print(f"insight_regency_agg.json saved to {regency_insight_path}")

result_country_df = df.groupby('nationality').agg(
    total_pendaftar=('label_pendaftar', 'sum'),
    total_pembayar=('label_bayar', 'sum'),
    total_enroll=('label_enroll', 'sum'),
    pred_pendaftar=('pred_pendaftar', 'sum'),
    pred_bayar=('pred_bayar', 'sum'),
    pred_enroll=('pred_enroll', 'sum')
).round(0)
result_country_dict = result_country_df.to_dict(orient='index')
country_insight_path = os.path.join(MODEL_FILES_DIR, 'insight_country_agg.json')
with open(country_insight_path, "w") as f:
    json.dump(result_country_dict, f)
print(f"insight_country_agg.json saved to {country_insight_path}")


print("\nAll models, preprocessor, and insight files have been recreated and saved to the correct directory.")
print("You can now run your Django server: python manage.py runserver")