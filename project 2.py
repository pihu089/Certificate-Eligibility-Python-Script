#certificate eligibility

print('------------Certificate Eligibility------------')

status = input('Enter Yes-for All day Attendance, No-for Day gap in Attendance = ')

if status == 'Yes':
    print('Hi! user pick the options for certificate eligibility')
    assignment = input('Enter Yes-if assignment done , No-if assignment not done = ')
    if assignment == 'Yes':
        print('Condition 1 Satisfied')
    else:
        print('User Not Eligible for Certificate')

    live_class = input('Enter Yes-if live class attended , No-if live class not attended = ')
    if live_class == 'Yes':
       print('Condition 2 Satisfied')
    else:
        print('User Not Eligible for Certificate')

    camera_on= input('Enter Yes-if camera on , No-if camera off = ')
    if camera_on == 'Yes':
       print('Condition 3 Satisfied, User is Eligible for Certificate') #all the condition are satisfied here  
    else:
        print('User Not Eligible for Certificate')      
        

if status == 'No':
    print('User Not Eligible for Certificate')                  



