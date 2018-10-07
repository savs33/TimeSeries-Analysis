import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io_data import get_train_test_data,get_ratings,get_data

import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose


def decompose_ratings(ratings):
    series = ratings

    for freq in [13,4]:
        result = seasonal_decompose(series, model='additive', freq=freq)
        result.plot()

    plt.show()


if __name__ == '__main__':

    train_df,test_df = get_train_test_data()
    ratings = get_ratings(train_df)
    decompose_ratings(ratings)
    ratings = get_ratings(test_df)
    decompose_ratings(ratings)

    df = get_data()
    ratings = get_ratings(df)
    decompose_ratings(ratings)