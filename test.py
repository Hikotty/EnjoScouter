import create_table

session = create_table.session
Enjyo = create_table.Enjyo

enjo =Enjyo(word = 'enjo',power = 10)
session.add(enjo)
session.commit()