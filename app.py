from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    """
    This function handles requests to the root URL (/)
    It returns an HTML response with the welcome message
    """
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MLOps Class</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome Areeba to this MLOPS Class.</h1>
        </div>
    </body>
    </html>
    """

# Run the application if this file is executed directly
if __name__ == '__main__':
    # debug=True: Enables auto-reload and detailed error messages
    # host='127.0.0.1': Only accessible from your computer
    # port=5000: The port number for the web server
    app.run(debug=True, host='127.0.0.1', port=5000)
