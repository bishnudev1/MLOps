from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', items=items)

items = [
    {
        "id": 1,
        "title": "Item 1",
        "task": "This is item 1"
    },
    {
        "id": 2,
        "title": "Item 2",
        "task": "This is item 2"
    },
    {
        "id": 3,
        "title": "Item 3",
        "task": "This is item 3"
    }
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return render_template('index.html', items=items)

# Get single item
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    for item in items:
        if item['id'] == id:
            return jsonify({
                "success": True,
                "message": "Item retrieved successfully",
                "data": item
            })
    return jsonify({
        "success": False,
        "message": "Item not found",
        "data": None
    })

# Add new item
@app.route('/add-item', methods=['POST'])
def add_item():
    title = request.form['title']
    task = request.form['task']
    
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "title": title,
        "task": task
    }
    items.append(new_item)
    return redirect(url_for('index'))

# Delete item
@app.route('/delete-item/<int:id>', methods=['DELETE'])
def delete_item(id):
    for item in items:
        if item['id'] == id:
            items.remove(item)
            return redirect(url_for('index'))
    return jsonify({
        "success": False,
        "message": "Item not found",
        "data": None
    })

# Update item
@app.route('/update-item/<int:id>', methods=['PUT'])
def update_item(id):
    if not request.is_json:
        return jsonify({
            "success": False,
            "message": "Request must be JSON",
            "data": None
        }), 415

    data = request.get_json()
    for item in items:
        if item['id'] == id:
            item['title'] = data.get('title', item['title'])
            item['task'] = data.get('task', item['task'])
            return jsonify({
                "success": True,
                "message": "Item updated successfully",
                "data": item
            })
    return jsonify({
        "success": False,
        "message": "Item not found",
        "data": None
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
