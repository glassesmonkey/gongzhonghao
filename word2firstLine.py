import os
import docx
import re
#把word文档里面的第一行作为文件名
# 定义文件夹路径
folder_path = 'D:\BaiduNetdiskDownload\公众号文章采集下载器\application\ - word'

# 遍历文件夹下所有Word文档
for filename in os.listdir(folder_path):
    if filename.endswith('.docx'):
        # 打开Word文档
        doc = docx.Document(os.path.join(folder_path, filename))

        # 获取第一段的文本
        first_paragraph = doc.paragraphs[0].text

        # 剔除特殊符号
        regex = re.compile('[^\u4e00-\u9fa5a-zA-Z0-9_]')
        new_filename = regex.sub('', first_paragraph)

        # 重命名文件
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, f'{new_filename}.docx'))
