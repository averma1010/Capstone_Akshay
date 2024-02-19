# -*- coding: utf-8 -*-
"""
Author: Your Name
Date: 2024-02-19
Version: 1.0
"""
import pandas as pd

class Person:
    def __init__(self, db_connector) -> object:
        """

        :rtype: object
        :param db_connector: instance of the DatabaseConnector class
        """
        self.db_connector = db_connector

    def flavors_count(self, start_date, end_date):
        """
        Function runs a query that gets the counts of  hate type between certain dates. Does server side processing for faster execution 
        :param start_date: Start of Date range
        :param end_date: End of Date range
        """
        query = (
            "SET TIME ZONE 'utc';"
            "SELECT "
            "    date_trunc('day', p.created_at) AS ds, "
            "    SUM(CASE WHEN f.religion_prediction THEN 1 ELSE 0 END) AS religion_prediction_count, "
            "    SUM(CASE WHEN f.race_prediction THEN 1 ELSE 0 END) AS race_prediction_count, "
            "    SUM(CASE WHEN f.gender_prediction THEN 1 ELSE 0 END) AS gender_prediction_count, "
            "    SUM(CASE WHEN f.giso_prediction THEN 1 ELSE 0 END) AS giso_prediction_count, "
            "    SUM(CASE WHEN f.immigration_prediction THEN 1 ELSE 0 END) AS immigration_prediction_count, "
            "    SUM(CASE WHEN f.ein_prediction THEN 1 ELSE 0 END) AS ein_prediction_count, "
            "    SUM(CASE WHEN f.antisemitism_prediction THEN 1 ELSE 0 END) AS antisemitism_prediction_count "
            "FROM "
            "    posts p "
            "JOIN "
            "    flavors f ON p.don_id = f.don_id "
            "WHERE "
            "    p.created_at >= '{start_date}'::timestamp AND p.created_at < '{end_date}'::timestamp "
            "GROUP BY "
            "    date_trunc('day', p.created_at);"
        )
        results = self.db_connector.execute_query(query)
        df = pd.DataFrame(results, columns=["Day", "religion_prediction_count", "race_prediction_count", "gender_prediction_count", "giso_prediction_count", "immigration_prediction_count", "ein_prediction_count", "antisemitism_prediction_count"])
        return df