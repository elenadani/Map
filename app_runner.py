import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

con = sqlite3.connect("map_db.sqlite")
cur = con.cursor()
result_1 = cur.execute("""SELECT thing FROM Invention""").fetchall()
result_2 = cur.execute("""SELECT year FROM Invention""").fetchall()
result_3 = cur.execute("""SELECT coord_1 FROM Invention""").fetchall()
result_4 = cur.execute("""SELECT coord_2 FROM Invention""").fetchall()
result_5 = cur.execute("""SELECT URL_picture FROM Invention""").fetchall()

map_dict = dict()
map_dict['name'] = [result_1[i][0] for i in range(len(result_1))]
map_dict['year'] = [result_2[i][0] for i in range(len(result_2))]
map_dict['coord_1'] = [result_3[i][0] for i in range(len(result_3))]
map_dict['coord_2'] = [result_4[i][0] for i in range(len(result_4))]
map_dict['URL_picture'] = [result_5[i][0] for i in range(len(result_5))]

con.commit()
con.close()


@app.route('/')
def render_map():
    return render_template('map.html', map_dict=map_dict)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
