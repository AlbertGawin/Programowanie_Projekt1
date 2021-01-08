import pandas as pd

kolumny = \
    ["N","M","D","H","DBT","RH","HR","WS","WD","ITH",
     "IDH","ISH","TSKY","N_0","N_30","NE_30","E_30","SE_30","S_30","SW_30",
     "W_30","NW_30","N_45","NE_45","E_45","SE_45","S_45","SW_45","W_45","NW_45",
     "N_60","NE_60","E_60","SE_60","S_60","SW_60","W_60","NW_60","N_90","NE_90",
     "E_90","SE_90","S_90","SW_90","W_90","NW_90"]

dane_bialystok = pd.read_fwf("Data/bialystok.txt")
dane_bydgoszcz = pd.read_fwf("Data/bydgoszcz.txt")
dane_chojnie = pd.read_fwf("Data/chojnice.txt")
dane_elblag = pd.read_fwf("Data/elblag.txt")

dane_bialystok.columns = kolumny
dane_bydgoszcz.columns = kolumny
dane_chojnie.columns = kolumny
dane_elblag.columns = kolumny
