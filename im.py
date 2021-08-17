import streamlit as st
import plotly.express as px
import pandas as pd
from functools import reduce
import plotly.graph_objects as go

df=pd.read_csv("C:/Users/j.elachkar/Desktop/internal_medicine_F.csv")
df1=pd.read_csv("C:/Users/j.elachkar/Desktop/internal_medicine.csv")
df1['visit_date']=pd.to_datetime(df1['visit_date'])
print(df.tail())
df['visit_date']=pd.to_datetime(df['visit_date'])
df['month']=df['visit_date'].dt.month
df['year']=df['visit_date'].dt.year
df['day']=df['visit_date'].dt.day
df['period'] = df['month'].astype(str) + "-" +df['year'].astype(str)
df['period'] = pd.to_datetime(df['period'])
df['period'] = df['period'].dt.strftime('%Y-%m')
print(df['period'])


st.header("Internal Medicine Dashboard - AMAN Hospital")



#1st visualization: total bill breakdown
df_1= df[['period','order_type','fees ']]
print(df_1.head())
df_1l=df_1[df_1['order_type']=='Lab'].groupby('period').agg(total_lab=('fees ',sum))
df_1l=df_1l.reset_index('period')
print(df_1l)
df_1r=df_1[df_1['order_type']=='Radiology '].groupby('period').agg(total_radiology=('fees ',sum))
df_1r=df_1r.reset_index('period')
print(df_1r)
df_1lr=pd.merge(df_1l,df_1r,left_on='period',right_on='period',how='left')
print(df_1lr)

df_1c=df_1[df_1['order_type']=='consultation '].groupby('period').agg(total_consult=('fees ',sum))
df_1c=df_1c.reset_index('period')

df_1o=df_1[df_1['order_type']=='other_diagnostics '].groupby('period').agg(total_other_diag=('fees ',sum))
df_1o=df_1o.reset_index('period')
print(df_1o)

df_1co=pd.merge(df_1c,df_1o,left_on='period',right_on='period',how='left')
print(df_1co)

df_1lrco=pd.merge(df_1lr,df_1co,left_on='period',right_on='period',how='left')
print(df_1lrco)


if st.sidebar.checkbox("Click to view: Internal Medicine Total Charges"):
    st.sidebar.markdown("Internal Medicine - Overall Monthly Charges")
    select = st.sidebar.selectbox("Select a chart type", ['Line Chart', 'Bar Chart'])
    st.subheader("Internal Medicine - Overall Monthly Charges")
    if select == 'Line Chart':
        fig = px.line(df_1lrco, x='period', y=['total_lab', 'total_radiology', 'total_consult', 'total_other_diag'])
        st.plotly_chart(fig)
    else:
        select == 'Bar Chart'
        fig1 = px.bar(df_1lrco, x='period', y=['total_lab', 'total_radiology', 'total_consult', 'total_other_diag'])
        st.plotly_chart(fig1)



#2nd visualization
# table of cardiology
df2 = df[['period','order_type','department ','fees ']]
print(df2.head())
df2cons_card=df2[(df2['order_type']=='consultation ') & (df2['department ']=='cardiology ')].groupby('period').agg(cardio_cons=('fees ',sum))
df2cons_card=df2cons_card.reset_index('period')
print(df2cons_card)

df2Lab_cardio =df2[(df2['order_type']=='Lab') & (df2['department ']=='cardiology ')].groupby('period').agg(cardio_Lab=('fees ',sum))
df2Lab_cardio=df2Lab_cardio.reset_index('period')
print(df2Lab_cardio)

df2other_diag_cardio=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='cardiology ')].groupby('period').agg(cardio_total_others=('fees ',sum))
df2other_diag_cardio=df2other_diag_cardio.reset_index('period')
print(df2other_diag_cardio)

df2rad_card=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='cardiology ')].groupby('period').agg(cardio_radio=('fees ',sum))
df2rad_card=df2rad_card.reset_index('period')
print(df2rad_card)


# table of endocrinology

df2cons_end=df2[(df2['order_type']=='consultation ') & (df2['department ']=='Endocrinology')].groupby('period').agg(endocrino_cons=('fees ',sum))
df2cons_end=df2cons_end.reset_index('period')
print(df2cons_end)

df2Lab_end =df2[(df2['order_type']=='Lab') & (df2['department ']=='Endocrinology')].groupby('period').agg(endocrino_Lab=('fees ',sum))
df2Lab_end=df2Lab_end.reset_index('period')
print(df2Lab_end)

df2other_diag_end=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='Endocrinology')].groupby('period').agg(endocrino_total_others=('fees ',sum))
df2other_diag_end=df2other_diag_end.reset_index('period')
print(df2other_diag_end)

df2rad_end=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='Endocrinology')].groupby('period').agg(endocrino_radio=('fees ',sum))
df2rad_end=df2rad_end.reset_index('period')
print(df2rad_end)


# general medicine table
df2cons_General_Med=df2[(df2['order_type']=='consultation ') & (df2['department ']=='General_Medicine ')].groupby('period').agg(General_Medocrino_cons=('fees ',sum))
df2cons_General_Med=df2cons_General_Med.reset_index('period')
print(df2cons_General_Med)

