flights_in_US[(flights_in_US.ORIGIN.isin(list_of_new_york_airports)) &
              (flights_in_US.DEST == 'SFO')].groupby(['YEAR']).sum().plot()
flights_in_US[(flights_in_US.ORIGIN.isin(list_of_new_york_airports)) &
              (flights_in_US.DEST == 'LAX')].groupby(['YEAR']).sum().plot()
flights_in_US[(flights_in_US.ORIGIN.isin(list_of_new_york_airports)) &
              (flights_in_US.DEST == 'ORD')].groupby(['YEAR']).sum().plot()