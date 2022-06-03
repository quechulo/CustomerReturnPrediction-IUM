if __name__ == '__main__':
    date = datetime.datetime(2022, 2, 15)
    weeks = weeksBefore(date, 4)
    pr = []
    for i in range(0, 30):
        pr.append(None)

    differences = []
    for i in range(30, 36):
        weeks = i
        prediction = predict(weeks, model)
        pr.append(prediction)
        diff = round(abs(data[i] - prediction), 1)
        differences.append(diff)


    print(np.mean(differences))


    plt.plot(data, label="observed")
    plt.plot(pr, label="predicted")
    x = [i for i in range(0, len(data))]
    y = data
    plt.plot(x, y)
    my_xticks = [None for i in range(0, len(data))]
    date = datetime.datetime(2022, 2, 1)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '02-2022'
    date = datetime.datetime(2021, 11, 25)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '11-2021'
    date = datetime.datetime(2020, 6, 15)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '06-2020'
    date = datetime.datetime(2021, 6, 15)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '06-2021'
    date = datetime.datetime(2019, 6, 15)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '06-2019'
    date = datetime.datetime(2020, 11, 25)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '11-2020'
    date = datetime.datetime(2019, 11, 25)
    weeks = weeksBefore(date, 4)
    my_xticks[weeks] = '11-2019'
    print(my_xticks)
    plt.xticks(x, my_xticks)
    plt.xticks(rotation=45)

    plt.xlabel('four weeks')
    plt.ylabel('number of returns')

    plt.legend()
    plt.show()

