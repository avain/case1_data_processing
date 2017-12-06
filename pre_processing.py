"""
mkdir /tmp/ramdisk
chmod 777 /tmp/ramdisk
sudo mount -t tmpfs -o size=8G tmpfs /tmp/ramdisk/
cp ~/Desktop/data_cleaning/* /tmp/ramdisk/
cd /tmp/ramdisk
"""

import pandas, sys
import pandas as pd
import numpy as np
a = pd.read_csv("ddq_answer.csv")
b = pd.read_csv("ddq_training.csv")

#sample a & b 
a = a #[1:100]
b = b #[1:100]

c = b.append(a)
c.index.name="ID"


#shutffe 
c = c.sample(frac=1)
c = c.sample(frac=1).reset_index(drop=True)
c.columns = ['Gender','Age','Code1','Code2','Code1_Count','Code2_Count','Co_occ']
#c.index.name="ID"
#reindex from 1

c.index = np.arange(1, len(c) + 1)
c.index.name="ID"
#filter the answer to answer file
ans=c[(c.Age=="40-49") & (c.Gender =='F')]
ans.sort_index(inplace=True)
ans.to_csv("answer_all.csv",index=True)

"""
df = df.drop('column_name', 1)
where 1 is the axis number (0 for rows and 1 for columns.)

df.drop(df.columns[[0, 1, 3]], axis=1)

"""
ans=ans.drop('Gender',1)
ans=ans.drop('Age',1)
ans=ans.drop('Code1',1)
ans=ans.drop('Code2',1)
ans=ans.drop('Code1_Count',1)
ans=ans.drop('Code2_Count',1)
ans.to_csv("answer_simple_all.csv")
ans.Co_occ=''
ans.to_csv("upload_sample.csv",index=True) #5817292
del ans

#del the answer part in the original file
c.loc[(c.Age=="40-49") & (c.Gender =='F'),'Co_occ']=''
c.to_csv("released_data.csv",index=True) #77722396

#comb.insert(0,'ID',range(1,1+len(comb)))
#comb.to_csv("test.csv",index=True)
