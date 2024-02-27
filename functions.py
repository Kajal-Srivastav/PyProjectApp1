def get_data():
    with open("filedata.txt" , 'r') as file:
        data = file.readlines()
        return data


def get_write(data):
    with open("filedata.txt", 'w') as file:
        file.writelines(data)

