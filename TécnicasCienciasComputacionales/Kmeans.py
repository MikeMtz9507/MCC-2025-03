from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('dataset.xlsx')
X = df.select_dtypes(include='number')

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

max_k_posible = max(2, min(10, X_scaled.shape[0] - 1))
ks = list(range(1, max_k_posible + 1))

inertias = []
for k in ks:
    km = KMeans(n_clusters=k, random_state=0, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

# Gráfica del codo
df_elbow = pd.DataFrame({'k': ks, 'inertia': inertias})
fig_elbow = px.line(
    df_elbow, x='k', y='inertia',
    markers=True,
    title='Método del codo (Inercia vs K)',
    labels={'k':'Número de clusters (K)', 'inertia':'Inercia (SSE)'}
)
fig_elbow.update_layout(width=700, height=450, title_x=0.5)
fig_elbow.show()

kmeans = KMeans(n_clusters=6, random_state=42)
kmeans.fit(X_scaled)

df['cluster'] = kmeans.labels_

centroides = scaler.inverse_transform(kmeans.cluster_centers_)
#print("Centroides:")
#print(centroides)

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x=X.columns[0], y=X.columns[1], hue="cluster", palette="tab10", s=60)
plt.title("Clusters con K-Means (K=5)")
#plt.show()

df.to_csv('resultados.csv', index=False)