df2Lab_General_Med =df2[(df2['order_type']=='Lab') & (df2['department ']=='General_Medicine ')].groupby('period').agg(General_Medocrino_Lab=('fees ',sum))
df2Lab_General_Med=df2Lab_General_Med.reset_index('period')
print(df2Lab_General_Med)

df2other_diag_General_Med=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='General_Medicine ')].groupby('period').agg(General_Medocrino_total_others=('fees ',sum))
df2other_diag_General_Med=df2other_diag_General_Med.reset_index('period')
print(df2other_diag_General_Med)

df2rad_General_Med=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='General_Medicine ')].groupby('period').agg(General_Medocrino_radio=('fees ',sum))
df2rad_General_Med=df2rad_General_Med.reset_index('period')
print(df2rad_General_Med)



# # table of GI
df2cons_GI=df2[(df2['order_type']=='consultation ') & (df2['department ']=='GI')].groupby('period').agg(GI_cons=('fees ',sum))
df2cons_GI=df2cons_GI.reset_index('period')
print(df2cons_GI)

df2Lab_GI =df2[(df2['order_type']=='Lab') & (df2['department ']=='GI')].groupby('period').agg(GI_Lab=('fees ',sum))
df2Lab_GI=df2Lab_GI.reset_index('period')
print(df2Lab_GI)

df2other_diag_GI=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='GI')].groupby('period').agg(GI_total_others=('fees ',sum))
df2other_diag_GI=df2other_diag_GI.reset_index('period')
print(df2other_diag_GI)

df2rad_GI=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='GI')].groupby('period').agg(GI_radio=('fees ',sum))
df2rad_GI=df2rad_GI.reset_index('period')
print(df2rad_GI)

# table ID

df2cons_ID=df2[(df2['order_type']=='consultation ') & (df2['department ']=='Infectious_Disease')].groupby('period').agg(INFECTIOUS_DISEASE_cons=('fees ',sum))
df2cons_ID=df2cons_ID.reset_index('period')
print(df2cons_ID)

df2Lab_ID =df2[(df2['order_type']=='Lab') & (df2['department ']=='Infectious_Disease')].groupby('period').agg(INFECTIOUS_DISEASE_Lab=('fees ',sum))
df2Lab_ID=df2Lab_ID.reset_index('period')
print(df2Lab_ID)

df2other_diag_ID=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='Infectious_Disease')].groupby('period').agg(INFECTIOUS_DISEASE_total_others=('fees ',sum))
df2other_diag_ID=df2other_diag_ID.reset_index('period')
print(df2other_diag_ID)

df2rad_ID=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='Infectious_Disease')].groupby('period').agg(INFECTIOUS_DISEASE_radio=('fees ',sum))
df2rad_ID=df2rad_ID.reset_index('period')
print(df2rad_ID)


# table of nephrology
df2cons_Nephrology =df2[(df2['order_type']=='consultation ') & (df2['department ']=='Nephrology ')].groupby('period').agg(NEPHROLOGY_cons=('fees ',sum))
df2cons_Nephrology =df2cons_Nephrology .reset_index('period')
print(df2cons_Nephrology )

df2Lab_NEPHROLOGY=df2[(df2['order_type']=='Lab') & (df2['department ']=='Nephrology ')].groupby('period').agg(NEPHROLOGY_Lab=('fees ',sum))
df2Lab_NEPHROLOGY = df2Lab_NEPHROLOGY.reset_index('period')
print(df2Lab_NEPHROLOGY)

df2other_diag_Nephrology =df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='Nephrology ')].groupby('period').agg(NEPHROLOGY_total_others=('fees ',sum))
df2other_diag_Nephrology =df2other_diag_Nephrology .reset_index('period')
print(df2other_diag_Nephrology )

df2rad_Nephrology =df2[(df2['order_type']=='Radiology ') & (df2['department ']=='Nephrology ')].groupby('period').agg(NEPHROLOGY_radio=('fees ',sum))
df2rad_Nephrology =df2rad_Nephrology .reset_index('period')
print(df2rad_Nephrology )

# table of Neurology


df2cons_Neurology=df2[(df2['order_type']=='consultation ') & (df2['department ']=='Neurology ')].groupby('period').agg(neurology_cons=('fees ',sum))
df2cons_Neurology=df2cons_Neurology.reset_index('period')
print(df2cons_Neurology)

df2Lab_NEUROLOGY =df2[(df2['order_type']=='Lab') & (df2['department ']=='Neurology ')].groupby('period').agg(neurology_lab=('fees ',sum))
df2Lab_NEUROLOGY= df2Lab_NEUROLOGY .reset_index('period')
print(df2Lab_NEUROLOGY )

df2other_diag_Neurology=df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='Neurology ')].groupby('period').agg(neuro_tot_others=('fees ',sum))
df2other_diag_Neurology=df2other_diag_Neurology.reset_index('period')
print(df2other_diag_Neurology)

df2rad_Neurology=df2[(df2['order_type']=='Radiology ') & (df2['department ']=='Neurology ')].groupby('period').agg(neurology_radio=('fees ',sum))
df2rad_Neurology=df2rad_Neurology.reset_index('period')
print(df2rad_Neurology)

