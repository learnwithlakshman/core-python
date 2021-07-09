data = "1001-Krish-CS,1002-Manoj-IS,1003-Charan-IS,1004-RK-IS,1005-ALN-EC,1006-PKM-CS,1007-RKS-IS,1008-GLN-EC,1008-KM-CS"

def map_data():
    lst = data.split(",")
    f_map = {}
    for item in lst:
        fdata = item.split("-")
        faculty = {'id':fdata[0],'name':fdata[1],'dept':fdata[2]}
        dept = faculty['dept']
        if f_map.get(dept):
            lst = f_map[dept]
            lst.append(faculty)
            f_map[dept] = lst
        else:
           f_map[dept] = [faculty]
    return f_map



def get_faculty_by_dept(deptname):
    dept_f_map = map_data()
    return dept_f_map.get(deptname)

def get_faculty_name(deptname):
    dept_f_map = map_data()
    if dept_f_map.get(deptname):
        return [f['name'] for f in dept_f_map.get(deptname)]

lst = get_faculty_by_dept("CS")
print(lst)

print(get_faculty_name("CS"))