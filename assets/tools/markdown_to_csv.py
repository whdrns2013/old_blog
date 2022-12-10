# markdown_to_csv : 마크다운을 CSV 파일로 변환
# 레퍼런스
## 파일 대화창 모듈 : https://digiconfactory.tistory.com/entry/파이썬-GUI-프로그래밍-5-7-Tkinter-filedialog
## 마크다운 -> CSV : https://blog.finxter.com/python-convert-markdown-table-to-csv/
## 제너레이터 리스트화 : https://whatisthenext.tistory.com/114

def markdown_to_csv():
    import pandas as pd
    from tkinter import filedialog
    import tabulate

    md_file_path = filedialog.askopenfilename(title = 'csv로 변환할 마크다운 파일을 선택해주세요.')
    md_file_name = md_file_path.split('/')[-1].replace('.md', '')
    csv_file_path = filedialog.askdirectory(title = 'csv를 저장할 경로를 선택해주세요.')
    csv_file_name = md_file_name

    if md_file_path.find('.md') == -1:
        print('마크다운 파일이 아닙니다. 다시 확인해주세요.')

    rows = []    
    for row in open(md_file_path, 'r', encoding='utf-8').readlines():
        rows.append(list(x.strip() for x in row.split('|')))
    
    df = pd.DataFrame(i for i in rows)
    df.drop(columns=[0, 1, list(df.columns)[-1]], index=[0, 1], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.columns = [str(x) for x in range(len(list(df.columns)))]
    
    print(df)
    
    df.to_csv(f'{csv_file_path}/{csv_file_name}.csv')

markdown_to_csv()