# pulmonary
df2cons_Pulmonary =df2[(df2['order_type']=='consultation ') & (df2['department ']=='Pulmonary ')].groupby('period').agg(con_pulmo=('fees ',sum))
df2cons_Pulmonary =df2cons_Pulmonary .reset_index('period')
print(df2cons_Pulmonary )

df2Lab_PULMONARY  =df2[(df2['order_type']=='Lab') & (df2['department ']=='Pulmonary ')].groupby('period').agg(pulmo_lab=('fees ',sum))
df2Lab_PULMONARY = df2Lab_PULMONARY  .reset_index('period')
print(df2Lab_PULMONARY  )

df2other_diag_Pulmonary =df2[(df2['order_type']=='other_diagnostics ') & (df2['department ']=='Pulmonary ')].groupby('period').agg(pulmo_tot_other=('fees ',sum))
df2other_diag_Pulmonary =df2other_diag_Pulmonary .reset_index('period')
print(df2other_diag_Pulmonary )

df2rad_Pulmonary =df2[(df2['order_type']=='Radiology ') & (df2['department ']=='Pulmonary ')].groupby('period').agg(pulmo_radio=('fees ',sum))
df2rad_Pulmonary =df2rad_Pulmonary .reset_index('period')
print(df2rad_Pulmonary )



# #compile the list of dataframes you want to merge
data_frames = [df2cons_card, df2Lab_cardio, df2other_diag_cardio,df2rad_card,df2cons_end,df2Lab_end,df2other_diag_end,df2rad_end,
               df2cons_General_Med,df2Lab_General_Med,df2other_diag_General_Med,df2rad_General_Med,
               df2cons_GI,df2Lab_GI,df2other_diag_GI,df2rad_GI,
               df2cons_Nephrology,df2Lab_NEPHROLOGY,df2other_diag_Nephrology,df2rad_Nephrology,
               df2cons_Neurology,df2Lab_NEUROLOGY,df2other_diag_Neurology,df2rad_Neurology,
               df2cons_Pulmonary,df2Lab_PULMONARY ,df2other_diag_Pulmonary,df2rad_Pulmonary,df2cons_ID,df2Lab_ID ,df2other_diag_ID,df2rad_ID]
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['period'],
                                            how='outer'), data_frames)

df_merged = df_merged.fillna(0)
print(df_merged)

if st.sidebar.checkbox("click to view: Total Charges by department"):
    st.sidebar.markdown("Charges by Department")
    selectbo = st.sidebar.selectbox("Select a department",
                                    ['Cardiology', 'Endocrinology', 'GI', 'ID', 'Neurology', 'Nephrology',
                                     'General_Medicine', 'Pulmonary'])

    st.subheader("Internal Medicine - Charges by Department ")
    if selectbo=='Cardiology':
        fig3=px.line(df_merged,x='period',y=['cardio_cons','cardio_Lab','cardio_total_others','cardio_radio'])
        st.plotly_chart(fig3)
    elif selectbo =='Endocrinology':
        fig4=px.line(df_merged,x='period',y=['endocrino_cons','endocrino_Lab','endocrino_total_others','endocrino_radio'])
        st.plotly_chart(fig4)
    elif selectbo =='GI':
        fig5=px.line(df_merged,x='period',y=['GI_cons','GI_Lab','GI_total_others','GI_radio'])
        st.plotly_chart(fig5)
    elif selectbo =='ID':
        fig6=px.line(df_merged,x='period',y=['INFECTIOUS_DISEASE_cons','INFECTIOUS_DISEASE_Lab','INFECTIOUS_DISEASE_total_others','INFECTIOUS_DISEASE_radio'])
        st.plotly_chart(fig6)
    elif selectbo =='Neurology':
        fig7=px.line(df_merged,x='period',y=['neurology_cons','neurology_lab','neuro_tot_others','neurology_radio'])
        st.plotly_chart(fig7)
    elif selectbo =='Nephrology':
        fig8 = px.line(df_merged,x='period',y=['NEPHROLOGY_cons','NEPHROLOGY_Lab','NEPHROLOGY_total_others','NEPHROLOGY_radio'])
        st.plotly_chart(fig8)
    elif selectbo =='General_Medicine':
        fig9=px.line(df_merged,x='period',y=['General_Medocrino_cons','General_Medocrino_Lab','General_Medocrino_total_others','General_Medocrino_radio'])
        st.plotly_chart(fig9)
    else:
        selectbo =='Pulmonary'
        fig10 =px.line(df_merged,x='period',y=['con_pulmo','pulmo_lab','pulmo_tot_other','pulmo_radio'])
        st.plotly_chart(fig10)

# visualization # 3
if st.sidebar.checkbox("Click to view : Geographical Distribution of AMAN Patients"):
    st.sidebar.markdown("Geographical distribution of AMAN Patients")
    slider = st.sidebar.slider("Select Hour", min_value=8, max_value=17)
    modified_data = df1[df1['visit_date'].dt.hour == slider]
    st.markdown("Geographical Location of AMAN Patients")
    st.markdown("%i patient between %i:00 and %i:00" % (len(modified_data),slider,(slider+3)%24))
    st.map(modified_data)


# visualization # 4 - number of visits per day

# extract day and month only from visit date ( month in a letter form, %m in a number format)

