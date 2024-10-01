from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    return render_template('index.html')

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to save registration details
        return redirect(url_for('index'))
    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to verify user credentials
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
