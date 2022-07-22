import collections
import streamlit as st
import pandas as pd

from visualizer import line_chart, pie

st.set_page_config(layout = "wide")

months = ["Mangsir 078","Poush 078","Magh 078","Falgun 078","Chaitra 078","Baishakh 079","Jestha 079","Asadh 079"]
count = 0
datas = []
for i in months:
    count = count + 1
    data = pd.ExcelFile('{}.xlsx'.format(i))
    sheet_numbers = len(data.sheet_names)
    for j in range(sheet_numbers):
        count_j = dict()
        current_sheet = pd.read_excel(data,'Sheet{}'.format(j+1))
        name = current_sheet.loc[[11],:]
        name = name['Unnamed: 5']
        working_Day = list(name)
        for k in working_Day:
            name = k 
        length = len(name)
        actual_len = length-4
        name = name[:actual_len]
        total_days = current_sheet.loc[[12],:]
        total_days= total_days['Unnamed: 13']
        total_day = list(total_days)
        for k in total_day:
            total_days = k

        working_Days = current_sheet.loc[[12],:]
        working_Days= working_Days['Unnamed: 20']
        working_Day = list(working_Days)
        for k in working_Day:
            working_Days = k        
        present_days = current_sheet.loc[[12],:]
        present_days= present_days['Unnamed: 24']
        total_day = list(present_days)
        for k in total_day:
            present_days = k
        Absent_Days = working_Days-present_days
        rows = len(current_sheet.axes[0])-1
        total_hrs = current_sheet.loc[[rows],:]
        total_hrs= total_hrs['Unnamed: 14']
        total_hr = list(total_hrs)
        for i in total_hr:
            total_hrs = i
        total_hrs  = total_hrs.replace(":",".")
        total_hrs = float(total_hrs)
        try:
            avg_total = total_hrs/float(present_days)
            avg_total = round(avg_total,2)
        except:
            avg_total = 0.0
            
        count_j["Name"] = name
        count_j["Total Days"] = total_days
        count_j["Working Days"] = working_Days
        count_j["Present Days"] = present_days
        count_j["Absent Days"] = Absent_Days
        count_j["Avg Hour"] = total_hrs
        datas.append(count_j)

names_lister = []
for i in datas:

    for key,value in i.items():
        if key == "Name":
            if value in names_lister:
                continue                            
            else:
                names_lister.append(value)
combined_dict = []       
for x in names_lister:
    combining_dict = []
    for i in datas:
        new_dict = dict()
        accessed = False
        for key,value in i.items():
            if key == "Name" and value == x:
                accessed = True
     
        while (accessed):
            combining_dict.append(i)
            accessed = False
    combined_dict.append(combining_dict)

finale_dict = []
for c in combined_dict:
    new_dict = dict()
    counter = 1
    for v in range(len(c)):        
        if v == 0:
            new_dict.update(c[v])
        else:
            
            for key_element,value_element in new_dict.items():
                for key,val in c[v].items():
                    if key_element == "Avg Hour":
                        counter += 1
                    if key_element == key and key != "Name":
                        new_dict[key] = value_element + val
        for keys,vals in new_dict.items():
            if keys == "Avg Hour":
                Hours = vals
            if keys == "Present Days":
                Date = vals
        try:
            new_dict["Avg Hours"] = Hours/Date
        except ZeroDivisionError:
            new_dict["Avg Hours"] = 0
    finale_dict.append(new_dict)
avg_list = []
name_list = []
total_hrs = []
present_days = []
absent_days = []
for l in finale_dict:
    for b,n in l.items():
        if b == "Avg Hours":
            avg_list.append(n)
        if b == "Avg Hour":
            total_hrs.append(n)
        if b == "Name":
            name_list.append(n) 
        if b == "Present Days":
            present_days.append(n) 
        if b == "Absent Days":
            absent_days.append(n) 





    


name_hr = dict()    
for q,w in zip(name_list,total_hrs):
    name_hr[q] = w
name_hr =  sorted(name_hr.items(), key=lambda x: x[1], reverse=True)

st.title(" ")
st.title(" ")

st.subheader("TOp 4 People with Highest Hour Spent")

st.title(" ")
st.title(" ")
col0,col1,col2,col3 = st.columns(4)
with col0:
    st.subheader(name_hr[0][0] + " : " + str(name_hr[0][1])+ "hr")
with col1:
    st.subheader(name_hr[1][0] + " : " + str(name_hr[1][1])+ "hr")
with col2:
    st.subheader(name_hr[2][0] + " : " + str(name_hr[2][1])+ "hr")
with col3:
    st.subheader(name_hr[3][0] + " : " + str(name_hr[3][1])+ "hr")
 
st.title(" ")
st.title(" ")

st.subheader("Bar Chart Showing Avg Duration of Each Indivisual in Office")

st.title(" ")
st.title(" ")
  
 
employee_bar = line_chart(name_list,avg_list)
st.pyplot(employee_bar)

columns1,columns2,columns3 = st.columns([2,1,2])
with columns2:
    staff_name = st.selectbox("Select Employee Name To see Detailed Info",(i for i in name_list))
counting_num = 0

for i in name_list:
    counting_num += 1
    if i == staff_name:
        absent = int(absent_days[counting_num-1])
        present = int(present_days[counting_num-1])
        columnss1,columnss2,columnss3 = st.columns([2,3,2])
        with columnss2:
            labels = ["Absent","Present"]
            values = [absent,present]
            fig2 = pie(labels,values)
            st.pyplot(fig2)