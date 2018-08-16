import pandas as pd
student_data={'Name':['Lokesh','Nishant','Isha','Chandan'],
              'Roll No':[11,12,13,14],
              'Subject':['Deep Learning','Machine Learning','Artificial Inteligence','Python'],
              'Address':['Uttrakhand','Uttar Pradesh','Assam','Nepal']}
record=pd.DataFrame(student_data)
print(record)
