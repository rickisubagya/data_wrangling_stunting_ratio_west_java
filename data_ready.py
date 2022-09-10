import pandas as pd

from helper.data_check_preparation import read_and_check_data
from helper.feature_engineering import feature_engineering
from helper.constant import PATH1, PATH2, PATH3, PATH4, PATH5, NEW_COLUMN_NAME

def clean_data():
    # read and check data
    df1 = read_and_check_data(PATH1)
    df2 = read_and_check_data(PATH2)
    df3 = read_and_check_data(PATH3)
    df4 = read_and_check_data(PATH4)
    df5 = read_and_check_data(PATH5)
    
    # feature engineering
    print('Start claning data')
    stunting_data_ready = feature_engineering(df1, df2, df3, df4, df5)
    print('Done cleaning data\nStart saving result cleaning data')
    stunting_data_ready.to_excel('artefacts/stunting_data.xlsx', index=False)
    
if __name__=="__main__":
    print('START RUNNING PIPELINE!')
    clean_data()
    print('FINISH RUNNING PIPELINE!')