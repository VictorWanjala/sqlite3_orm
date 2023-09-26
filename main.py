import sqlite3
CONN = sqlite3.connect('orm.db')
CURSOR = CONN.cursor()

class Car:
    all = []
    def __init__(self, model,YOM):
        print('car obj initialised')
        self.model = model
        self.YOM = YOM
        self.add_to_all(self)


    @classmethod
    def add_to_all(cls, car):
        cls.all.append(car)

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS cars(
        id INTEGER PRIMARY KEY,
        model TEXT,
        YOM INTEGER
        )"""

        CURSOR.execute(sql)
    

    def save(self):
        sql =  """INSERT INTO cars (model, YOM) VALUES (?,?)"""
        CURSOR.execute(sql,(self.model, self.YOM))
    
    @classmethod
    def all_data(cls):
        sql = """SELECT * FROM cars"""
        all_items = CURSOR.execute(sql).fetchall()
        print(all_items)

    @classmethod
    def get_by_id(cls,id):
        sql = """SELECT * FROM cars WHERE id=? LIMIT 1"""
        car = CURSOR.execute(sql,(id,)).fetchone()
        print(car)
       
Car.create_table()
bmw = Car('X6',2018)
toyota = Car('supra',2020)
print(bmw)
bmw.save()
Car.all_data()
Car.get_by_id(2)
CONN.commit()



