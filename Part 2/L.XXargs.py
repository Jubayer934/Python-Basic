#XXargs

#works like dictionary

def student(**details):
    print(details['name'])
    print(details['id'])


student(id=101,name='jubayer')