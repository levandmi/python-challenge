import os
import csv



#set path for employee data csv
emppath = os.path.join('employee_data.csv')
#open employee data csv
with open(emppath, newline='') as empfile:
    #read employee data csv as a csv file
    empreader = csv.reader(empfile, delimiter=',')

    #remove header
    empheader = next(empreader)

    #move colums into lists
    empid = []
    empname = []
    empdob = []
    empssn = []
    empstat = []
    for row in empreader:
        empid.append(row[0])
        empname.append(row[1])
        empdob.append(row[2])
        empssn.append(row[3])
        empstat.append(row[4])
    
    #splitting names
    firstname = []
    lastname = []
    for row in empname:
        firstname.append(row.split(' ')[0])
        lastname.append(row.split(' ')[1])

    #moidify date of birth
    day = []
    month = []
    year = []
    for row in empdob:
        year.append(row.split('-')[0])
        month.append(row.split('-')[1])
        day.append(row.split('-')[2])

    newdate = []
    for i in range(len(month)):
        newdate.append(month[i] + '/' + day[i] + '/' + year[i])
  
    #hiding the first 5 numnbers of SSN
    hiddenssn = []
    for ssn in empssn:
         hiddenssn.append("***-**-" + ssn[-4:])

    #state change
    stateab = []
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

    for state in empstat:
        stateab.append(us_state_abbrev[state])

    #creating new list
    newlist = zip(empid, firstname, lastname, newdate, hiddenssn, stateab)

    newheader = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

    bossoutpath = os.path.join('bossexport.csv')
    with open(bossoutpath, 'w', newline='') as bossoutfile:
        bossoutwriter = csv.writer(bossoutfile, delimiter=',')
        bossoutwriter.writerow(newheader)
        bossoutwriter.writerows(newlist)

        