df['daymonth'] = df['visit_date'].dt.strftime('%B-%d')
df['MONTH']=df['visit_date'].dt.strftime('%B')
dfd = df[['daymonth','doctor_name','MONTH','coverage']]


#table showing days
# dfd1=dfd[dfd['doctor_name']=='Dr_H_Ismaeel'].groupby(['daymonth'],sort=False).agg(Number_of_Visits_Dr_H_Ismaeel=('coverage','count'))
# dfd1=dfd1.reset_index('daymonth')


dfd2= dfd[dfd['doctor_name']=='Dr_H_Ismaeel'].groupby(['MONTH'],sort=False).agg(Dr_Hussain_Ismaeel=('coverage','count'))
dfd2=dfd2.reset_index('MONTH')


dfd3=dfd[dfd['doctor_name']=='Dr_A_Khalil '].groupby(['MONTH'],sort=False).agg(Dr_Ali_Khalil=('coverage','count'))
dfd3=dfd3.reset_index('MONTH')


dfd4=dfd[dfd['doctor_name']=='Dr_D_Sleiman'].groupby(['MONTH'],sort=False).agg(Dr_Dana_Sleiman=('coverage','count'))
dfd4=dfd4.reset_index('MONTH')


dfd6=dfd[dfd['doctor_name']=='Dr_L_Semaan '].groupby(['MONTH'],sort=False).agg(Dr_Lea_Semaan=('coverage','count'))
dfd6=dfd6.reset_index('MONTH')


dfd7=dfd[dfd['doctor_name']=='Dr_Nephrology '].groupby(['MONTH'],sort=False).agg(Dr_Nephrology=('coverage','count'))
dfd7=dfd7.reset_index('MONTH')


dfd8=dfd[dfd['doctor_name']=='Dr_O_Dbouni '].groupby(['MONTH'],sort=False).agg(Dr_Ousayma_Dbouni=('coverage','count'))
dfd8=dfd8.reset_index('MONTH')


dfd9=dfd[dfd['doctor_name']=='Dr_P_Bou_Khalil '].groupby(['MONTH'],sort=False).agg(Dr_Pierre_Bou_Khalil=('coverage','count'))
dfd9=dfd9.reset_index('MONTH')


dfd10=dfd[dfd['doctor_name']=='Dr_R_Ahdab '].groupby(['MONTH'],sort=False).agg(Dr_Rushdi_Ahdab=('coverage','count'))
dfd10=dfd10.reset_index('MONTH')

data_f = [dfd2,dfd3,dfd4,dfd6,dfd7,dfd8,dfd9,dfd10]
df_merged1=reduce(lambda left,right:pd.merge(left,right,on=['MONTH'],
                                             how='outer'),data_f)
df_merged1=df_merged1.fillna(0)
# getting sum of number of visits for each physician
df_merged2=df_merged1[['Dr_Hussain_Ismaeel']]
dfdd = df_merged2.agg(total_num=('Dr_Hussain_Ismaeel', sum))
dfdd = dfdd.reset_index()

df_merged3=df_merged1[['Dr_Ali_Khalil']]
dfdd1 = df_merged3.agg(total_num=('Dr_Ali_Khalil', sum))
dfdd1 = dfdd1.reset_index()

df_merged4=df_merged1[['Dr_Dana_Sleiman']]
dfdd2 = df_merged4.agg(total_num=('Dr_Dana_Sleiman', sum))
dfdd2 = dfdd2.reset_index()

df_merged5=df_merged1[['Dr_Lea_Semaan']]
dfdd3 = df_merged5.agg(total_num=('Dr_Lea_Semaan', sum))
dfdd3 = dfdd3.reset_index()

df_merged6=df_merged1[['Dr_Nephrology']]
dfdd4 = df_merged6.agg(total_num=('Dr_Nephrology', sum))
dfdd4 = dfdd4.reset_index()

df_merged7=df_merged1[['Dr_Ousayma_Dbouni']]
dfdd5 = df_merged7.agg(total_num=('Dr_Ousayma_Dbouni', sum))
dfdd5 = dfdd5.reset_index()


df_merged8=df_merged1[['Dr_Pierre_Bou_Khalil']]
dfdd8 = df_merged8.agg(total_num=('Dr_Pierre_Bou_Khalil', sum))
dfdd8 = dfdd8.reset_index()

df_merged9=df_merged1[['Dr_Rushdi_Ahdab']]
dfdd9 = df_merged9.agg(total_num=('Dr_Rushdi_Ahdab', sum))
dfdd9 = dfdd9.reset_index()
dfdd9['Dr_Rushdi_Ahdab'] = dfdd9['Dr_Rushdi_Ahdab'].astype(int)
values_1 = [dfdd,dfdd1,dfdd2,dfdd3,dfdd4,dfdd5,dfdd8,dfdd9]
df_visits = reduce(lambda left,right:pd.merge(left,right,on=['index'],how='outer'),values_1)
df_visits = df_visits.drop(columns=['index'])

#

values = [df_visits['Dr_Hussain_Ismaeel'][0],
          df_visits['Dr_Ali_Khalil'][0],
          df_visits['Dr_Dana_Sleiman'][0],
          df_visits['Dr_Lea_Semaan'][0],
          df_visits['Dr_Nephrology'][0],
          df_visits['Dr_Ousayma_Dbouni'][0],
          df_visits['Dr_Pierre_Bou_Khalil'][0],
          df_visits['Dr_Rushdi_Ahdab'][0]]

