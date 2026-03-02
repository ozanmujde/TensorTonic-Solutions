def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    diff = series[:]
    for _ in range(order):
        diff_tmp = []
        for i in range(1, len(diff)):
            diff_tmp.append(diff[i] - diff[i-1])
        diff = diff_tmp
    return diff
            