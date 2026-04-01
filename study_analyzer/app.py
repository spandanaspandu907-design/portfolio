from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():   # <-- return must be inside this function
    result = ""
    if request.method == "POST":
        try:
            hours = float(request.form.get("hours", 0))
            if hours >= 6:
                result = "Excellent! Keep it up 🏆👍"
            elif hours >= 3:
                result = "Good! Try a bit more 📈💡"
            else:
                result = "Poor! Increase your study hours ⚡😓"
        except ValueError:
            result = "Please enter a valid number!"

    # <-- the return is here, inside home()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Study Performance Analyzer</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f8ff;
                margin-top: 50px;
            }}
            input {{
                padding: 10px;
                width: 200px;
                font-size: 16px;
            }}
            button {{
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                background-color: #4caf50;
                color: white;
                border: none;
                border-radius: 5px;
            }}
            h1 {{
                color: #3333cc;
            }}
            h2 {{
                color: #cc3300;
                margin-top: 20px;
            }}
            form {{
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Smart Study Performance Analyzer</h1>
        <p>Enter your study hours:</p>
        <form method='POST'>
            <input type='text' name='hours' placeholder='Enter hours'>
            <button type='submit'>Analyze</button>
        </form>
        <h2>{result}</h2>
    </body>
    </html>
    """

app.run(debug=True)