if st.sidebar.checkbox("Click to view: Number of Patients Visits per Physician"):
    col1,col2=st.columns(2)

    # regular pie chart coding
    # figt = px.pie(df_visits, names=df_visits.columns, values=values,
    #               title="Total Number of patients visits per physician")
    # # figt.update_traces(textposition='inside', textinfo='percent+label')
    # figt.update_traces(hoverinfo='label+percent', textinfo='value + percent', textfont_size=20,
    #                   marker=dict(line=dict(color='#000000', width=1)))
    # st.plotly_chart(figt)

    # pull is given as a fraction of the pie radius
    with col1:
        st.subheader("Total number of patients visits")
        fig = go.Figure(data=[go.Pie(labels=df_visits.columns, values=values, pull=[0, 0, 0, 0, 0.2, 0, 0, 0])])
        fig.update_layout(legend=dict(orientation="h"),width=470,height=470)
        st.plotly_chart(fig)

    with col2:
        st.sidebar.markdown("Number of Patients Visits per Physician per Month")
        st.subheader("Number of Patients Visits per Physician per Month")
        selectbo1 = st.sidebar.selectbox("select a physician name", ['Line Chart', 'Bar Chart'])
        if selectbo1 == 'Line Chart':
            fig20 = px.line(df_merged1, x='MONTH',
                            y=['Dr_Hussain_Ismaeel', 'Dr_Ali_Khalil', 'Dr_Dana_Sleiman', 'Dr_Lea_Semaan',
                               'Dr_Nephrology', 'Dr_Ousayma_Dbouni', 'Dr_Pierre_Bou_Khalil', 'Dr_Rushdi_Ahdab'], width=500,height=500)
            st.plotly_chart(fig20)
        else:
            selectbo1 == 'Bar Chart'
            fig21 = px.bar(df_merged1, x='MONTH',
                           y=['Dr_Hussain_Ismaeel', 'Dr_Ali_Khalil', 'Dr_Dana_Sleiman', 'Dr_Lea_Semaan',
                              'Dr_Nephrology', 'Dr_Ousayma_Dbouni', 'Dr_Pierre_Bou_Khalil', 'Dr_Rushdi_Ahdab'])
            st.plotly_chart(fig21)


# visualization # 5

df_vis5= df[['period','doctor_name','order_type','fees ']]
df_50 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_H_Ismaeel')].groupby('period').agg(cons_ism=('fees ',sum))
df_50=df_50.reset_index('period')
print(df_50)

df_51 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_H_Ismaeel')].groupby('period').agg(lab_ism=('fees ',sum))
df_51=df_51.reset_index('period')
print(df_51)

df_52 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_H_Ismaeel')].groupby('period').agg(rad_ism=('fees ',sum))
df_52=df_52.reset_index('period')
print(df_52)

df_53 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_H_Ismaeel')].groupby('period').agg(other_diag_ism=('fees ',sum))
df_53=df_53.reset_index('period')
print(df_53)

huss = [df_50,df_51,df_52,df_53]
df_h = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),huss)
df_h=df_h.fillna(0)
print(df_h)


# dr ali khalil
df_54 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_A_Khalil ')].groupby('period').agg(cons_ali=('fees ',sum))
df_55=df_54.reset_index('period')
print(df_54)

df_55 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_A_Khalil ')].groupby('period').agg(lab_ali=('fees ',sum))
df_55=df_55.reset_index('period')
print(df_55)

df_56 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_A_Khalil ')].groupby('period').agg(rad_ali=('fees ',sum))
df_56=df_56.reset_index('period')
print(df_56)

df_57 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_A_Khalil ')].groupby('period').agg(other_diag_ali=('fees ',sum))
df_57=df_57.reset_index('period')
print(df_57)

v1=[df_54,df_55,df_56,df_57]
df_ali = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),v1)
df_ali=df_ali.fillna(0)
print(df_ali)

# dr dana sleiman
df_58 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_D_Sleiman')].groupby('period').agg(cons_dana=('fees ',sum))
df_58=df_58.reset_index('period')
print(df_58)

df_59 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_D_Sleiman')].groupby('period').agg(lab_dana=('fees ',sum))
df_59=df_59.reset_index('period')
print(df_59)

df_60 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_D_Sleiman')].groupby('period').agg(rad_dana=('fees ',sum))
df_60=df_60.reset_index('period')
print(df_60)

df_61 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_D_Sleiman')].groupby('period').agg(other_diag_dana=('fees ',sum))
df_61=df_61.reset_index('period')
print(df_61)

dd= [df_58,df_59,df_60,df_61]
df_dana= reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dd)
df_dana = df_dana.fillna(0)
print(df_dana)


# lea semaan
df_62 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_L_Semaan ')].groupby('period').agg(cons_lea=('fees ',sum))
df_62=df_62.reset_index('period')
print(df_62)

df_63 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_L_Semaan ')].groupby('period').agg(lab_lea=('fees ',sum))
df_63=df_63.reset_index('period')
print(df_63)

