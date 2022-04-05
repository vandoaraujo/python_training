from typing import Any
from datetime import date
import psycopg2
import urllib.parse as up


def obter_usuarios():
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('select * from account')
        registros = cursor.fetchall()
        return registros
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()
                print('Database connection closed.')

def obter_usuario(id):
    print(id)
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('select * from account where user_id = ' + id)
        registros = cursor.fetchall()
        for registro in registros:
            return registro
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()
                print('Database connection closed.')

def inserir_account(account):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        sql = """
            insert into account(user_id, username,password,email,created_on)
             values (%s,%s,%s,%s,%s)
        """
        cursor.execute(sql,(account['user_id'],
                        account['username'],
                        account['password'],
                        account['email'],
                        date.today(),)
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.commit()
                conn.close()
                print('Database connection closed.')

def modifica_conta(account):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        sql = """
            update account
                set username = %s,
                    password = %s,
                    email = %s
                where user_id = %s
        """
        cursor.execute(sql,(account['username'],
                        account['password'],
                        account['email'],
                        account['user_id'],)
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.commit()
                conn.close()
                print('Database connection closed.')


def deletar_conta(id):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('delete from account where user_id = ' + id)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.commit()
                conn.close()
                print('Database connection closed.')

def obter_conexao():
    conn = psycopg2.connect(
            host="localhost",
            database="school",
            user="xpto",
            password="xpto")
    return conn

if __name__ == "__main__":
    obter_usuarios()