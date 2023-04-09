from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_area = request.form['text_area']
        range_slider = request.form['range_slider'].split(',')
        small_text = request.form['small_text']
        select_text = request.form['select_text']
        select_function = request.form['select_function']
        
        return f"Введенный текст: {text_area}<br>Диапазон: {range_slider[0]} - {range_slider[1]}<br>Маленький текст: {small_text}<br>Выбранный текст: {select_text}<br>{select_function}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
