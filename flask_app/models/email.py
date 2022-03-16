from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db = 'email_valid'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM emails WHERE id = %(id)s'
        return connectToMySQL(cls.db).query_db(query,data)