from flask import jsonify
from lib.database_setup import Restaurant, MenuItem, session


def api_restaurant_menu(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[item.serialize for item in items])


def api_menu_item(restaurant_id, menu_id):
    menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(menu_item=menu_item.serialize)


def api_restaurants():
    restaurants = session.query(Restaurant).all()
    return jsonify(restaurants=[res.serialize for res in restaurants])
