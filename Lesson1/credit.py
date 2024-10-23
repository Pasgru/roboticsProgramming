from flask import Flask, request 
import sqlite3

app = Flask(__name__)

def getconn():
    return sqlite3.connect("credit.db")

@app.route("/")
def credit():
    return """<h1>Credit App</h1>
    <ul>
    <li><a href=clients>Clients</a></li>
    <li><a href=newclient>New Client</a></li>
    <li><a href=initdb>Init DB</a></li>
    </ul>"""
    
@app.route('/initdb')
def initdb():
    conn = getconn()
    cur = conn.cursor()
    cur.execute("drop table if exists client")
    cur.execute("create table client "
    + "(id int primary key, lim int, sex int, edu int, mar int, age int)")
    conn.commit()
    conn.close()
    return "DB initialized."

@app.route('/clients')
def clients():
    conn = getconn()
    cur = conn.cursor()
    rows = cur.execute("select id, lim from client limit 500")
    html = "<h3>Clients</h3><table>\n" 
    for row in rows:
        html +=  "<tr><td align=right> %d <td align=right> %.2f\n" % row
    return html + "</table>\n"
    conn.close()
    
@app.route('/newclient')
def newclient():
    return """<h3>New Client</h3>
    <form action=insertclient method=POST>
    <table>
    <tr><td>Client ID:<td><input type=text name=id>
    <tr><td>Credit Limit:<td><input type=text name=lim>
    <tr><td>Sex:<td><input type=text name=sex value=1>
    <tr><td>Education:<td><input type=text name=edu value=1>
    <tr><td>Marriage:<td><input type=text name=mar value=1>
    <tr><td>Age:<td><input type=text name=age value=30>
    </table><input type=submit value=OK></form>"""
       
@app.route('/insertclient', methods=['POST'])
def insertclient():
    id = request.form['id']
    lim = request.form['lim']
    sex = request.form['sex']
    edu = request.form['edu']
    mar = request.form['mar']
    age = request.form['age']
    conn = getconn()
    cur = conn.cursor()
    cur.execute('insert into client (id, lim, sex, edu, mar, age) '
        + ' values (?, ?, ?, ?, ?, ?)', (id, lim, sex, edu, mar, age))
    conn.commit()
    conn.close()
    return "Client inserted."

app.run(host='localhost', port=8080, debug=True, use_reloader=True)