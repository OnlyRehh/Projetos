
import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"])/2

df ["media"] = media

situacao = 0
df["situacao"] = situacao

df.loc[df["media"] >= 7, "situacao"] = "APROVADO"
df.loc[df["media"] < 7  , "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"
  

df.to_csv("alunos_situacao.csv")


df2 = pd.read_csv("alunos_situacao.csv")

maior_falta = df2["faltas"].max()
print("O maior número de faltas: "+str(maior_falta))

media_geral= df2["media"].median()
print("Media geral das notas: "+str(media_geral))

maior_media = df2["media"].max()
print("Maior media: "+str(maior_media)) 