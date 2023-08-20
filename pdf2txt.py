import os
from PyPDF2 import PdfReader

# 定义PDF文件夹路径和TXT文件夹路径
pdf_folder = r'C:\Users\gaochao02\Desktop\婆媳'  # 使用原始字符串
txt_folder = r'C:\Users\gaochao02\Desktop\婆媳'  # 使用原始字符串

# 获取PDF文件夹中所有PDF文件的文件名
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# 遍历PDF文件名列表
for pdf_file in pdf_files:
    # 打开PDF文件
    pdf_path = os.path.join(pdf_folder, pdf_file)
    pdf = PdfReader(pdf_path)

    # 将PDF文本合并为一个字符串
    text = ''
    for page in pdf.pages:
        text += page.extract_text()

    # 创建TXT文件并写入文本内容
    txt_path = os.path.join(txt_folder, pdf_file[:-4] + '.txt')
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)