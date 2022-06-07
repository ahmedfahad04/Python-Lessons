import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
from bioinfokit.analys import stat
import pandas as pd

A = [12.6, 12, 11.8, 11.9, 13, 12.5, 14]
B = [10, 10.2, 10, 12, 14, 13]
C = [10.1, 13, 13.4, 12.9, 8.9, 10.7, 13.6, 12]

all_score = A + B + C
company_names = (['A']*len(A) + ['B']*len(B) + ['C']*len(C) )

data = pd.DataFrame({'company': company_names, 'score': all_score}) # arrange the data into a Table

# print(data)

data = data.groupby('company').mean() # arrange the data according to mean
print(data)

lm = ols('score ~ company', data=data).fit()
table = sm.stats.anova_lm(lm, typ=2)
# print(table)


# model = smf.ols('score ~ company', data=data)
# fit = model.fit()
# # fit.predict([0.25])
# fit.predict({'company': [0.25]})