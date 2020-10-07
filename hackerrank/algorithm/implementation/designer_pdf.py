# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max_area = 0
    for i in word:
        index = ord(i)-97
        if max_area < h[index]:
            max_area = h[index]
    return max_area * len(word)
