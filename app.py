import cv2
import pytesseract

def reading_image(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # 画像をグレースケールに変換する
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ノイズを軽減するために画像をぼかす
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # 画像からテキストを抽出する
    text = pytesseract.image_to_string(blurred, lang='eng')

    return text

# 画像からテキストを抽出する
image_path = 'image/clothes.jpeg'
text = reading_image(image_path)

print(text)