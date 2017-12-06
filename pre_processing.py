"""
mkdir /tmp/ramdisk
chmod 777 /tmp/ramdisk
sudo mount -t tmpfs -o size=8G tmpfs /tmp/ramdisk/
cp ~/Desktop/data_cleaning/* /tmp/ramdisk/
cd /tmp/ramdisk
"""

import pandas, sys
import pandas as pd
a = pd.read_csv("ddq_answer.csv")
b = pd.read_csv("ddq_training.csv")
comb = b.append(a)
#comb.insert(0,'ID',range(1,1+len(comb))
