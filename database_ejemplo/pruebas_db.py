from Database import PSConnection
conn = PSConnection()
query = """
INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
VALUES (%s, %s, NOW());
"""
parametros = ('usuario07','5678')

conn.query(query,parametros)


query2 = """
SELECT PUBLIC."USUARIO".usu_id,usu_pass,usu_fecha_registro
FROM PUBLIC."USUARIO";
"""

usuarios = conn.fetch_all(query2,None)
print(usuarios)

'''
[
    ('usuario01', '1234', datetime.datetime(2021, 6, 17, 0, 48, 9, 436194)), 
    ('usuario02', '1234', datetime.datetime(2021, 6, 17, 0, 49, 15, 460495)), 
    ('usuario03', '1234', datetime.datetime(2021, 6, 17, 0, 52, 19, 186020)), 
    ('usuario04', '1234', datetime.datetime(2021, 6, 17, 0, 52, 19, 186020)), 
    ('usuario05', '1234', datetime.datetime(2021, 6, 17, 0, 52, 19, 186020)), 
    ('Nicoffee', '1234', datetime.datetime(2021, 6, 17, 1, 13, 29, 574768)), 
    ('usuario06', '5678', datetime.datetime(2021, 6, 24, 0, 50, 13, 545569))
]

'''
