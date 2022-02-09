# Challenge-Data-Analysis
# Data Analysis of Immoweb Scrapped Data

![image](https://user-images.githubusercontent.com/96992159/152752109-48401fdc-5ab6-415c-9a8c-c36e349871f4.png)

### Prequisites:
- Python 3.10
- Data for Analysis (CSV file): 
  https://raw.githubusercontent.com/adityachugh02/challenge-collecting-data/master/data_clean_2.csv
- Third Party Libraries:
  - Pandas 0.23.4
  - Numpy Version 1.13.1
  - Matpotlib Version 2.0.2
  - Seaborn Version 0.8.1
## Data Cleaning
 
The data scrapped from Immoweb had multiple usleless data which was cleaned using `Pandas` library in order to have clean dataset for better analysis. We figured out all null\empty values in data and replaced it with appropriate values. The replaced data was converted to new csv file `dataset-cleaned.csv`.

## Data Analysis

The cleaned data is analysed using `matplotlib` library. Our target variable for the analysis was `Price`. In our dataset of 13505 rows and 17 columns, how price is making a difference on other variables.

## Data Interpretation

After the analyzing the data, we could interpret different result based on the data which are as follows:

#### Outliners:
![outliners](https://user-images.githubusercontent.com/96992159/153191172-fc943e5f-ff48-446f-8a41-25cd799fe487.PNG)


 Note: The red circled are the extreme values in data due to wrong input data or data is about different property type(i.e whole appartment)

#### Detailed Informations:

-Most expensive area in Belgium is '8300 Knokke-Heis' with avegage price per square metre is 11647.
-Most expensive area in Wallonia is ' 5541 Hasriere-par-dela' with avegage price per square metre is 320. 
-Most expensive area in Flanders is '8300 Knokke-Heist' with avegage price per square metre is 11647.

-Least expensive area in Belgium is '6592 Monceau-Imbrechies' with avegage price per square metre is 173.7.
-Least expensive area in Wallonia is '6592 Monceau-Imbrechies'  with avegage price per square metre is 173.7. 
-Least expensive area in Flanders is '8953 Wijtschate'  with avegage price per square metre is 322.6.



 
