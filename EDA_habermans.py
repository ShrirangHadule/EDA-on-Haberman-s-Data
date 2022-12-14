# -*- coding: utf-8 -*-
"""

##Habermans Dataset information#

Haberman's survival dataset contains cases from a study that was conducted between 1958 and 1970 at the University of Chicago's Billings Hospital on the survival of patients who had undergone surgery for breast cancer.

Attribute Information:

* Age of patient at the time of operation (numerical);
* Patient's year of operation (year - 1900, numerical) ;
* Number of positive axillary nodes detected (numerical) ;
* Survival status (class attribute) 1 = the patient survived 5 years or longer 2 = the patient died within 5 years

### Objective ### 
Whether patient survived 5 years or longer OR patient died within 5 years who had undergone surgery for breast cancer.
"""

#importing bunch of libbraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading data haberman.csv dataset in pandas dataframe
haberman = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/haberman.csv") #Using google colab
haberman

print("Data points and features:")
print(haberman.shape)

print("\ncolumn names in our dataset:")
print(haberman.columns)

print("\nDatapoints for each class label i.e status:")
print(haberman["status"].value_counts())

"""###Conclusion###
 * Habermans data is imbalanced dataset with 306 rows and 4 columns
 * The patients who survived > 5 years are (73%) 
 * patients who died within 5 years (27%)
"""

#2D scatter plot 
#Bivariate analysis
haberman.plot(kind = 'scatter',y='nodes', x='age')
plt.show()

#Does not make any sense

#lets try by coloring points belonging to class label i.e status
sns.set_style('whitegrid')
g = sns.FacetGrid(haberman, hue='status', height=6)
g.map(sns.scatterplot,'age','nodes').add_legend()
plt.title('nodes vs age', size=15)
plt.show()

"""###Conclusion###

* There is high chance of patients survival more than 5 years if nodes are less than 20 and age <= 40, with 3 misclassified patients.
* In between age 50 to 60, patients who had nodes ==0 are survived > 5 years

## scatter plot ##
"""

#pairwise scatter plor: pair plot
#we have 3 datapoints in 2D, so 3c2= 3 pair plots

sns.set_style('whitegrid')
sns.pairplot(haberman, hue='status', kind='scatter',height=4)
plt.show()

"""###Conclusion###
* nodes and age are the comparitively useful feature
* But we cannot seperate the status by drawing lines i.e by using if else condition, as they are overlapping

##Univariate analysis##
"""

haberman_1=haberman.loc[haberman['status']==1]
haberman_2=haberman.loc[haberman['status']==2]

#Plotting histogram for nodes
h=sns.FacetGrid(haberman, hue="status", height=8) 
h.map(sns.histplot, "nodes") .add_legend();
plt.show()

"""###conclusion###
* Most of the patients who survived > 5 years have nodes < 5 also majority of the patients who survived < 5 years, are also belongs to the nodes < 5

"""

#Plotting histogram for age
sns.FacetGrid(haberman, hue="status", height=4) \
   .map(sns.histplot, "age") \
   .add_legend();
plt.show()

"""###Conclusion###
* patients who survived > 5 years belong to age group of 30 to 76
* patients who survived < 5 years belong to age group of 35 to 83
* Patients whose age < 33 years survived > 5 years irrespective of nodes.
* Patients whose age > 76 years are not survived > 5 years irrespective of nodes.
"""

#Plotting histogram for year
sns.FacetGrid(haberman, hue="status", height=6) \
   .map(sns.distplot, "year") \
   .add_legend();
plt.show()

"""###Conclusion###
* In year 60 to 62 highest patients survived > 5 years 
* In year 64 to 66 lowest patients survived > 5 years
"""

#PDF does not provide any information about probability
#Let's Draw CDF

counts, bin_edges = np.histogram(haberman_1['nodes'], bins=10, 
                                 density = True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf, label='PDF Survival more than 5 years')
plt.plot(bin_edges[1:],cdf, label='CDF Survival more than 5 years')


counts, bin_edges = np.histogram(haberman_2['nodes'], bins=10, 
                                 density = True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf,label='PDF Survival less than 5 years')
plt.plot(bin_edges[1:],cdf,label='CDF Survival less than 5 years')


plt.title("CDF of nodes")
plt.xlabel('nodes')
plt.ylabel('probability')

plt.legend()

plt.show()

"""###Conclusion###
* 85% patients who survived have nodes less than 5
* as axillary nodes increases survival rate decreases
"""

#mean
print('mean of number of nodes of people who survived > 5:')
print(np.mean(haberman_1['nodes']))

print('\nmean of number of ages of people who survived > 5:')
print(np.mean(haberman_1['age']))

print('\nmean of number of ages of people who survived < 5:')
print(np.mean(haberman_2['age']))

print('\nmean of number of nodes of people who survived < 5:')
print(np.mean(haberman_2['nodes']))

#median
print('median of number of nodes of people who survived > 5:')
print(np.median(haberman_1['nodes']))

print('\nmedian of number of ages of people who survived > 5:')
print(np.median(haberman_1['age']))

print('\nmedian of number of ages of people who survived < 5:')
print(np.median(haberman_2['age']))

print('\nmedian of number of nodes of people who survived < 5:')
print(np.median(haberman_2['nodes']))

#standard devitation 
print('std.dev of number of nodes of people who survived > 5:')
print(np.std(haberman_1['nodes']))

print('\nstd.dev of number of ages of people who survived > 5:')
print(np.std(haberman_1['age']))

print('\nstd.dev of number of ages of people who survived < 5:')
print(np.std(haberman_2['age']))

print('\nstd.dev of number of nodes of people who survived < 5:')
print(np.std(haberman_2['nodes']))

#percentile and quantiles
print('quantiles')
q = np.percentile(haberman_1['nodes'],np.arange(0,100,25))
print(q)

print('\n90 percentile')
r = np.percentile(haberman_1['nodes'],90)
print(r)

#Median absolute devitation
from statsmodels import robust
print ("\nMedian Absolute Deviation")
print(robust.mad(haberman_1["nodes"]))
print(robust.mad(haberman_2["nodes"]))

#Box plot with whiskers
sns.boxplot(x='status', y='nodes', data=haberman)
plt.show()

#violin plot
sns.violinplot(x='status', y='nodes', data= haberman, height= 5)
plt.show()

"""##Conclusion##
* For survival status 1, axillary nodes are denser in region of 0 to 3
* It is impossibel set threshold as majority of points are overlapping

##Conclusion summary##
* Habermans data is imbalanced dataset with 306 rows and 4 columns
* The patients who survived > 5 years are (73%)
* patients who died within 5 years (27%)

###From 2d scatter plot###
* There is high chance of patients survival more than 5 years if nodes are less than 20 and age <= 40, with 3 misclassified patients.
* In between age 50 to 60, patients who had nodes ==0 are survived > 5 years

###From pair plot###
* nodes and age are the comparitively useful feature 
* But we cannot seperate the status by drawing lines i.e by using if else condition, as they are overlapping

###From PDF###
* of Nodes
* Most of the patients who survived > 5 years have nodes < 5 also majority of the patients who survived < 5 years, are also belongs to the nodes < 5

* of age
* patients who survived > 5 years belong to age group of 30 to 76
* patients who survived < 5 years belong to age group of 35 to 83
* Patients whose age < 33 years survived > 5 years irrespective of nodes.
* Patients whose age > 76 years are not survived > 5 years irrespective of nodes.

* year of operation
* In year 60 to 62 highest patients survived > 5 years 
* In year 64 to 66 lowest patients survived > 5 years
"""
