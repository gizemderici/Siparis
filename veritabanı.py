
import sqlite3 as sql
def veritabani_kur(isim:str):
    db = sql.connect(f"{isim}.sqlite")
    cursor = db.cursor()
   
    return db , cursor
def tablo_olustur(table_name:str , cursor , col_name:str ):
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} ({col_name})
"""
    cursor.execute(query)


def tabloya_info_ekle(db, cursor, table_name: str, col_name:str , values: str):
    query = f"""
    INSERT INTO {table_name} ({col_name}) VALUES ({values})
"""
    cursor.execute(query)
    db.commit()


def urunleri_cek(cursor, table_name: str):
    select_query = f"""
    SELECT * FROM {table_name} 
"""
    cursor.execute(select_query)
    return cursor.fetchall() #satırları tümünü içeren bir liste olarak döndürür


def veritabani_kapat(db):
    db.close()

