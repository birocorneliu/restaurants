from flask import Flask

import api_routes
import html_routes
from database_setup import Restaurant, MenuItem, session

app = Flask(__name__)

ROUTES = (
    #API urls
    ("/restaurant/JSON", api_routes.api_restaurants),
    ("/restaurant/<int:restaurant_id>/menu/JSON", api_routes.api_restaurant_menu),
    ("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON", api_routes.api_menu_item),

    #HTML urls
    ("/", html_routes.show_restaurants),
    ("/restaurant/", html_routes.show_restaurants),
    ("/restaurant/new/", html_routes.new_restaurant),
    ("/restaurant/<int:restaurant_id>/edit/", html_routes.edit_restaurant),
    ("/restaurant/<int:restaurant_id>/delete/", html_routes.delete_restaurant),
    ("/restaurant/<int:restaurant_id>/", html_routes.show_menu),
    ("/restaurant/<int:restaurant_id>/menu/", html_routes.show_menu),
    ("/restaurant/<int:restaurant_id>/menu/new/", html_routes.new_menu_item),
    ("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit", html_routes.edit_menu_item),
    ("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete", html_routes.delete_menu_item),
)

#route urls to functions
for path, method in ROUTES:
    app.add_url_rule(path, view_func=method)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
