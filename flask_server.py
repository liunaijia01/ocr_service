from flask import Flask, request
import ocr_service

app = Flask(__name__)

@app.route('/pic2text', methods=['GET', 'POST'])
def pic2text():
    if request.method == 'POST':
        img_url = request.form.get('img_url', '')
    else:
        img_url = request.args.get('img_url', '')
    output = ""
    if img_url:
        output = ocr_service.convert_from_url(img_url)
    return output