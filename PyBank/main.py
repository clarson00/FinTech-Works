#imports
from pathlib import Path
import csv



#Open file
relative_path=("data.csv")

with open(relative_path, 'r') as data:
    reader = csv.reader(data, delimiter=',', quotechar='|')
    header = next(reader)
    

    print(header)
    #x=list(reader)
    # number of months in file
    #no_months=len(x)
    #print(no_months)
    
    c=0
    max_i=[0,0]
    max_d=[0,0]
    total=0
    previous_pl=0
    changepl_list=[]
    total_changepl=0

    for i in reader:

        c+=1
        total= total+int(i[1])

        if int(i[1]) >= int(max_i[1]):
            max_i = i

        if int(i[1]) <= int(max_d[1]):
            max_d = i
        
        current_pl=int(i[1])
        change_pl = current_pl - previous_pl
        total_changepl +=change_pl
        previous_pl = current_pl
        changepl_list.append(change_pl)

print(changepl_list)


    
    






avg_change=total/c
print('\n' * 100)
print('-' * 60)
print(f"Total Months: {c}")
print(f'Total:  ${total}')
print(f'Average  Change:  ${round(total_changepl/(c),2)}')
print(f'Greatest Increase in Profits: {max_i[0]}  ${max_i[1]}')
print(f'Greatest Decrease in Profits: {max_d[0]}  ${max_d[1]}')

