# we can format printed output

temp = 20.12345
desc = 'sunny'
wind = 6.98765

report = 'The weather is {} with a wind speed of {} and a temperature of {}'
print(report.format(desc,wind,temp))

report = 'The weather is {1} with a wind speed of {2} and a temperature of {0}'
print(report.format(temp,desc,wind))

report = 'The weather is {1} with a wind speed of {2:0.2f}mph and a temperature of {0:0.1f}c'
print(report.format(temp,desc,wind))
