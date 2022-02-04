import numpy as np

ar1 = np.arange(10)
print(ar1)

ar2 = np.arange(2, 10)
print(ar2)

ar3 = np.arange(2, 10, 2)
print(ar3)

ar4 = np.arange(2, 10, dtype=np.float32)
print(ar4)

ar5 = np.arange(10, 0, -1)
print(ar5)

#Working with dates:
months_2017 = np.arange('2017-01-01', '2018-01-01', dtype='datetime64[M]')
print(months_2017)
print()

quarters_2017 = np.arange('2017-01-01', '2018-01-01', 3, dtype='datetime64[M]')
print(quarters_2017)
quarter_start_dates = [np.datetime64(date, 'D') for date in quarters_2017]
print(quarter_start_dates)