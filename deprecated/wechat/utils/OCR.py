import easyocr


def OCR_extraction(msg):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext('ItChatDownloaded/' + msg.fileName, detail=0)

    return result