df_64 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_L_Semaan ')].groupby('period').agg(rad_lea=('fees ',sum))
df_64=df_64.reset_index('period')
print(df_64)

df_65 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_L_Semaan ')].groupby('period').agg(other_diag_lea=('fees ',sum))
df_65=df_65.reset_index('period')
print(df_65)

dl=[df_62,df_63,df_64,df_65]
df_lea = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dl)
df_lea = df_lea.fillna(0)
print(df_lea)


# nephrology
df_66 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_Nephrology ')].groupby('period').agg(cons_nephro=('fees ',sum))
df_66=df_66.reset_index('period')
print(df_66)

df_67 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_Nephrology ')].groupby('period').agg(lab_nephro=('fees ',sum))
df_67=df_67.reset_index('period')
print(df_67)

df_68 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_Nephrology ')].groupby('period').agg(rad_nephro=('fees ',sum))
df_68=df_68.reset_index('period')
print(df_68)

df_69 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_Nephrology ')].groupby('period').agg(other_diag_nephro=('fees ',sum))
df_69=df_69.reset_index('period')
print(df_69)

dn =[df_66,df_67,df_68,df_69]
df_neph = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dn)
df_neph=df_neph.fillna(0)
print(df_neph)

# oussayma dbouni
df_70 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_O_Dbouni ')].groupby('period').agg(cons_dbouni=('fees ',sum))
df_70=df_70.reset_index('period')
print(df_70)

df_71 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_O_Dbouni ')].groupby('period').agg(lab_dbouni=('fees ',sum))
df_71=df_71.reset_index('period')
print(df_71)

df_72 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_O_Dbouni ')].groupby('period').agg(rad_dbouni=('fees ',sum))
df_72=df_72.reset_index('period')
print(df_72)

df_73 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_O_Dbouni ')].groupby('period').agg(other_diag_dbouni=('fees ',sum))
df_73=df_73.reset_index('period')
print(df_73)

dfdb = [df_70,df_71,df_72,df_73]
df_dbouni= reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dfdb)
df_dbouni= df_dbouni.fillna(0)
print(df_dbouni)

# bou khalil
df_80 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_P_Bou_Khalil ')].groupby('period').agg(cons_boukhalil=('fees ',sum))
df_80=df_80.reset_index('period')
print(df_80)

df_81 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_P_Bou_Khalil ')].groupby('period').agg(lab_boukhalil=('fees ',sum))
df_81=df_81.reset_index('period')
print(df_81)

df_82 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_P_Bou_Khalil ')].groupby('period').agg(rad_boukhalil=('fees ',sum))
df_82=df_82.reset_index('period')
print(df_82)

df_83 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_P_Bou_Khalil ')].groupby('period').agg(other_diag_boukhalil=('fees ',sum))
df_83=df_83.reset_index('period')
print(df_83)

dfp = [df_80,df_81,df_82,df_83]
df_boukhalil = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dfp)
df_boukhalil = df_boukhalil.fillna(0)
print(df_boukhalil)

# ahdab

df_90 = df_vis5[(df_vis5['order_type']=='consultation ')&(df['doctor_name']=='Dr_R_Ahdab ')].groupby('period').agg(cons_ahdab=('fees ',sum))
df_90=df_90.reset_index('period')
print(df_90)

df_91 = df_vis5[(df_vis5['order_type']=='Lab')&(df['doctor_name']=='Dr_R_Ahdab ')].groupby('period').agg(lab_ahdab=('fees ',sum))
df_91=df_91.reset_index('period')
print(df_91)

df_92 = df_vis5[(df_vis5['order_type']=='Radiology ')&(df['doctor_name']=='Dr_R_Ahdab ')].groupby('period').agg(rad_ahdab=('fees ',sum))
df_92=df_92.reset_index('period')
print(df_92)

df_93 = df_vis5[(df_vis5['order_type']=='other_diagnostics ')&(df['doctor_name']=='Dr_R_Ahdab ')].groupby('period').agg(other_diag_ahdab=('fees ',sum))
df_93=df_93.reset_index('period')
print(df_93)

dfa = [df_90,df_91,df_92,df_93]
df_ah = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dfa)
df_ahdab= df_ah.fillna(0)
print(df_ahdab)

dffin = [df_h,df_ali,df_dana,df_lea,df_neph,df_dbouni,df_boukhalil,df_ahdab]
df_finale = reduce(lambda left,right:pd.merge(left,right,on=['period'],how='outer'),dffin)
df_finale= df_finale.fillna(0)
print(df_finale)

# chart 5

