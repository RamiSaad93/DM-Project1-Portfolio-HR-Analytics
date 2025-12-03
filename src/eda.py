"""
to start with a quick eda, important if to import the following 
"""
import pandas as pd
import numpy as np
from typing import Dict, Any, List
import seaborn as sns
import matplotlib.pyplot as plt

"""
the dataset needs to be loaded as follows
"""
df = pd.read_csv("https://raw.githubusercontent.com/Dee-M123/DM-Project-Portfolio/refs/heads/main/Project1/HR%20Analytics/Data/Uncleaned_employees_final_dataset%20(1).csv")

"""
a quick review of the dataset can be conducted as follows to make 
sure everthing is as expected and everything was uploaded correctly 
without any errors
"""
# df.head(10) #view first 10 rows

# df.tail(5) #view of last 5 rows

# df.shape #shape of the data

# df.columns #list of all coulmns 

# df.dtypes #get data types of all columns 

# df.info() # an overall summery of the above steps, also lets you know the count of non_null values and memory usage

# df.isnull().sum().sort_values(ascending= False) #have a summary of misisng values 
# df.isnull().mean().sort_values(ascending= False) * 100 #missing values as % breakdown
# df.nunique().sort_values(ascending=False) #count of unique values 
# df.duplicated() #look for duplicated rolls as they my inflate aspects like mean

"""
once a general check of loaded data is done
moving over to look into simple eda as next 
step.

the easiest is to create a class that will generate
summaries of you different datas types.

creating a class with three four:
- the first being one that summarises numeric data
- the second provides a general distribution of numeric data
- the third is a distribution of categorical data per column
- the fourth is distribution of numeric data of all categorical columns
"""

class HREDA:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.numeric_col = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    def numeric_summary(self) -> pd.DataFrame:
        return self.df[self.numeric_col].describe().T


    def numeric_distribution_stats(self, col: str) -> Dict[str, float]:
        numeric_data = self.df[col].dropna()
        return {"mode": numeric_data.mode()[0] if not numeric_data.mode().empty else None,
                "min": numeric_data.min(),
                "max": numeric_data.max(),
                "q25 (lower)": numeric_data.quantile(0.25),
                "q50 (median)": numeric_data.quantile(0.50),
                "q75 (upper)": numeric_data.quantile(0.75),
                "q90 (top 10%)": numeric_data.quantile(0.90),
                "q99": numeric_data.quantile(0.99)}

    """
    categorical summary for one column
    """
    def summarise_cat(self, col: str) -> pd.DataFrame:
        counts = self.df[col].value_counts()
        perc = self.df[col].value_counts(normalize=True) * 100
        return pd.DataFrame({"count": counts, "percentage": perc})

    """
    categorical summary of all columns returned as dictionary
    """
    def cat_summary(self) -> dict:
        return {col: self.summarise_cat(col) for col in self.categorical_cols}

"""
implimating the created class to have data
summarised is the next step in the process

to make use of the class, the following steps have to be take:
"""

# eda = HREDA(df) # drawing from the class methods 

# eda.numeric_summary() # Numericsummary

# # Distribution stats for a single numeric column
# eda.numeric_distribution_stats("avg_training_score")

# #summary of numeric columns can be called upon using:
# per_column_stats = {col: eda.numeric_distribution_stats(col) for col in eda.numeric_col}
# per_column_stats

# # Categorical summary for one column
# eda.summarise_cat("department")

# # Summarise all categorical columns at once via:
# object_summary = eda.cat_summary()
# object_summary

# #or

# object_summary["department"] # access summary for 'department'


# """
# there is a need to have a general overview of how the categorical data relates to numerical.

# To have this done in a quick and easy manner, a pivot table can be used to create summarise table:

# """

# df_filter = df[df["department"] == "Sales & Marketing"] #was visually practical to view per department as opposed to everything at once
# pivot = df_filter.pivot_table(
#     values=["no_of_trainings","age","previous_year_rating","length_of_service",
#         "KPIs_met_more_than_80","awards_won","avg_training_score"],index=["department", "education", "recruitment_channel","gender"],
# aggfunc="mean")

# pivot

# """
# to have a visual representation of the number of employees per department 
# the following graph helps paint a visual representation of that
# """

# sns.countplot(x="department", data=df)
# plt.xticks(rotation=45)
# plt.title("Number of Employees per Department")
# plt.show()

# Percentage distribution
dept_counts = df["department"].value_counts(normalize=True) * 100
dept_counts.plot(kind="bar")
plt.ylabel("Percentage")
plt.title("Department Distribution (%)")
plt.show()



"""
taking average training score as an example, a simple
view on distribution of numerical data can be made
"""

sns.histplot(df["avg_training_score"], bins=20, kde=True)
plt.title("Distribution of Average Training Score")
plt.xlabel("Avg Training Score")
plt.show()




"""
in identifying outliers, 

the following boxplot can help us identify those
"""
sns.boxplot(x="department", y="avg_training_score", data=df)
plt.xticks(rotation=45)
plt.title("Training Score by Department")
plt.show()



"""
a correlation headmap helps have a summarised visual representation 
of numerical columns.

this helps build general insights as to what information of direction is most 
logical to view to drive exploratory questions.

"""

numeric_cols = ["no_of_trainings",
        "age",
        "previous_year_rating",
        "length_of_service",
        "KPIs_met_more_than_80",
        "awards_won",
        "avg_training_score"]
corr = df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Numeric Variables")
plt.show()
