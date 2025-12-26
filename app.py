import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

SHOP_NAME = "NOMAN DRESS MATERIAL"
CONTACT = "7597660035"

@app.route('/')
def home():
    # Ye photos dhoondne ka sabse asan tarika hai
    files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{SHOP_NAME}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background: #f4f4f4; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
            .header {{ background: #8e44ad; color: white; padding: 20px; text-align: center; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }}
            .card {{ border: none; border-radius: 15px; overflow: hidden; transition: 0.3s; background: white; }}
            .card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }}
            .product-img {{ height: 300px; object-fit: cover; width: 100%; }}
            .btn-wa {{ background: #25d366; color: white; font-weight: bold; width: 100%; padding: 12px; text-decoration: none; display: block; text-align: center; font-size: 1.1rem; }}
        </style>
    </head>
    <body>
        <div class="header"><h1>{SHOP_NAME}</h1><p>Hamare naye designs dekhein</p></div>
        <div class="container">
            <div class="row g-4">
    '''

    for filename in files:
        html += f'''
                <div class="col-md-4 col-sm-6">
                    <div class="card">
                        <img src="/{filename}" class="product-img">
                        <div class="p-2 text-center">
                            <h5 class="mt-2">{filename.split('.')[0]}</h5>
                            <a href="https://wa.me/91{CONTACT}?text=Salam, mujhe ye design chahiye: {filename}" class="btn-wa">WhatsApp Order</a>
                        </div>
                    </div>
                </div>
        '''

    if not files:
        html += '<div class="col-12 text-center"><h3>Abhi koi photo upload nahi ki gayi hai.</h3></div>'

    html += '</div></div><footer class="text-center mt-5 mb-4 text-muted">© 2025 {SHOP_NAME}</footer></body></html>'
    return render_template_string(html)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
