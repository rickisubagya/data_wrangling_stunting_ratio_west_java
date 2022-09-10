import numpy as np
import pandas as pd
from helper.constant import NEW_COLUMN_NAME


def feature_engineering(df1, df2, df3, df4,  df5):
    stunting_data = df1.merge(df2, how='inner').merge(df3, how='inner', on='id').merge(df4, how='inner').merge(df5, how='inner')
    
    # Rename some columns' name
    stunting_data = stunting_data.rename(columns=NEW_COLUMN_NAME)
       
    # Convert string to title case
    stunting_data['regency'] = stunting_data['regency'].str.title()

    stunting_data['district'] = stunting_data['district'].str.title()
    
    stunting_data['sub_district'] = stunting_data['sub_district'].str.title()
    
    # Create a column called toddler_measured
    stunting_data['toddler_measured'] = stunting_data.apply(lambda x: x['toddler_green'] + x['toddler_yellow'] + x['toddler_red'], axis=1)

    
    # Reindex columns position
    stunting_data = stunting_data.reindex(columns=['year', 'sub_district', 'district', 'regency', 'toddler_green', 'toddler_yellow', 'toddler_red', 'toddler_measured', 'pregnant_ced', 'pregnant_all'])

    
    # Convert column year to Datetime format
    stunting_data['year'] = pd.to_datetime(stunting_data['year'], format='%Y')
    
    return stunting_data