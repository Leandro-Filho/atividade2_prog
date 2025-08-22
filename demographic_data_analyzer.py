import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == "Male"]["age"].mean()

    numero_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    total_pessoas = df.shape[0]
    percentage_bachelors = (numero_bachelors / total_pessoas) * (100)

        
    educacao_avancada = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    salario_avancado = df['salary'] == '>50K'
    educacao_avancada_somada = educacao_avancada.sum()
    total_pessoas_ricacas = (educacao_avancada & salario_avancado).sum()
    higher_education = (total_pessoas_ricacas / educacao_avancada_somada) * 100

    sem_educacao = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    total_sem_educacao = sem_educacao.sum()
    total_ricos_sem_educacao= (sem_educacao & salario_avancado).sum()
    lower_education = (total_ricos_sem_educacao/ total_sem_educacao)*100

    higher_education_rich = higher_education
    lower_education_rich = lower_education

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = (df['hours-per-week'] == 1).sum()
    num_rich_min_workers = ((df['hours-per-week'] == 1) & (df['salary'] == '>50K')).sum()
    rich_percentage = (num_rich_min_workers / num_min_workers) * 100


    salarios_paises = df[df['salary'] == '>50K'].groupby('native-country').size()
    highest_earning_country = salarios_paises.idxmax()
    unitad_states = salarios_paises.max()
    total_ricos = salarios_paises.sum()
    highest_earning_country_percentage = (unitad_states / total_ricos) * 100

    india = df[df['native-country'] == 'India']
    filtragem_india = india[['salary','occupation']]
    india_ganham_50K = filtragem_india[filtragem_india['salary'] == '>50K']
    india_occupation_count = india_ganham_50K['occupation'].value_counts()
    top_IN_occupation = india_occupation_count.idxmax()

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
