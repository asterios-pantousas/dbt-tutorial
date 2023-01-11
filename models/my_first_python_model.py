def model (dbt,session):
    

    sql_model_df = dbt.source("asterios_playground","orders")
    
    return sql_model_df

