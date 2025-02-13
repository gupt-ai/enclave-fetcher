from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                response = requests.get(url)
                response_text = response.text
            except requests.exceptions.RequestException as e:
                response_text = f"Error: {e}"
    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7887, ssl_context=('./ssl/cert.pem', './ssl/key.pem')) 