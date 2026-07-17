import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="linkdin",
    user="postgres",
    password=" ",
    port=5432,
)