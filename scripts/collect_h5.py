import os,sys
sys.argv

inputs = sys.argv[1]

# read input file
with open(inputs, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    for line in lines:
        print(line)

outputs = inputs.replace('inputs.txt','outputs.txt')

file_path = os.path.abspath('658583_aggregated.h5')
the_dir = os.path.split(line)[0]
file_path = os.path.join(the_dir,'658583_aggregated.h5')

plot1_path = os.path.join(the_dir,'plot1.png')
plot2_path = os.path.join(the_dir,'plot2.png')
plot3_path = os.path.join(the_dir,'plot3.png')

# write outputs.txt file
with open(outputs, 'w', encoding='utf-8') as output_file:
    output_file.write(file_path + '\n')
    output_file.write(plot1_path + '\n')
    output_file.write(plot2_path + '\n')
    output_file.write(plot3_path + '\n')

# create the aggregated file (simulated)
with open(file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('this is a simulated aggregated H5 file')

# create plots (simulated)
with open(plot1_path, 'w', encoding='utf-8') as output_file:
    output_file.write('this is a simulated plot')

with open(plot2_path, 'w', encoding='utf-8') as output_file:
    output_file.write('this is a simulated plot')

with open(plot3_path, 'w', encoding='utf-8') as output_file:
    output_file.write('this is a simulated plot')

print('succesfully executed collect_h5.py')