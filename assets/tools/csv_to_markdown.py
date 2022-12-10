# CSV_TO_MAKRDOWN : CSV 파일을 마크다운 형식으로 변환

def csv_to_markdown() : 
    import pandas as pd
    from tkinter import filedialog
    import tabulate

    csv_file_path = filedialog.askopenfilename(title = '마크다운으로 변경할 csv 파일을 선택해주세요.')
    csv_file_name = csv_file_path.split('/')[-1].replace('.csv', '')
    md_file_path = filedialog.askdirectory(title = '마크다운을 저장할 경로를 선택해주세요.')
    md_file_name = csv_file_name
    
    if csv_file_path.find('.csv') == -1:
        print('csv 파일이 아닙니다. 다시 확인해주세요.')

    df = pd.read_csv(csv_file_path)
    with open(f'{md_file_path}/{md_file_name}.md', 'w') as md:
        df.to_markdown(buf=md)

csv_to_markdown()