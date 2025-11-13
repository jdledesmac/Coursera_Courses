from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    # STEP 3: YOUR CODE HERE
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():

    data = request.get_json()

    # STEP 4.2: Your code here
    if 'title' not in data and 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    # STEP 4.3: Your code here
    new_post={'id':len(posts)+1, 'title':data['title'], 'content':data['content']}
    
    posts.append(new_post)

    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(debug=True)