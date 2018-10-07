import pandas as pd


def get_data():
    df = pd.read_csv('data/cleaned_ratings.csv')
    return df


def get_train_test_data():
    df = get_data()
    limit = 71
    train_df = df[:limit]
    test_df = df[limit:]
    return train_df, test_df


def get_ratings(df):
    ratings = df['ratings']
    ratings = pd.Series(ratings)
    return ratings


def get_dates(df):
    dates = df['date']
    dates = pd.Series(dates)
    return dates


def get_weeks(df):
    weeks = df['week']
    weeks = pd.Series(weeks)
    return weeks


def get_date_ratings_weeks(df):
    dates = get_dates(df)
    ratings = get_ratings(df)
    weeks = get_weeks(df)
    return dates, ratings, weeks


def get_train_data():
    train_df, __ = get_train_test_data()
    dates, ratings, weeks = get_date_ratings_weeks(train_df)
    return dates, ratings, weeks


def get_test_data():
    __, test_df = get_train_test_data()
    dates, ratings, weeks = get_date_ratings_weeks(test_df)
    return dates, ratings, weeks

if __name__ == '__main__':
    get_train_data()
