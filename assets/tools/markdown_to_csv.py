# markdown_to_csv : 마크다운을 CSV 파일로 변환

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

    # with open(md_file_path) as f:
    #     rows = []
    #     for row in f.readlines():
            
    # with open(f'{csv_file_path}/{csv_file_name}.csv', 'w') as csv:
    #     df.to_csv(buf=csv)

markdown_to_csv()