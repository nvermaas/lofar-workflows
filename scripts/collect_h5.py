import os,sys
sys.argv

inputs = sys.argv[1]

# read input file
with open(inputs, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    for line in lines:
        print(line)

outputs = inputs.replace('inputs.txt','outputs.txt')

# write outputs.txt file
with open(outputs, 'w', encoding='utf-8') as output_file:
    output_file.write('my_storage_location\\658584\\658583_aggregated.h5')

# write the aggregated file (simulated)
with open('my_storage_location\\658584\\658583_aggregated.h5', 'w', encoding='utf-8') as output_file:
    output_file.write('this is a simulated aggregated H5 file')


print('succesfully executed collect_h5.py')