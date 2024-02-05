import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/centuries_19-20')
def render_map():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result_1 = cur.execute("""SELECT thing FROM Invention""").fetchall()
    result_2 = cur.execute("""SELECT year FROM Invention""").fetchall()
    result_3 = cur.execute("""SELECT coord_1 FROM Invention""").fetchall()
    result_4 = cur.execute("""SELECT coord_2 FROM Invention""").fetchall()
    result_5 = cur.execute("""SELECT URL_picture FROM Invention""").fetchall()
    result_6 = cur.execute("""SELECT icon FROM Invention""").fetchall()

    map_dict = dict()
    map_dict['name'] = [result_1[i][0] for i in range(len(result_1))]
    map_dict['year'] = [result_2[i][0] for i in range(len(result_2))]
    map_dict['coord_1'] = [result_3[i][0] for i in range(len(result_3))]
    map_dict['coord_2'] = [result_4[i][0] for i in range(len(result_4))]
    map_dict['URL_picture'] = [result_5[i][0] for i in range(len(result_5))]
    map_dict['icon'] = [result_6[i][0] for i in range(len(result_6))]

    con.commit()
    con.close()
    return render_template('map.html', map_dict=map_dict)


@app.route('/19_century')
def render_map_1():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result_1 = cur.execute("""SELECT thing FROM Invention WHERE century <= 1900""").fetchall()
    result_2 = cur.execute("""SELECT year FROM Invention WHERE century <= 1900""").fetchall()
    result_3 = cur.execute("""SELECT coord_1 FROM Invention WHERE century <= 1900""").fetchall()
    result_4 = cur.execute("""SELECT coord_2 FROM Invention WHERE century <= 1900""").fetchall()
    result_5 = cur.execute("""SELECT URL_picture FROM Invention WHERE century <= 1900""").fetchall()
    result_6 = cur.execute("""SELECT icon FROM Invention WHERE century <= 1900""").fetchall()

    map_dict = dict()
    map_dict['name'] = [result_1[i][0] for i in range(len(result_1))]
    map_dict['year'] = [result_2[i][0] for i in range(len(result_2))]
    map_dict['coord_1'] = [result_3[i][0] for i in range(len(result_3))]
    map_dict['coord_2'] = [result_4[i][0] for i in range(len(result_4))]
    map_dict['URL_picture'] = [result_5[i][0] for i in range(len(result_5))]
    map_dict['icon'] = [result_6[i][0] for i in range(len(result_6))]

    con.commit()
    con.close()
    return render_template('map.html', map_dict=map_dict)


@app.route('/20_century')
def render_map_2():
    con = sqlite3.connect("map_db.sqlite")
    cur = con.cursor()
    result_1 = cur.execute("""SELECT thing FROM Invention WHERE century > 1900""").fetchall()
    result_2 = cur.execute("""SELECT year FROM Invention WHERE century > 1900""").fetchall()
    result_3 = cur.execute("""SELECT coord_1 FROM Invention WHERE century > 1900""").fetchall()
    result_4 = cur.execute("""SELECT coord_2 FROM Invention WHERE century > 1900""").fetchall()
    result_5 = cur.execute("""SELECT URL_picture FROM Invention WHERE century > 1900""").fetchall()
    result_6 = cur.execute("""SELECT icon FROM Invention WHERE century > 1900""").fetchall()

    map_dict = dict()
    map_dict['name'] = [result_1[i][0] for i in range(len(result_1))]
    map_dict['year'] = [result_2[i][0] for i in range(len(result_2))]
    map_dict['coord_1'] = [result_3[i][0] for i in range(len(result_3))]
    map_dict['coord_2'] = [result_4[i][0] for i in range(len(result_4))]
    map_dict['URL_picture'] = [result_5[i][0] for i in range(len(result_5))]
    map_dict['icon'] = [result_6[i][0] for i in range(len(result_6))]

    con.commit()
    con.close()
    return render_template('map.html', map_dict=map_dict)


@app.route('/about')
def about_project():
    return "Hello"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
