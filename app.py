import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

SHOP_NAME = "NOMAN DRESS MATERIAL"
CONTACT = "9694262268"

@app.route('/')
def home():
    # Aapki photos ko dhoondne ke liye
    files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{SHOP_NAME}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background: #f8f9fa; padding-top: 20px; font-family: sans-serif; }}
            .navbar {{ background: #2c3e50; color: white; padding: 15px; text-align: center; margin-bottom: 20px; }}
            .card {{ border: none; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; overflow: hidden; }}
            .product-img {{ height: 300px; object-fit: cover; width: 100%; }}
            .btn-wa {{ background: #25d366; color: white; font-weight: bold; width: 100%; padding: 12px; text-decoration: none; display: inline-block; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="navbar"><h1>{SHOP_NAME}</h1></div>
        <div class="container text-center">
            <div class="row g-3">
    '''

    for filename in files:
        html += f'''
                <div class="col-md-4 col-6">
                    <div class="card">
                        <img src="/{filename}" class="product-img">
                        <a href="https://wa.me/91{CONTACT}?text=Mujhe ye design chahiye: {filename}" class="btn-wa">WhatsApp Order</a>
                    </div>
                </div>
        '''

    if not files:
        html += '<h3>Abhi koi photo nahi mili. GitHub par photos upload karein!</h3>'

    html += '</div></div></body></html>'
    return render_template_string(html)

@app.route('/<path:filename>')
def serve_file(filename):
    # Ye line photos ko dikhane ke liye zaroori hai
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)

