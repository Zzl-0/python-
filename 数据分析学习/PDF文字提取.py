import PyPDF2

pdf_file = open('C:\\Users\\28893\\Desktop\\个人简历\\C++软件工程师.pdf', 'rb+')
pdf_reader = PyPDF2.PdfReader(pdf_file)  # 可以直接使用PDF文件路径

# 获取PDF文件的页数
num_pages = len(pdf_reader.pages)
# print(num_pages)

# 遍历页面进行处理
for  page_nums in range(num_pages):
    # 获取当前页面项
    page = pdf_reader.pages[page_nums]
    # print(page)
    # 获取页面内容
    text = page.extract_text()
    print('获取到的内容为；', text)