import pandas as pd
import numpy as np
from statsmodels.tsa.api import VAR
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import python_scripts.data_handling.data_handler as dd
import python_scripts.analysis.fourier as ff
from sklearn.preprocessing import StandardScaler


#file_path = "src/data/daten.csv"
file_path = "src/data/Daten_pandas_2_weeks.csv"
user_data = pd.read_csv(file_path, decimal=',')
columnsdata = dd.get_column_names(user_data)

#start_date = "2021-02-09"
#end_date = "2021-02-15"

# Select the specified columnI
# Convert timestamps to datetime objects

timestamps = pd.to_datetime(user_data['timestamp'])
dataList = []
timestampsData=user_data[columnsdata[14]].values

for i in range(len(columnsdata)-2):
    # Filter data based on the specified date range
    #mask = (timestamps >= start_date) & (timestamps <= end_date)
    
    # Select the column and reset the index
    #column_values = user_data.loc[mask, columns[i]].reset_index(drop=True)
    column_values = user_data[columnsdata[i]].values
    dataList.append(column_values)
    
    # Append the selected column to the list
    #dataList.append(column_values)
# Convert the list of selected columns to a NumPy array
data = np.array(dataList).T  # Transpose to get the desired shape
# Créer un DataFrame avec des noms de colonnes
columns = [f'Signal_{i}' for i in range(1, 14)]
df = pd.DataFrame(data, columns=columns)
# Fraction d'observations à considérer comme anomalies
outliers_fraction = 0.01

# Estimation du modèle VAR
correlation_matrix = df.corr()
df = df.apply(pd.to_numeric, errors='coerce')
model = VAR(df)
results = model.fit(4)

# Récupérer les résidus du modèle VAR
residuals = results.resid

# Vérifier la longueur des résidus
min_length = min(len(residuals), len(df))

# Appliquer Isolation Forest sur les résidus
scaler = StandardScaler()
residuals_scaled = scaler.fit_transform(residuals.iloc[:min_length, :])  # Utilisez seulement les résidus disponibles
isolation_forest = IsolationForest(contamination=outliers_fraction)
outlier_labels = isolation_forest.fit_predict(residuals_scaled)

# Ajouter une colonne 'Anomaly' au DataFrame
df['Anomaly'] = 0
df['Anomaly'].iloc[:min_length] = np.where(outlier_labels == -1, 1, 0)
# Plot des signaux avec points rouges pour les anomalies
plt.figure(figsize=(12, 8))

for i in range(13):
    plt.subplot(13, 1, i+1)
    plt.plot(df.index, df[f'Signal_{i+1}'], label=f'Signal_{i+1}')
    anomalies = df[df['Anomaly'] == 1]
    plt.scatter(anomalies.index, anomalies[f'Signal_{i+1}'], color='red', label='Anomaly', marker='o')
    plt.legend()
    plt.title(f'Signal_{i+1} with Anomalies')

plt.tight_layout()
plt.show()

print("do you want all graphes seperately ? y for yes")
next=input()
if (next=='y'):
    for i in range(13):
        plt.subplot(1, 1, 1)  # Vous pouvez ajuster le nombre de lignes et de colonnes selon vos besoins
        plt.plot(df.index, df[f'Signal_{i+1}'], label=f'Signal_{i+1}')
        anomalies = df[df['Anomaly'] == 1]
        plt.scatter(anomalies.index, anomalies[f'Signal_{i+1}'], color='red', label='Anomaly', marker='o')
        plt.legend()
        plt.title(f'Signal_{i+1} with Anomalies')
        plt.show()

for i in range(len(df.iloc[:,13])):
    if df.iloc[i,13]==1:   
        print(timestampsData[i])
        