if st.sidebar.checkbox("Click to view: Side by Side plot: Charges by Physician"):
    col1,col2=st.columns(2)
    with col1:
        select = st.selectbox("Select Bill Component", ['Lab', 'Radiology', 'Consultation', 'Other_diagnostics'])
        # st.subheader("Bill component Charges")
        if select == 'Lab':
            fig90=px.line(df_finale,x='period',
                          y=['lab_ism','lab_ali','lab_dana','lab_lea','lab_nephro','lab_dbouni',
                                                'lab_ahdab','lab_boukhalil'],width=470,height=470)
            fig90.update_layout(
                legend=dict(
                    x=0,
                    y=1,
                    traceorder="reversed",
                    title_font_family="Times New Roman",
                    font=dict(
                        family="Courier",
                        size=12,
                        color="black"
                    ),
                    bgcolor="LightSteelBlue",
                    bordercolor="Black",
                    borderwidth=2
                )
            )

            st.plotly_chart(fig90)


        elif select =='Radiology':
            fig91=px.line(df_finale,x='period',y=['rad_ism','rad_ali','rad_dana','rad_lea','rad_nephro','rad_dbouni',
                                    'rad_ahdab','rad_boukhalil'],width=470,height=470)
            fig91.update_layout(
                legend=dict(
                    x=0,
                    y=1,
                    traceorder="reversed",
                    title_font_family="Times New Roman",
                    font=dict(
                        family="Courier",
                        size=12,
                        color="black"
                    ),
                    bgcolor="LightSteelBlue",
                    bordercolor="Black",
                    borderwidth=2
                )
            )
            st.plotly_chart(fig91)

        elif select =='Consultation':
            fig92=px.line(df_finale,x='period',y=['cons_ism','cons_ali','cons_dana','cons_lea','cons_nephro','cons_dbouni',
                        'cons_ahdab','cons_boukhalil'],width=470,height=470)
            fig92.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor='left',
                x=0.01

            ))
            st.plotly_chart(fig92)

        else:
            select =='Other_diagnostics'
            fig93=px.line(df_finale,x='period',y=['other_diag_ism','other_diag_ali','other_diag_dana','other_diag_lea','other_diag_nephro','other_diag_dbouni',
            'other_diag_ahdab','other_diag_boukhalil'],width=470,height=470)
            fig93.update_layout(legend=dict(
                yanchor='top',
                y=0.9,
                xanchor='left',
                x=0.01

            ))
            st.plotly_chart(fig93)

    with col2:
        select1 = st.selectbox("Select a Physician",['Dr_Hussain_Ismaeel','Dr_Ruchdi_Ahdab','Dr_Ali_Khalil',
                                                             'Dr_Ousayma_Dbouni','Dr_Lea_Semaan','Dr_Pierre_Bou_Khalil',
                                                             'Dr_Dana_Sleiman','Dr_Nephrology'])
        # st.subheader("charges by physician name")

        if select1 == 'Dr_Hussain_Ismaeel':
            fig100=px.line(df_finale,x='period',y=['cons_ism','lab_ism','rad_ism','other_diag_ism'],width=470,height=470)
            st.plotly_chart(fig100)
        elif select1 =='Dr_Ruchdi_Ahdab':
            fig101 = px.line(df_finale,x='period',y=['cons_ahdab','lab_ahdab','rad_ahdab','other_diag_ahdab'],width=470,height=470)
            st.plotly_chart(fig101)
        elif select1 =='Dr_Ali_Khalil':
            fig102=px.line(df_finale,x='period',y=['cons_ali','lab_ali','rad_ali','other_diag_ali'],width=470,height=470)
            st.plotly_chart(fig102)
        elif select1 == 'Dr_Ousayma_Dbouni':
            fig103=px.line(df_finale,x='period',y=['cons_dbouni','lab_dbouni','rad_dbouni','other_diag_dbouni'],width=470,height=470)
            st.plotly_chart(fig103)
        elif select1 =='Dr_Lea_Semaan':
            fig104 =px.line(df_finale,x='period',y=['cons_lea','lab_lea','rad_lea','other_diag_lea'],width=470,height=470)
            st.plotly_chart(fig104)
        elif select1== 'Dr_Nephrology':
            fig105=px.line(df_finale,x='period',y=['cons_nephro','lab_nephro','rad_nephro','other_diag_nephro'],width=470,height=470)
            st.plotly_chart(fig105)
        elif select =='Dr_Pierre_Bou_Khalil':
            fig106 = px.line(df_finale,x='period',y=['cons_boukhalil','lab_boukhalil','rad_boukhalil','other_diag_boukhalil'],width=470,height=470)
            st.plotly_chart(fig106)
        else:
            select =='Dr_Dana_Sleiman'
            fig107 = px.line(df_finale,x='period',y=['cons_dana','lab_dana','rad_dana','other_diag_dana'],width=470,height=470)
            st.plotly_chart(fig107)

# chart 6
# income statement
# def format(x):
#     return "${:.1f}K".format(x/1000)

datap = [['Jan-2021',100000,70000,65000,48000,75000,65000,98000,78000,65000,58000,115000,101000,93000,85000,51000,35000],
         ['Feb-2021',89000,71000,85000,65000,78000,65000,58000,41000,98000,78000,101000,105000,128000,98000,150000,125000],
         ['Mar-2021',45000,31000,71000,85000,65000,78000,65000,58000,41000,98000,78000,101000,105000,128000,98000,150000],
         ['Apr-2021',112000,67000,55000,38000,65000,55000,88000,68000,55000,48000,105000,111000,83000,75000,41000,25000],
         ['May-2021',134000,92000,75000,55000,68000,55000,48000,31000,88000,78000,101000,105000,118000,58000,130000,105000],
         ['Jun-2021',141000,98000,61000,75000,55000,48000,65000,48000,41800,68000,68000,91000,85000,118000,91000,78000],
         ['Jul-2021',145000,110000,55000,38000,69000,55000,88000,68000,41000,48000,105000,100000,83000,79000,31000,25000],
         ['Aug-2021',123000,87000,65000,38000,95000,85000,108000,100000,55000,48000,125000,111000,133000,75000,141000,125000],
         ['Sep-2021',165000,123000,51000,75000,25000,48000,65000,48000,31800,58000,68000,81000,85000,118000,71000,58000],
         ['Oct-2021', 189000,145000,95000,68000,69000,55000,78000,68000,41000,48000,95000,810000,83000,79000,31000,25000],
         ['Nov-2021',190000,154000,65000,38000,95000,75000,88000,630000,55000,48000,125000,98000,133000,75000,112000,99000],
         ['Dec-2021', 210000,160000,41000,35000,25000,48000,55000,38000,31800,48000,88000,71000,75000,48000,111000,58000]]
