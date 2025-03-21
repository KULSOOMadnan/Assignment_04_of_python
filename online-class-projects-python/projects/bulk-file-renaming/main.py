import os


def rename_file():
    i = 0 
    path = 'C:/Users/Axis-Main/Pictures/Screenshots/'
    for file_name in os.listdir(path):
        my_dest = 'img' + str(i) + '.jpg'
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source , my_dest)
        
        i += 1 
        
if __name__ == "__main__":
    rename_file()