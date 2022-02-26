import os
folder_path = r'G:\3DOM\13_Imgs_aeree\aerial_trento\trento_gcp_proj'

file =os.listdir(folder_path)
#print(file)

with open('rearranged.txt', 'w') as new_file:
    for item in file:
        with open('{}/{}'.format(folder_path, item),'r') as targets:
            for line in targets:
                line = line.strip()
                id, x, y = line.split(" ", 3)      #id, x, y, bin = line.split(" ", 3)
                x = float(x) + 0.5 #x = float(x) * 1500/6048 + 0.5
                y = float(y) + 0.5 #y = float(y) * 1500/6048 + 0.5
                new_file.write("{},{},{},{}\n".format(id[0:],item[:-8],str(x),str(y)))