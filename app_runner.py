import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/centuries_19-20')
def render_map():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Invention WHERE id BETWEEN 1 AND 30""").fetchall()
    con.commit()
    con.close()
    return render_template('map.html', map_dict=result)


@app.route('/19_century')
def render_map_1():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Invention WHERE (century < 1901) AND id BETWEEN 1 AND 30""").fetchall()
    con.commit()
    con.close()
    return render_template('map.html', map_dict=result)


@app.route('/20_century')
def render_map_2():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Invention WHERE (century > 1900) AND id BETWEEN 1 AND 30""").fetchall()
    con.commit()
    con.close()
    return render_template('map.html', map_dict=result)


@app.route('/about')
def about_project():
    return render_template('about_project.html')


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
