import pandas as pd

background = pd.read_csv("data/background-clean.csv")
interest = pd.read_csv("data/interest-clean.csv")

combined = pd.merge(background, interest, on = "response_id", how = "inner")
combined = combined.rename(columns={'dom_x': 'dom_tf', 'dom_y': 'dom_interest', 
                                    "do_you_have_any_preference_regarding_working_on_an_industry_project_or_a_research_lab_project":"rsrch_or_ind"})

combined['dom_interest'] = combined['dom_interest'].str.split('; ')

df_exploded = combined.explode('dom_interest')
one_hot = pd.get_dummies(df_exploded['dom_interest'])

df_encoded = combined[['response_id']].join(one_hot).groupby('response_id', as_index=False).max()

print(combined.head())