Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/USER/Documents/NM.PY
                 Sample            G1             G2  ...  1-2  3-4 already
4                     2             2              2  ...  20%  20%     40%
5                     1           17%              1  ...    1    1       1
6                     4           11%            11%  ...  11%  11%     44%
7                     1             1              2  ...  996   9%    189%
8                   45%            9%            50%  ...  17%    1     17%
9      Micro-array (99)  Normal (n=4)  Serous (n=41)  ...    4  AND      10
10                    4            19            46%  ...  10%  79%     24%
11                   10             4             19  ...   2%  10%     79%
12  Endometrioid in=37)            10              1  ...    3    3      10
14                  27%            8%            27%  ...    6    2     75%

[10 rows x 7 columns]
import pandas as pd
... dataset = [
...     "Sample,G1,G2,Stage,1-2,3-4,already",
...     "1,34,,already,1-2,34,already",
...     "G3,,,,,,",
...     "1-2,3-4,,Q-PCR (n=531 Benign in-15):, , , ",
...     "serous-subtype (14),mucinous subtype [1],Serous in 101,Endometrioid in=9),Clear call in 11),Mucinous in=6)",
...     "2,2,2,20%,20%,20%,40%",
...     "1,17%,1,1,1,1,1",
...     "4,11%,11%,11%,11%,11%,44%",
...     "1,1,2,5,996,9%,189%",
...     "45%,9%,50%,1,17%,1,17%",
...     "Micro-array (99),Normal (n=4),Serous (n=41),1,4,AND,10",
...     "4,19,46%,2%,10%,79%,24%",
...     "10,4,19,46%,2%,10%,79%",
...     "Endometrioid in=37),10,1,10,3,3,10",
...     "27%,3%,27%,8%,27%,,",
...     "27%,8%,27%,Clear cell inw,6,2,75%",
...     "25%,Mucinous (n=151,a,67%,1,89%"
... ]
... df = pd.DataFrame([x.split(',') for x in dataset[1:]], columns=dataset[0].split(','))
... df.replace('', pd.NA, inplace=True)
df.replace(' ', pd.NA, inplace=True)
df.dropna(inplace=True)
print(df)
