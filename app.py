from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # name the application app after the file
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shreyaasridhar@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey(
        'todolists.id'), nullable=False)

    def __repr__(self):
        return f'< Todo {self.id}, {self.description}>'


class TodoList(db.Model):
    __tablename__ = "todolists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)


@app.route('/')
def index():
    return redirect(url_for('get_list_todos', listid=1))


@app.route('/lists/<listid>')
def get_list_todos(listid):
    return render_template('index.html', data=Todo.query.filter_by(list_id=listid).order_by('id').all())


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        desc = request.get_json()['description']
        todo = Todo(description=desc)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
        body['id'] = todo.id
        body['completed'] = todo.completed
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        return abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<todoid>/set-completed', methods=['POST'])
def set_completed(todoid):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todoid)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('index'))


@app.route('/todos/<todoid>/deleteitem', methods=['DELETE'])
def delete_item(todoid):
    print(todoid)
    try:
        Todo.query.filter_by(id=todoid).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})
