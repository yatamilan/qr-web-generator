from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_url = None
    if request.method == 'POST':
        name = request.form.get('name')
        info = request.form.get('info')
        data = f"Name: {name}\nInfo: {info}"

        # Generate QR code
        img = qrcode.make(data)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)

        # Convert image to base64 string
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        qr_code_url = f"data:image/png;base64,{img_base64}"

    return render_template('index.html', qr_code_url=qr_code_url)

if __name__ == '__main__':
    app.run(debug=True)
