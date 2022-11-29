# CSV_TO_MAKRDOWN : CSV 파일을 마크다운 형식으로 변환

def csv_to_markdown() : 
    import pandas as pd

    csv_file_name = input("md로 변환할 csv 파일 경로를 입력해주세요. : ")
    md_file_name = input("mark down 파일 명을 입력해주세요. : ")
    
    df = pd.read_csv(csv_file_name)
    with open(md_file_name, 'w') as md:
        df.to_markdown(buf=md, tablefmt="grid")


# markdown_to_csv : 마크다운을 CSV 파일로 변환
def markdown_to_csv():
    import pandas as pd

    md_file_name = input("csv로 변환할 md 파일 경로를 입력해주세요. : ")
    csv_file_name = input("csv 파일 명을 입력해주세요 : ")

    df = pd.read_csv(md_file_name)
    with open(csv_file_name, 'w') as csv_name:
        df.to_csv(buf=csv_name, tablefmt="grid")



csv_to_markdown()