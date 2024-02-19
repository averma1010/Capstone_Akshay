# -*- coding: utf-8 -*-
"""
Author: Akshay Verma
Date: 2024-02-19
Version: 1.0
"""
import psycopg2 as ps 


class DatabaseConnector:
    def __init__(self, username, password) -> object:
        """

        :rtype: object
        :param username: My username
        :param password: My password
        """
        self.host = "complex2.phys.gwu.edu"  ## Hardcoding the host name
        self.dbname = "don_hate" ## Hardcoding the database
        self.username = username 
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = ps.connect(
                dbname=self.dbname,
                user=self.username,
                password=self.password,
                host=self.host
            )
            print("Connected to the database.")
        except Exception as e:
            print("Error connecting to the database:", e)

    def execute_query(self, query):

        """
        :param query: The SQL query to be executed
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            print("No active connection to close.")
