from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId


def get_reports():
    '''
    Returns all user reports
    '''
    user_id = g.user['id']
    reports = g.db.reports.find({'_user_id': user_id})
    return list(reports)


def create_report():
    '''
    Creates new report
    '''
    user_id = g.user['id']
    report = {'_user_id': user_id, 'name': 'New Report'}
    g.db.reports.insert_one(report)
    return report
