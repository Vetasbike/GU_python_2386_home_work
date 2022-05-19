import os

my_val = ['settings','mainapp','adminapp','authapp']
my_key = 'my_project'
my_dict = {my_key : my_val}

dir_path = [os.makedirs(os.path.join(my_key,i)) for i in my_val if not os.path.exists(os.path.join(my_key,i))]

print(os.path.join(os.path.abspath(os.getcwd()), my_key))
my_path=os.path.join(os.path.abspath(os.getcwd()), my_key)
for i in my_val:
    print(os.path.join(my_path,i))
