server:
	python server.py
db:
	python lib/database_setup.py
fulldb:
	python lib/populate_db.py && python lib/lotsofmenus.py

.PHONY: server db fulldb