dfii = pd.DataFrame(datap,columns=['Period1','Cardiology_Revenues','Cardiology_Expenses','Endocrinology_Revenues','Endocrinology_Expenses','GI_Revenues','GI_Expenses','General_Med_Revenues','General_Med_Expenses','Neurology_Revenues','Neurology_Expenses','ID_Revenues','ID_Expenses','Pulmonary_Revenues','Pulmonary_Expenses','Nephrology_Revenues','Nephrology_Expenses'])

dfii['Net_Income_Cardiology']= dfii['Cardiology_Revenues'] - dfii['Cardiology_Expenses']
dfii['Net_Income_Endocrino']= dfii['Endocrinology_Revenues'] - dfii['Endocrinology_Expenses']
dfii['Net_Income_GI']= dfii['GI_Revenues'] - dfii['GI_Expenses']
dfii['Net_Income_General_Med']= dfii['General_Med_Revenues'] - dfii['General_Med_Expenses']
dfii['Net_Income_Neurology']= dfii['Neurology_Revenues'] - dfii['Neurology_Expenses']
dfii['Net_Income_ID']= dfii['ID_Revenues'] - dfii['ID_Expenses']
dfii['Net_Income_Pulmonary']= dfii['Pulmonary_Revenues'] - dfii['Pulmonary_Expenses']
dfii['Net_Income_Nephrology']= dfii['Nephrology_Revenues'] - dfii['Nephrology_Expenses']
dfii['Period1']=pd.to_datetime(dfii['Period1'])
# i am limititing to Month and Year
dfii['Period1']=dfii["Period1"].dt.strftime('%B-%Y')

# dfii['Cardiology_Revenues']= dfii['Cardiology_Revenues'].apply(format)
# dfii['Cardiology_Expenses']= dfii['Cardiology_Expenses'].apply(format)
# dfii['Net_Income_Cardiology']= dfii['Net_Income'].apply(format)

if st.sidebar.checkbox("Click to view : Departmental Income Statement"):
    selecti = st.sidebar.selectbox("Departmental Income Statement",
                                   ['Cardiology', 'Pulmonary', 'GI', 'Endocrinology', 'Neurology', 'ID', 'Nephrology',
                                    'General_Medicine'])
    if selecti == 'Cardiology':
        st.subheader("Cardiology Income Statement")
        fig400 = px.line(dfii, x='Period1', y=['Cardiology_Revenues', 'Cardiology_Expenses', 'Net_Income_Cardiology'])
        st.plotly_chart(fig400)
    elif selecti == 'Pulmonary':
        st.subheader("Pulmonary Income Statement")
        fig401 = px.line(dfii, x='Period1',
                         y=['Endocrinology_Revenues', 'Endocrinology_Expenses', 'Net_Income_Endocrino'])
        st.plotly_chart(fig401)
    elif selecti == 'GI':
        st.subheader("GI Income Statement")
        fig402 = px.line(dfii, x='Period1', y=['GI_Revenues', 'GI_Expenses', 'Net_Income_GI'])
        st.plotly_chart(fig402)
    elif selecti == 'Endocrinology':
        st.subheader("Endocrinology Income Statement")
        fig403 = px.line(dfii, x='Period1',
                         y=['Endocrinology_Revenues', 'Endocrinology_Expenses', 'Net_Income_Endocrino'])
        st.plotly_chart(403)

    elif selecti == 'Neurology':
        st.subheader("Neurology Income Statement")
        fig404 = px.line(dfii, x='Period1', y=['Neurology_Revenues', 'Neurology_Expenses', 'Net_Income_Neurology'])
        st.plotly_chart(fig404)

    elif selecti == 'ID':
        st.subheader("ID Income Statement")
        fig405 = px.line(dfii, x='Period1', y=['ID_Revenues', 'ID_Expenses', 'Net_Income_ID'])
        st.plotly_chart(fig405)
    elif selecti == 'Nephrology':
        st.subheader("Nephrology Income Statement")
        fig406 = px.line(dfii, x='Period1', y=['Nephrology_Revenues', 'Nephrology_Expenses', 'Net_Income_Nephrology'])
        st.plotly_chart(fig406)

    else:
        selecti == 'General_Medicine'
        st.subheader("General_Medicine Income Statement")
        fig407 = px.line(dfii, x='Period1',
                         y=['General_Med_Revenues', 'General_Med_Expenses', 'Net_Income_General_Med'])
        st.plotly_chart(fig407)

















