import sys
sys.argv

# read input file
with open('inputs.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    for line in lines:
        print(line)

# write output file
with open('outputs.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('my_storage_location\658584\658583_aggregated.h5')

print('succesfully executed collect_h5.py')