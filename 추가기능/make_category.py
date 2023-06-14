import csv
import pandas as pd



def make_category(keyword, category):
    file = open('megaGymDataset.csv', encoding='utf-8-sig')
    csvreader = csv.reader(file)
    header = next(csvreader)

    #Extract Rows
    rows = []
    for row in csvreader:
        rows.append(row)
    result={}
    userName = []
    for i in range(0,len(rows)):
        if keyword in rows[i][5]:
            userName.append(rows[i])

    if category=='Type':
        for i in range(len(userName)):
            cat = userName[i][3]
            if cat not in result:
                result[cat] = []
            result[cat].append(userName[i][1])
    elif category=='BodyPart':
        for i in range(len(userName)):
            cat = userName[i][4]
            if cat not in result:
                result[cat] = []
            result[cat].append(userName[i][1])
    elif category=='Level':
        for i in range(len(userName)):
            cat = userName[i][6]
            if cat not in result:
                result[cat] = []
            result[cat].append(userName[i][1])
    else:
        print("잘못")


    max_length = max([len(values) for values in result.values()])
    for key in result.keys():
        result[key] += [''] * (max_length - len(result[key]))

    df = pd.DataFrame(result)

    # CSV 파일로 저장
    df.to_csv("Gym.csv", encoding="utf-8", index=True)
keyword = input("운동 기구을 입력하세요 : ex)Bands")
category = input("분류 기준을 선택하세요(Type,BodyPart,Level): ")
make_category(keyword,category)
