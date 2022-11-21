# %%
from os import listdir
import numpy as np

def find_csv_filenames( path_to_dir, suffix=".CSV" ):
    filenames = listdir(path_to_dir) 
    return [ filename for filename in filenames if filename.endswith( suffix ) ]



fl = find_csv_filenames('C:\\Users\\SAMPRITHI\\Desktop\\sample_downloads')

# %%
import pandas as pd

# %%
websites = []
for fi_name in fl:
    df_1 = pd.read_csv(r'C:\Users\SAMPRITHI\Desktop\sample_downloads\{0}'.format(fi_name), delimiter='\t')

    

# %%
websites = pd.DataFrame(websites,columns = ['websites'])
websites.to_csv('C:\\Users\\SAMPRITHI\\Desktop\\Research\\websites.CSV') 

# %%
df_1 = pd.read_csv(r'C:\Users\SAMPRITHI\Desktop\sample_downloads\20220228.CSV', delimiter='\t')
df_1

# %%
import numpy as np

# %%
def search(sub):

    def find(X):
        try:
            return X.apply(lambda x: sub in x)
        except TypeError:
            return X.apply(lambda x: False)
    return find

# %%
data = {}
for sub in [".rt.com", "sputniknews.com"]:
    data[sub]  = []
    for fi_name in fl:
        df_1 = pd.read_csv(r'C:\Users\SAMPRITHI\Desktop\sample_downloads\{0}'.format(fi_name), delimiter='\t')
        flag_df = df_1.apply(search(sub))
        for col in flag_df.columns:
            if np.any(flag_df[col].values):
                data[sub].extend(list(df_1[col].values[flag_df[col].values]))
        print(f"Done... {fi_name}")

# %%


# %%
for i in df_1.columns:
    i = str(i)
    print(i)
    print(type(i))
    col_list = df_1.i.values.tolist()
    print(col_list)
    res = [j for j in col_list if sub in j]
    print(res)
    #df_1[i].astype('str').apply(lambda x: print(df_1[i].name) if x.startswith(sub) else 'pass')


