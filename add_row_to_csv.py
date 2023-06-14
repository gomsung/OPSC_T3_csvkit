import csv

def add_row_to_csv(filename, new_row):
    # 기존 CSV 파일 열기
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # 새로운 행 추가
    rows.append(new_row)

    # 변경된 내용을 새로운 CSV 파일에 저장
    new_filename = f"new_{filename}"
    with open(new_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"새로운 행이 추가된 파일 {new_filename}이 생성되었습니다.")


filename = 'data.csv'  # 기존 CSV 파일 이름
new_row = ['value1', 'value2', 'value3']  # 추가할 행의 데이터
add_row_to_csv(filename, new_row)
