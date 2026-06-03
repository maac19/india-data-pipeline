import pandas as pd
print("Starting ingestion...")

#------------------
#Population Dataset
#------------------
population_df = pd.read_csv(
      "/data/raw_files/population_data_2011.csv"
)
print("\nPopulation Dataset Preview:")
print(population_df.head())

print("\nPopulation Dataset Shape:")
print(population_df.shape)

print("\nPopulation Columns:")
print(population_df.columns.tolist())

#-----------------
#Litereacy Dataset
#-----------------

literacy_df = pd.read_excel(
    "/data/raw_files/literacy_data.xlsx"
)
print("\nLiteracy Dataset Preview:")
print(literacy_df.head())

print("\nLiteracy Dateset Shape:")
print(literacy_df.shape)

print("\nLiteracy Columns:")
print(literacy_df.columns.tolist())

#------------------
#Employment Dataset
#------------------

emp_df = pd.read_csv(
    "/data/raw_files/employment_data.csv"
)
print("\nEmployment Dataset Preview:")
print(emp_df.head())

print("\nEmployment Dataset Shape:")
print(emp_df.shape)

print("\nEmployment Coulmns:")
print(emp_df.columns.tolist())

print("\nIngestion completed successfully")

#-----------------------------------
# Data Cleaning (Clean Column Names)
#-----------------------------------

population_df.columns = population_df.columns.str.strip()
literacy_df.columns = literacy_df.columns.str.strip()
emp_df.columns = emp_df.columns.str.strip()

print("\nCleaned Employment Columns:")
print(emp_df.columns.tolist())

#---------------------------------------------------
# Data Cleaning Transformation (Removing Empty Rows)
#---------------------------------------------------

emp_df = emp_df.dropna(how='all')

print("\nEmployment Dataset After Cleaning:")
print(emp_df.shape)

#-------------------------------------------
# Data Quality Validation (Null Value Analysis)
#-------------------------------------------

print("\nPopulation Null Values:")
print(population_df.isnull().sum())

print("\nLiteracy Null Values:")
print(literacy_df.isnull().sum())

print("\nEMployment Null Values:")
print(emp_df.isnull().sum())

#--------------------------------------------------
# Saving Cleaned Data (Create Processed Data Layer)
#--------------------------------------------------

population_df.to_csv(
    "/data/processed/clean_population_data.csv",
    index=False
)

literacy_df.to_csv(
    "/data/processed/clean_literacy_data.csv",
    index=False
)

emp_df.to_csv(
    "/data/processed/clean_employment_data.csv",
    index=False
)

selected_population_columns = [
    'District code',
    'State name',
    'District name',
    'Population',
    'Male',
    'Female',
    'Literate',
    'Male_Literate',
    'Female_Literate',
    'SC',
    'Male_SC',
    'Female_SC',
    'ST',
    'Male_ST',
    'Female_ST'
]
population_small_df = population_df[selected_population_columns]

population_small_df.to_csv(
    '/data/processed/clean_population_small.csv',
    index=False
)

print("\nSmall Population Dataset Created")
print(population_small_df.head())


selected_literacy_columns = [
    'State',
    'District',
    'Level',
    'TRU',
    'No_HH',
    'TOT_P',
    'TOT_M',
    'TOT_F',
    'P_LIT',
    'M_LIT',
    'F_LIT',
    'P_ILL',
    'M_ILL',
    'F_ILL',
    'TOT_WORK_P',
    'TOT_WORK_M',
    'TOT_WORK_F',
    'NON_WORK_P',
    'NON_WORK_M',
    'NON_WORK_F'
]
literacy_small_df = literacy_df[selected_literacy_columns]
literacy_small_df.to_csv(
        '/data/processed/clean_literacy_small.csv',
        index=False
)

print("\nSmall Literacy Dataset Created")
print(literacy_small_df.head())


print("\nCleaned dataset saved sucessfully") 

