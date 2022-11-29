# markdown_to_csv : 마크다운을 CSV 파일로 변환

def markdown_to_csv():
    import pandas as pd

    md_file_name = input("csv로 변환할 md 파일 경로를 입력해주세요. : ")
    csv_file_name = input("csv 파일 명을 입력해주세요 : ")

    df = pd.read_md(md_file_name)
    with open(csv_file_name, 'w') as csv:
        df.to_csv(buf=csv)

markdown_to_csv()