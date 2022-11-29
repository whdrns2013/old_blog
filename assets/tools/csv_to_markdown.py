# CSV_TO_MAKRDOWN : CSV 파일을 마크다운 형식으로 변환

def csv_to_markdown() : 
    import pandas as pd

    csv_file_name = input("md로 변환할 csv 파일 경로를 입력해주세요. : ")
    md_file_name = input("mark down 파일 명을 입력해주세요. : ")
    
    df = pd.read_csv(csv_file_name)
    with open(md_file_name, 'w') as md:
        df.to_markdown(buf=md)

csv_to_markdown()