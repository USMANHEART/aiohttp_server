import logging
import MySQLdb as mdb


def connect_db(db_name, sb_host, db_password, db_user):
    connection = 0
    try:
        connection = mdb.connect(sb_host, db_user, db_password, db_name)
        print("Success connection with Database!")
    except mdb.Error as e:
        print("Failed connection with Database!")
        print(e)
    return connection


def start_db():
    db = connect_db("web_db", "localhost", "123456", "root")
    cursor = None
    if db == 0:
        print("Error in Database connection")
    else:
        cursor = db.cursor()
    return db, cursor


def fetchone(_sql):
    db, cursor = start_db()
    result = 0
    logging.info("Query: " + _sql)
    print("Query: " + _sql)
    try:
        cursor.execute(_sql)
        result = cursor.fetchone()
        if result is not None:
            for res in result:
                result = res
                break
    except mdb.Error as e:
        print("Can't read data!")
        print(e)
    db.commit()
    db.close()
    return result


def fetchall(_sql):
    db, cursor = start_db()
    results = 0
    logging.info("Query: " + _sql)
    try:
        cursor.execute(_sql)
        results = cursor.fetchall()
    except mdb.Error as e:
        print("Can't read data!")
        print(e)
    db.commit()
    db.close()
    return results
