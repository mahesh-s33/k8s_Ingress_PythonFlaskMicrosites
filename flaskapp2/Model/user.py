from Database.database import CursorFromConnectionPool


class User:
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            cursor.execute("INSERT INTO users(email, first_name, last_name) " +
                           f"values('{self.email}', '{self.first_name}', '{self.last_name}')")

    @classmethod
    def load_data_using_email(cls, email):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(f"SELECT * from users where email = '{email}'")
            user_data = cursor.fetchone()
            user = User(id=user_data[0], email=user_data[1],
                        first_name=user_data[2], last_name=user_data[3])
            return user

    @classmethod
    def get_all_users(cls):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(f"SELECT * from users")
            user_data = cursor.fetchall()
            users = []
            for user in user_data:
                users.append(user)
            return users
