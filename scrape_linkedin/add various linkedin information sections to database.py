
# @author: sid3345

import os
import json
import mysql.connector
import csv
import re

from date_month import duration

url_file = open(".....path/urls_to_scrape.txt", "r")   
lines = [line.rstrip('\n') for line in url_file]
print("lines:",lines)

for id in lines:
    
    print("id:",id)

    os.system('scrapeli --user={} -o "....path\output_file.json"'.format(id))
    print('scraping ends')

    conn = mysql.connector.connect(host='localhost', user='root', password='', database='db')
    cursor = conn.cursor()

    domain=open('..path/Domain_keywords_to_match_to_job_title_to_count_experience_in_a_particular_domain.csv', 'r', encoding="utf8")

    ''' Database tables: personal_info, linkedin_job, user_education_linkedin, user_skills_linkedin, accomplishments_linkedin, user_interests '''

    output = open("..path/output_file.json", "r", encoding="utf8")

    for line in output:
        #print(line)
        data = json.loads(line)
    #print(data)
    for i in data:
        #print(i)
        
        personal_info=i["personal_info"]
        name=str(personal_info["name"])
        current_company=str(personal_info["company"])
        location=str(personal_info["location"])
        school=str(personal_info["school"])
        summary=str(personal_info["summary"])
        email=str(personal_info["email"]) 
        phone=str(personal_info["phone"])
        if phone.isdigit():
            phone1=int(personal_info)

        else:
            phone1=0    
        website=str(personal_info["websites"])
        followers=str(personal_info["followers"])

        #print(name, location, current_company,school,email,summary,website,location)
        
        query1="INSERT INTO personal_info (name, current_company, location, school, summary, email, phone, website) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val= (name, current_company, location, school, summary, email, phone1, website )
        cursor.execute(query1,val)
        conn.commit()

        experiences=i["experiences"]
        jobs_lis=experiences["jobs"]
        #print(jobs)

        for count1 in range(len(experiences["jobs"])):
            
            jobs=jobs_lis[count1]
            #print(jobs)
            title=jobs["title"]
            #print('title ',type(title))
            company=jobs["company"]
   
            job_date_range=jobs["date_range"]
            job_location=jobs["location"]
            job_description=jobs["description"]

            job_duration=duration(job_date_range)

            reader = csv.reader(domain, delimiter=',')
            #print('title ',title)
            title_list=title.split()
            #print(title_list)
            for title1 in title_list:
                #print('title1 ',title1)
                for row in reader:
                    #print('row ',row)
                    for field in row:
                        #print('field ',field)
                        if field == title1:
                            print (title1, " is in file")

            if job_duration<=6:
                level='beginner'

            elif job_duration>6 and job_duration<=18:
                level='intermediate'

            elif job_duration>18 and job_duration<=36:
                level='advanced'    

            elif job_duration>36 and job_duration<=60:
                level='expert'

            elif job_duration>60:
                level='master'            

            query2="INSERT INTO linkedin_job (name,title,company,job_date_range,job_location,job_description,duration,level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
     
            val= (name,str(title), str(company),str(job_date_range), str(job_location),str(job_description),job_duration,level)
            cursor.execute(query2,val)
            conn.commit()
            
        education_lis=experiences["education"]
        
        for count2 in range(len(experiences["education"])):
            education=education_lis[count2]
   
            college=education["name"]
    
            degree=education["degree"]

            grades=education["grades"]

            field_of_study=education["field_of_study"]

            college_date_range=education["date_range"]

            query3="INSERT INTO user_education_linkedin(name,college,degree,grades,field_of_study,college_date_range) VALUES (%s,%s,%s,%s,%s,%s)"
 
            val= (name,str(college), str(degree),str(grades),str(field_of_study), str(college_date_range),)
            cursor.execute(query3,val)
            conn.commit()

        skills_lis=i["skills"]

        for count3 in range(len(i["skills"])):

            skills=skills_lis[count3]
            skill_name=skills["name"]
            skill_endorsement=skills["endorsements"]

            level=""

            if int(skill_endorsement)<=1:
                level='beginner'

            elif int(skill_endorsement)>1 and int(skill_endorsement)<=4:
                level='intermediate'    

            elif int(skill_endorsement)>4 and int(skill_endorsement)<=8:
                level='advanced'    

            elif int(skill_endorsement)>8:
                level='expert'    

            query4="INSERT INTO user_skills_linkedin (name,skills, skill_endorsements,level) VALUES (%s,%s,%s,%s)"
            val= (name,str(skill_name),skill_endorsement,level)
            cursor.execute(query4,val)
            conn.commit()

        accomplishments=i["accomplishments"] 
        publications_lis=accomplishments["publications"]
        for count4 in range(len(publications_lis)):
            publications=publications_lis[count4]

            query5="INSERT INTO accomplishments_linkedin (name,publications) VALUES (%s,%s)"
            val= (name,str(publications),)
            cursor.execute(query5,val)
            conn.commit()

        certifications_lis=accomplishments["certifications"]
        for count5 in range(len(certifications_lis)):
            certifications=certifications_lis[count5]

            query6="INSERT INTO accomplishments_linkedin (name,certifications) VALUES (%s,%s)"
            val= (name,str(certifications),)
            cursor.execute(query6,val)
            conn.commit()    

        patents_lis=accomplishments["patents"]
        for count6 in range(len(patents_lis)):
            patent_names=patents_lis[count6]

            query7="INSERT INTO accomplishments_linkedin (name,patents) VALUES (%s,%s)"
            val= (name,str(patent_names),)
            cursor.execute(query7,val)
            conn.commit()

        course_lis=accomplishments["courses"]
        for count7 in range(len(course_lis)):
            course_names=course_lis[count7] 

            query8="INSERT INTO accomplishments_linkedin (name,courses) VALUES (%s,%s)"
            val= (name,str(course_names),)
            cursor.execute(query8,val)
            conn.commit()

        project_lis=accomplishments["projects"]
        for count8 in range(len(project_lis)):
            project_names=project_lis[count8]

            query9="INSERT INTO accomplishments_linkedin (name,projects) VALUES (%s,%s)"
            val= (name,str(project_names),)
            cursor.execute(query9,val)
            conn.commit()

        language_lis=accomplishments["languages"]
        for count9 in range(len(language_lis)):
            language_names=language_lis[count9]

            query10="INSERT INTO accomplishments_linkedin (name,languages) VALUES (%s,%s)"
            val= (name,str(language_names),)
            cursor.execute(query10,val)
            conn.commit()        

        test_lis=accomplishments["test_scores"]
        for count10 in range(len(test_lis)):
            test_names=test_lis[count10]  

            query11="INSERT INTO accomplishments_linkedin (name,test_scores) VALUES (%s,%s)"
            val= (name,str(test_names),)
            cursor.execute(query11,val)
            conn.commit()

        interest_lis=i["interests"]
        for count11 in range(len(i["interests"])):

            interest=interest_lis[count11]

            query12="INSERT INTO user_interests_linkedin (name,interests) VALUES (%s,%s)"
            val= (name,str(interest),)
            cursor.execute(query12,val)
            conn.commit()

        output.close()
        print("database storage ends")

url_file.close()    


