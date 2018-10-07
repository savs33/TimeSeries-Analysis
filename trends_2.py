import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io_data import get_train_test_data,get_ratings,get_data

# Ref : https://anomaly.io/seasonal-trend-decomposition-in-r/

def decompose_ratings(ratings):

    freq = 4

    series = ratings
    series.plot(title='TV_Ratings',legend='ratings')

    trend = series.rolling(window=freq).mean()
    trend.plot()
    
    detrended = series - trend
    detrended.plot()

    seasonality = detrended.values.reshape(freq,-1)
    seasonality = np.nan_to_num(seasonality)
    seasonality = np.mean(seasonality,axis=0).reshape(1,-1)
    seasonality = np.tile(seasonality,freq)
    seasonality = pd.Series(seasonality.flatten())
    seasonality.plot()
    
    noise = series - trend - seasonality
    noise.plot()

    plt.show()

if __name__ == '__main__':

    # train_df,test_df = get_train_test_data()
    # ratings = get_ratings(train_df)
    # decompose_ratings(ratings)
    # ratings = get_ratings(test_df)
    # decompose_ratings(ratings)

    df = get_data()
    ratings = get_ratings(df)
    decompose_ratings(ratings)