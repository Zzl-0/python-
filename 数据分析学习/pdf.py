import fitz  # PyMuPDF
from googletrans import Translator


# 读取PDF文件并提取文本
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(pdf_file)
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text


# 将文本翻译成中文
def translate_to_chinese(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='zh-cn')
    return translated_text.text


if __name__ == "__main__":
    pdf_file_path = "C:\\bookPDF\\TCP-IP.Illustrated.Volume.1.The.Protocols.2nd.Edition.(z-lib.org).pdf"

    # 提取PDF中的英文文本
    english_text = extract_text_from_pdf(pdf_file_path)

    # 将英文文本翻译成中文
    chinese_text = translate_to_chinese(english_text)

    # 打印或保存翻译后的文本
    print(chinese_text)
