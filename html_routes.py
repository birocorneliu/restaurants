from flask import render_template, request, redirect, url_for
from database_setup import Restaurant, MenuItem, session


#Show all restaurants
def show_restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


#Create a new restaurant
def new_restaurant():
    if request.method == 'POST':
        restaurant = Restaurant(name=request.form['name'])
        session.add(restaurant)
        session.commit()
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('new_restaurant.html')


#Edit a restaurant
def edit_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            restaurant.name = request.form['name']
            return redirect(url_for('show_restaurants'))
    else:
        return render_template('edit_restaurant.html', restaurant=restaurant)


#Delete a restaurant
def delete_restaurant(restaurant_id):
    restaurants = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurants)
        session.commit()
        return redirect(url_for('show_restaurants',
                                restaurant_id=restaurant_id))
    else:
        return render_template('delete_restaurant.html', restaurant=restaurants)


#Show a restaurant menu
def show_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)


#Create a new menu item
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'],
                            description=request.form['description'],
                            price=request.form['price'],
                            course=request.form['course'],
                            restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()

        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html',
                               restaurant_id=restaurant_id)
	#return render_template('new_menu_item.html', restaurant=restaurant)


#Edit a menu item
def edit_menu_item(restaurant_id, menu_id):
    edited_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['description']:
            edited_item.description = request.form['name']
        if request.form['price']:
            edited_item.price = request.form['price']
        if request.form['course']:
            edited_item.course = request.form['course']
        session.add(edited_item)
        session.commit()
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:

        return render_template('edit_menu_item.html',
                               restaurant_id=restaurant_id,
                               menu_id=menu_id,
                               item=edited_item)


#Delete a menu item
def delete_menu_item(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html', item=itemToDelete)
