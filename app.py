import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Aapki shop ki details
SHOP_NAME = "NOMAN DRESS MATERIAL"
CONTACT = "7597660035"

@app.route('/')
def home():
    # Yeh line automatic static folder se saari photos dhoond legi
    static_folder = os.path.join(app.root_path, 'static')
    files = [f for f in os.listdir(static_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{SHOP_NAME}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background: #f8f9fa; font-family: 'Segoe UI', sans-serif; }}
            .navbar {{ background: #2c3e50; color: white; padding: 20px; text-align: center; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }}
            .card {{ border: none; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: 0.3s; background: white; }}
            .card:hover {{ transform: translateY(-5px); }}
            .product-img {{ height: 300px; object-fit: cover; width: 100%; border-top-left-radius: 15px; border-top-right-radius: 15px; }}
            .price {{ color: #e67e22; font-size: 1.4rem; font-weight: bold; }}
            .btn-wa {{ background: #25d366; color: white; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; padding: 12px; margin-top: 10px; }}
            .btn-wa:hover {{ background: #128c7e; color: white; }}
        </style>
    </head>
    <body>
        <div class="navbar"><h1>{SHOP_NAME}</h1></div>
        <div class="container mb-5">
            <h3 class="text-center mb-4">Hamara Naya Collection</h3>
            <div class="row g-4">
    '''

    for filename in files:
        html += f'''
                <div class="col-md-3 col-6">
                    <div class="card h-100">
                        <img src="/static/{filename}" class="product-img">
                        <div class="card-body text-center">
                            <h6 class="text-uppercase text-muted" style="font-size: 0.8rem;">Item Code: {filename.split('.')[0]}</h6>
                            <p class="price">Contact for Price</p>
                            <a href="https://wa.me/91{CONTACT}?text=Mujhe ye design chahiye: {filename}" class="btn-wa">Order on WhatsApp</a>
                        </div>
                    </div>
                </div>
        '''

    html += '''
            </div>
        </div>
        <footer class="text-center py-4 bg-dark text-white">© 2025 NOMAN DRESS MATERIAL</footer>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)