import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == "Male"]["age"].mean()

    num_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    total_people = df.shape[0]
    percentage_bachelors = (num_bachelors / total_people) * (100)

        
    education_advance = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    salary_advance = df['salary'] == ' >50K'
    total_higher_ed = education_advance.sum()
    higher_ed_rich = (education_advance & salary_advance).sum()
    higher_education = (higher_ed_rich / total_higher_ed) * 100


    lower_education = 

    higher_education_rich = None
    lower_education_rich = None

    min_work_hours = None

    num_min_workers = None  

    rich_percentage = None

    highest_earning_country = None
    highest_earning_country_percentage = None

    top_IN_occupation = None


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
