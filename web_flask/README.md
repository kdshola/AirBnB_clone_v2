Flask and jinja modules

0-hello_route.py
A script that starts a Flask web application:

Listening on 0.0.0.0, port 5000
Routes:
/: displays “Hello HBNB!”

1-hbnb_route.py
adds route to previous app
/hbnb: displays “HBNB”

2-c_route.py
adds route to previous app
/c/<text>: displays “C ” followed by the value of the text variable (replace underscore _ symbols with a space )

3-python_route.py
adds route to previous app
/python/<text>: displays “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”

4-number_route.py
adds route to previous app:
/number/<n>: displays “n is a number” only if n is an integer

5-number_template.py
adds route to previous app:
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY

6-number_odd_or_even.py
adds route to previous app:
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY

7-states_list.py
A script that starts a Flask web application:
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>

8-cities_by_states.py
A script that starts a Flask web application:
Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>

10-hbnb_filters.py
A script that starts a Flask web application:
Routes:
/states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
/states/<id>: display a HTML page: (inside the tag BODY)
If a State object is found with this id:
H1 tag: “State: ”
H3 tag: “Cities:”
UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
H1 tag: “Not found!”

100-hbnb.py
A script that starts a Flask web application:
Routes:
/hbnb_filters: display a HTML page 6-index.html.
