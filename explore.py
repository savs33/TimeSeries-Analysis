import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_data():
    df = pd.read_csv('data/tv_ratings.csv')
    print(df.head)
    print(df.columns)

    dates = df['date']
    ratings = df['GRP']

    weeks = []
    date_str = []

    for line in dates:
        date, week = line.split(' ')

        date = str(date)
        date_str.append(date)

        week = week[1:-1]
        week = int(week)
        weeks.append(week)

    date_cvt = pd.to_datetime(date_str)

    df = pd.DataFrame()
    df['date'] = date_cvt
    df['week'] = weeks
    df['ratings'] = ratings

    df.to_csv('data/cleaned_ratings.csv', index=False)


def get_data():
    df = pd.read_csv('data/cleaned_ratings.csv')
    return df


def plot_ratings():
    df = get_data()
    ratings = df['ratings']
    ratings.plot()
    plt.show()

def plot_diff_ratings():
    df = get_data()
    ratings = df['ratings']
    ratings = ratings.diff(periods=1)
    ratings.plot()
    plt.show()

def plot_dates():
    df = get_data()
    date = df['date']
    date = pd.to_datetime(date)
    # date.plot(style='o')
    # plt.show()
    print(len(date))

if __name__ == '__main__':
    # clean_data()
    # get_data()
    # get_train_test_data()
    # plot_ratings()
    # plot_dates()
    plot_diff_ratings()
