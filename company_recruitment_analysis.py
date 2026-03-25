import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'Amdocs']
recruitments = [120, 100, 150, 80, 90, 110, 70]

plt.figure()
plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xlabel("Companies")
plt.ylabel("No. of Students")
plt.xticks(rotation=30)
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

explode = [0.1,0,0,0,0,0,0]

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
circle = plt.Circle((0,0),0.70,fc='white')
plt.gca().add_artist(circle)
plt.title("Doughnut Chart")
plt.show()

plt.figure()
plt.bar(['IBM','Amdocs'], [80,70])
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Students")
plt.show()