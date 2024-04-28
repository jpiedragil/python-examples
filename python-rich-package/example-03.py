from rich import inspect

superhero = {"person": {"name": "John Jones", "age":30, "address":{"street": "123 Main St", "city": "Gotham",
 "state":"NY", "zip_code": "12345"},
"superpowers":{"leaps_buildings":True,"factorizes_polynomials":False},
"contacts":[{"type":"email","value":"john.jones@heroes.are.us"},
{"type":"phone","value":"555-123-4567"}],
"hobbies": ["reading","hiking","coding","crimefighting"],
"family":{"spouse": {"name":"Griselda Jones", "age":28},
"children":[{"name":"Bellatrix", "age":5, "name":"Draco", "age":8}
]}}}

inspect(superhero, methods=True)