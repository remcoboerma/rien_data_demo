
# pip install pydal
from pydal import DAL
db = DAL('sqlite://output.db')
#  voor verwerken:
rows = db.executesql('select * from data limit 10', as_dict=True)
for row in rows:
    print(row)



