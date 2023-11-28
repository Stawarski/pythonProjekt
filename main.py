import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv')

def aboveAge(age):
    return lambda df: df[df['age'] > age]

def belowAge(age):
    return lambda df: df[df['age'] < age]

def equalAge(age):
    return lambda df: df[df['age'] == age]

jobList = data['job'].unique()
educList = data['education'].unique()

def jobSort(job):
    return lambda df: df[df['job'] == job]

def educSort(educ):
    return lambda df: df[df['education'] == educ]

def aboveBalance(balance):
    return lambda df: df[df['balance'] > balance]

def belowBalance(balance):
    return lambda df: df[df['balance'] < balance]

def aboveDuration(duration):
    return lambda df: df[df['duration'] > duration]

def belowDuration(duration):
    return lambda df: df[df['duration'] < duration]


def compose(*functions):
    def combined(df):
        result = df
        for func in functions:
            result = func(result)
        return result
    return combined


exampleFunctions = compose(
    aboveAge(30),
    jobSort('technician'),
    belowDuration(1500)
)

print(exampleFunctions(data))
