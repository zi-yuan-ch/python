if __name__ == '__main__':
    import time
    import datetime

    start = datetime.datetime.strptime('2021-01-15 00:00:00', '%Y-%m-%d 00:00:00')
    print(start + datetime.timedelta(days=100))
