from flask import Flask, render_template, request
import ai_api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_area = request.form['text_area']
        range_slider = request.form['range_slider'].split(',')
        small_text = request.form['small_text']
        select_text = request.form['select_text']
        select_function = request.form['select_function']
        answer = ai_api.api(text_area, small_text, range_slider[0], range_slider[1], select_function, select_text)
        return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Ответ</title><style>body {display: flex;justify-content: center;align-items: center;height: 100vh;margin: 0;font-family: Arial, sans-serif;}.container {width: 80%;text-align: center;}.rounded-rectangle {background-color: #007BFF;padding: 20px 40px;border-radius: 10px;color: #fff;font-size: 24px;display: inline-block;}</style></head><body><div class="container"><div class="rounded-rectangle">' + answer + '</div></div></body></html>'
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
