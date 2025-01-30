# análise de dados com python e pandas

# importando a biblioteca pandas
import pandas as pd
import folium
from folium.plugins import HeatMap


df = pd.read_csv(r"C:\Users\arauj\Desktop\Python\Projetos\atividades Python\california_housing_train.csv")

# renomeando as colunas

df = df.rename(columns={"housing_median_age":"idade_mediana_casas", "total_rooms":"total_quartos", "population":"populacao", "households":"total_domicilios_area", "median_income":"renda_mediana_familias", "median_house_value":"valor_mediano_casa"})

print(df.head())

# verificando a quantidade de linhas e colunas
print("verificando a quantidade de linhas e colunas")
print(df.shape)

# retornando as 5 últimas linhas
print("mostrando as últimas 5 linhas")
print(df.tail())

# retornando informações com o describre

print("retornando informações com o describre")
print(df.describe())

# 1. **Análise de Correlação**:
# - Verifique a correlação entre diferentes variáveis, como `renda_mediana_familias` e
# `valor_mediano_casa`, para entender como a renda afeta o valor das casas.

correlacao = df['renda_mediana_familias'].corr(df['valor_mediano_casa'])

print("verificando a correlação entre a renda das famílias e o valor das casas")

if correlacao == -1 or correlacao == 1: 
    print("correlação perfeita")
elif 0.7 <= correlacao <= 0.9 or -0.9 <= correlacao <= -0.7: 
    print("correlação forte") 
elif 0.4 <= correlacao < 0.7 or -0.7 < correlacao <= -0.4: 
    print("correlação moderada") 
elif 0.1 <= correlacao < 0.4 or -0.4 < correlacao <= -0.1: 
    print("correlação fraca") 
else: 
    print("sem correlação")
    
    
#2. **Distribuição Geográfica**:
#- Crie mapas de calor para visualizar a distribuição geográfica de variáveis como 
#`valor_mediano_casa` e `renda_mediana_familias`.

# Criar um mapa base centrado na localização média
mapa = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=6)

# Adicionar o mapa de calor para 'valor_mediano_casa'
heat_data = [[row['latitude'], row['longitude'], row['valor_mediano_casa']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(mapa)

# Salvar o mapa em um arquivo HTML
mapa.save('mapa_valor_mediano_casa.html')



"""
Claro! Aqui estão algumas ideias de análises que você pode fazer com o DataFrame de dados de habitação da Califórnia:





3. **Análise de Densidade Populacional**:
- Calcule a densidade populacional dividindo `populacao` pelo `total_domicilios_area` e
visualize as áreas com maior densidade.

4. **Análise de Idade das Casas**:
- Estude a relação entre a `idade_mediana_casas` e o `valor_mediano_casa` para ver se 
casas mais novas tendem a ter valores mais altos.

5. **Análise de Quartos e Dormitórios**:
- Compare o `total_quartos` e `total_bedrooms` para entender a proporção de quartos de
dormir em relação ao total de quartos.

6. **Análise de Renda e População**:
- Verifique se há uma relação entre `renda_mediana_familias` e `populacao` para 
entender se áreas mais populosas têm rendas mais altas ou mais baixas.

7. **Análise de Outliers**:
- Identifique outliers em variáveis como `valor_mediano_casa` e `renda_mediana_familias`]
para entender quais áreas têm valores atípicos.

8. **Análise Temporal**:
- Se você tiver dados de diferentes anos, pode analisar como as variáveis mudaram ao 
longo do tempo.

9. **Clusterização**:
- Use técnicas de clusterização, como K-means, para agrupar áreas com características 
semelhantes.

10. **Regressão Linear**:
- Construa modelos de regressão linear para prever o `valor_mediano_casa` com 
base em outras variáveis, como `renda_mediana_familias`, `total_quartos`, etc.

"""