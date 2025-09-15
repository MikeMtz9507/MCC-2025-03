import pandas as pd
import numpy as np
from dask_expr import DataFrame
from streamlit import dataframe, columns

from KNN_Modularizado import CargaInstancia
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale


instancia= CargaInstancia.cargarInstancia("../Archivos/iris/iris.csv")
print(instancia)



X= instancia.iloc[:,:-1]
Y= pd.DataFrame(instancia.iloc[:,-1])
print(X)

Xarray= X.to_numpy()

Xstd= scaler= StandardScaler().fit_transform(Xarray)
Xstd= pd.DataFrame(data=Xstd, columns=[X.columns])

new_instancia= pd.concat([Xstd,Y])
#new_instancia.to_csv("../Archivos/iris/iris_estandarizado.csv",index=None)
new_instancia.to_csv("../Archivos/iris/iris_normalizada.csv",index=None)
print()