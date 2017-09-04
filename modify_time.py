import numpy as np
import sys
import re
import itertools

myfile = sys.argv[1]
time_file = sys.argv[2]
out_file = open('output_file.xdmf', 'w')
fieldOut=1000

step_series = []
time_series = []
#be caution with the first step. if it starts with 1, copy one extra line 
with open(time_file) as input_lines:
     nthlines=itertools.islice(input_lines, 0, None, fieldOut)
     for line in nthlines:
        data = line.split()
        step_series.append(int(data[0]))
        time_series.append(float(data[1]))

step_series = np.array(step_series)
time_series = np.array(time_series)
print time_series
with open(myfile) as input_lines:
    for line in input_lines:
        if "<Time" in line:
            step = re.search(r'\d+', line).group()
            number = int(re.search(r'\d+', line).group())
            print number
            curr_time = time_series[np.where(step_series == number)[0][0]]
            curr_replace = 'Value="' + str(curr_time) + '"'
            line = re.sub(r'Value="\d+"',curr_replace,line)
        out_file.write(line)

