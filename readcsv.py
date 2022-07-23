import pandas as pd
dt=pd.read_csv('data.csv' , delimiter=r"\s+",names=["Line","Station","Alt.","Grav.","SD.","Tiltx","Tilty","Temp","Tide","Dur","Rej","Time","Dec.Time+Dat","Terrain","Date"])

print(dt['Line']==2)