
## 1. Chargez le jeu de données
import subprocess
import gdown
import pandas as pd

# 1b) Remplacez l'ID du fichier
file_id = '11OYR8amwgxgFkIc9bbmi8zygrH9b_wUK'
gdown.download(f'https://drive.google.com/uc?id={file_id}', 'STEG_BILLING_HISTORY_ONLINE.csv', quiet=False)

client_0_bills = pd.read_csv('STEG_BILLING_HISTORY_ONLINE.csv')

client_0_bills['counter_number'] = pd.to_numeric(client_0_bills['counter_number'], errors='coerce')

# 1c) Afficher les dix premières lignes
print(client_0_bills.head(10))

## 2. Type de données de la variable 'client_0_bills'
print(type(client_0_bills))

## 3. Informations générales sur le jeu de données
print(client_0_bills.info())

# 3b) Pour connaître le nombre de lignes et de colonnes
rows, columns = client_0_bills.shap
print(f'Nombre de lignes: {rows}, Nombre de colonnes: {columns}')

# 3c) Pour identifier le nombre de caractéristiques catégorielles 
categorical_features = client_0_bills.select_dtypes(include=['object']).columns
print(f'Nombre de caractéristiques catégorielles: {len(categorical_features)}')

# 3d) Pour connaître l'espace mémoire consommé par le jeu de données
memory_usage = client_0_bills.memory_usage(deep=True).sum()
print(f'Espace mémoire consommé: {memory_usage} octets')

# 4. Inspection des valeurs manquantes
missing_values = client_0_bills.isnull().sum()
print(missing_values[missing_values > 0])

## 5. Choix de la Stratégie
# Dans le cas présent, nous avons procédé à la suppression des valeurs manquantes 
# Parce que la proportion de données manquantes est faible ( moins de 10%) pour affecter significativement l'analyse.

# 5a) Vérification des valeurs manquantes
missing_values = client_0_bills.isnull().sum()
print(missing_values)

# 5b) Évaluer la proportion de valeurs manquantes par rapport au total des données
total_missing = missing_values[missing_values > 0]
proportion_missing = total_missing / len(client_0_bills) * 100
print(proportion_missing)

# 5c) Supprimer les lignes avec des valeurs manquantes
client_0_bills_cleaned = client_0_bills.dropna(how='all')
client_0_bills_cleaned = client_0_bills.dropna(subset=['counter_number', 'reading_remarque'])
client_0_bills_cleaned = client_0_bills.dropna(axis=1)
client_0_bills.dropna(inplace=True)
missing_values_afterDropna = (client_0_bills.isnull().sum())

# 5d) Vérification des chaînes vides
print(client_0_bills[client_0_bills['counter_number'] == ''])

# 5e) Reverification des valeurs manquantes
print(missing_values_afterDropna)

## 6. Analyse descriptive
descriptive_stats = client_0_bills.describe()
print(descriptive_stats)

## 7. Sélectionner les enregistrements du client avec id ='train_Client_0'

# 7a) Méthode 1 : Utilisation du filtrage direct
client_records = client_0_bills[client_0_bills['client_id'] == 'train_Client_0']
print(client_records)

# 7b) Méthode 2 : Utilisation de la méthode query
client_records_query = client_0_bills.query("client_id == 'train_Client_0'")
print(client_records_query)

## 8. Transformation de 'counter_type' en variable numérique
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
client_0_bills['counter_type_encoded'] = le.fit_transform(client_0_bills['counter_type'])

# 8b) Afficher les résultats après transformation
print(client_0_bills[['counter_type', 'counter_type_encoded']].head(10))

# 8c) Afficher les classes et leurs valeurs encodées
print("Classes et valeurs encodées :")
for i, class_name in enumerate(le.classes_):
    print(f"{class_name} = {i}")

## 9. Suppression de la fonction « counter_statue »
client_0_bills.drop(columns=['counter_statue'], inplace=True)

print(client_0_bills.head(10))
