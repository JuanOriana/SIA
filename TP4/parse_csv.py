import csv


def getInputsStandard():
    data = []
    countries = []
    sum_area = 0
    sum_GDP = 0
    sum_inflation =0
    sum_life_expec = 0
    sum_militray =0
    sum_pop_growth=0
    sum_unemployment =0
    lines =0
    with open('../europe.csv','r') as file:
        csv_file = csv.DictReader(file)

        for row in csv_file:
            countries.append(row['Country'])
            data.append([row['Country'],float(row['Area']),float(row['GDP']),float(row['Inflation']),float(row['Life.expect']),float(row['Military']),float(row['Pop.growth']),float(row['Unemployment'])])
            sum_area += float(row['Area'])
            sum_GDP += float(row['GDP'])
            sum_inflation += float(row['Inflation'])
            sum_life_expec += float(row['Life.expect'])
            sum_militray += float(row['Military'])
            sum_pop_growth += float(row['Pop.growth'])
            sum_unemployment += float(row['Unemployment'])
            lines+=1
        medium_area = sum_area / lines
        medium_GDP = sum_GDP / lines
        medium_inflation = sum_inflation / lines
        medium_life_expec = sum_life_expec / lines
        medium_militray = sum_militray / lines
        medium_pop_growth = sum_pop_growth / lines
        medium_unemployment = sum_unemployment / lines

        sum_area = 0
        sum_GDP = 0
        sum_inflation = 0
        sum_life_expec = 0
        sum_militray = 0
        sum_pop_growth = 0
        sum_unemployment = 0
        for i in data:
            sum_area += (float(row['Area']) - medium_area) ** 2
            sum_GDP += (float(row['GDP']) - medium_GDP) ** 2
            sum_inflation += (float(row['Inflation']) - medium_inflation)**2
            sum_life_expec += (float(row['Life.expect']) - medium_life_expec)**2
            sum_militray += (float(row['Military']) - medium_militray)**2
            sum_pop_growth += (float(row['Pop.growth']) - medium_pop_growth)**2
            sum_unemployment += (float(row['Unemployment']) - medium_unemployment)**2

        desv_area = sum_area / lines
        desv_GDP = sum_GDP / lines
        desv_inflation = sum_inflation / lines
        desv_life_expec = sum_life_expec / lines
        desv_militray = sum_militray / lines
        desv_pop_growth = sum_pop_growth / lines
        desv_unemployment = sum_unemployment / lines

        for line in range(lines):
            data[line] = [(data[line][1]-medium_area)/desv_area,(data[line][2]-medium_GDP)/desv_GDP,(data[line][3]-medium_inflation)/desv_inflation,(data[line][4]-medium_life_expec)/desv_life_expec,(data[line][5]-medium_militray)/desv_militray,(data[line][6]-medium_pop_growth)/desv_pop_growth,(data[line][7]-medium_unemployment)/desv_unemployment]

    return data, countries


if __name__ == "__main__":
    print(getInputsStandard())
