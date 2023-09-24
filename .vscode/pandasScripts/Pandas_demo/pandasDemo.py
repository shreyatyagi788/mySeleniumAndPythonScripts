import pandas as pd
df = pd.read_csv("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\.vscode\\pandasScripts\\Pandas_demo\\survey_results_public.csv")
#print(df)
#print(df.shape)
#print(df.info())

#pd.set_option('display.max_columns',61)
#print(df)

schema_df = pd.read_csv(".vscode\\pandasScripts\\Pandas_demo\\survey_results_schema.csv")
#print(schema_df)
# pd.set_option('display.max_rows',61)
# print(schema_df)
#print(schema_df.head(10))
#print(schema_df.tail(15))
#print(df['Hobbyist'].value_counts())
#print(df.columns)

# grabbing rows- we use loc(we always pass labels) and iloc(we pass integers).
#print(df.loc[[0,1],['Hobbyist','Age']]) 
#print(df.loc[0:3,'Hobbyist':'Country'])
#print(df.iloc[0:2,0:4]) #if we use slicing inside loc and iloc, we do not need to specify in [].




# #to make some column as index-method1.
#df = pd.read_csv("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\.vscode\\pandasScripts\\Pandas_demo\\survey_results_public.csv",index_col='Respondent')

#method2

# df.set_index('Respondent',inplace=True)
# print(df)
# df.reset_index(inplace=True)
#print(df)

#to make all columns as index in schemacsv.
schema_df = pd.read_csv(".vscode\\pandasScripts\\Pandas_demo\\survey_results_schema.csv",index_col='Column')
#print(schema_df)
print(schema_df.loc["Age"])

#filtering
high_sal = df['ConvertedComp']>70000
print(df[high_sal])
#print(df.loc[high_sal])







