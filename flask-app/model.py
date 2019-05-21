import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()


def getPosts(username):
    cur.execute("select * from user_posts where username='{}'".format(username))
    rows = cur.fetchall()
    resultlist = []
    for row in rows:
        resultlist.append({'id':row[0], 'post':row[1], 'username':row[2]})

    return resultlist

def createPost(post, username):
    cur.execute("insert into user_posts (post, username) values ('{}','{}')".format(post,username))
    conn.commit()
    print("Records inserted successfully")

#createPost('This is a second post','swaroop')
print(getPosts('swaroop'))

#conn.close()
