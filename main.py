import psycopg2
from collections import namedtuple

School = namedtuple('School', ['id', 'name', 'address', 'phone_number', 'davlat_maktabi'])

db = psycopg2.connect(
    database='5-OY 2-DARS',
    user='postgres',
    host='localhost',
    password='1',
)

cursor = db.cursor()

cursor.execute('''

-- 1 ##################################################################################################################################
CREATE TABLE avtomobillar (
    id SERIAL PRIMARY KEY,
    nomi VARCHAR(100) NOT NULL,
    model TEXT,
    yil INTEGER,
    narx NUMERIC(12, 2),
    mavjudmi BOOL DEFAULT TRUE
);

CREATE TABLE clientlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50),
    telefon CHAR(13),
    manzil TEXT
);

CREATE TABLE buyurtmalar (
    id SERIAL PRIMARY KEY,
    avtomobil_id INTEGER,
    client_id INTEGER,
    sana DATE NOT NULL,
    umumiy_narx NUMERIC(12, 2),
    FOREIGN KEY (avtomobil_id) REFERENCES avtomobillar(id),
    FOREIGN KEY (client_id) REFERENCES clientlar(id)
);

CREATE TABLE xodimlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    lavozim VARCHAR(50),
    maosh NUMERIC(10, 2)
);

-- 2 ##################################################################################################################################
ALTER TABLE clientlar
ADD COLUMN email VARCHAR(100);

ALTER TABLE clientlar
RENAME COLUMN ism TO first_name;

ALTER TABLE clientlar
RENAME TO mijozlar;

-- 3 ##################################################################################################################################
INSERT INTO avtomobillar (nomi, model, yil, narx) VALUES
('Toyota Corolla', 'Sedan', 2020, 22000.00),
('Honda Civic', 'Sedan', 2021, 25000.00),
('BMW X5', 'SUV', 2022, 45000.00);

INSERT INTO mijozlar (first_name, familiya, telefon, manzil, email) VALUES
('Ali', 'Valiev', '998901234567', 'Toshkent, Chilonzor', 'ali@example.com'),
('Olim', 'Akhmedov', '998907654321', 'Toshkent, Yunusobod', 'olim@example.com');

INSERT INTO buyurtmalar (avtomobil_id, client_id, sana, umumiy_narx) VALUES
(1, 1, '2024-11-01', 22000.00),
(2, 2, '2024-11-02', 25000.00);

INSERT INTO xodimlar (ism, lavozim, maosh) VALUES
('Daler', 'Meneger', 3000.00),
('Ravshan', 'Sotuvchi', 1500.00);

-- 4 ##################################################################################################################################
UPDATE xodimlar
SET ism = 'Azizbek'
WHERE id = 1;

UPDATE xodimlar
SET ism = 'Zafarbek'
WHERE id = 2;

-- 5 ##################################################################################################################################
DELETE FROM xodimlar
WHERE id = 2;

-- 6 ##################################################################################################################################
SELECT * FROM avtomobillar;

SELECT * FROM mijozlar;

SELECT * FROM buyurtmalar;

SELECT * FROM xodimlar;
''')

schools = cursor.fetchall()

for school in schools:
    school = School(*school)
    print(f"Name: {school.name}, Address: {school.address}")

db.commit()

db.close()
