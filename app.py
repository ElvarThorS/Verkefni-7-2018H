#Elvar Þór Sævarsson
#Verkefni 7
#7.11.2018

import pymysql
from bottle import *

@get('/')
def index():
    return template('index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    # Connection object, búum til tengingu við gagnagrunn
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1106012980', passwd='mypassword', db='1106012980_vef2_demo')
    # Cursor object, used to manage the context of a fetch operation
    cur = conn.cursor()

    # Prepare and execute a database operation (query or command).
    # SQL fyrirspurn, sækjum notanda úr db
    cur.execute("SELECT count(*) FROM 1106012980_vef2_demo.users where user=%s",(u))
    # Fetch the next row of a query result set, returning a single sequence, or None when no more data is available.
    result = cur.fetchone() #fáum tuple (runa eða listi af read-only objectum)

    # notandi er ekki til
    if result[0] == 0:
        cur.execute("INSERT INTO 1106012980_vef2_demo.users Values(%s,%s,%s)", (u, p, n))
        # Commit any pending transaction to the database.
        conn.commit()
        cur.close()
        # lokum db tengingu
        conn.close()
        return u, " hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, " er frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1106012980', passwd='mypassword', db='1106012980_vef2_demo')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 1106012980_vef2_demo.users where user=%s and pass=%s",(u,p))
    result = cur.fetchone()#fáum tuple
    print(result)
    # er u og p til í db?
    if result[0] == 1:

        cur.close()
        conn.close()
        return template('leyni',u=u)
    else:
        return template('ekkileyni')

# Félagaskrá allir: "SELECT * FROM gjg_vef2_v77.users"
# delete FROM gjg_vef2_v77.users where user = 'toti';

@route('/members')
def member():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1106012980', passwd='mypassword', db='1106012980_vef2_demo')
    c = conn.cursor()
    c.execute("SELECT user FROM 1106012980_vef2_demo.users")
    result = c.fetchall() #fáum nöfnin í tuple lista
    c.close()
    output = template('members', rows=result)
    return output


 run(host='0.0.0.0', port=os.environ.get('PORT'), app=app)
