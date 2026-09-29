student_ids = ["2410807", "2410724","2410004","2410007","2410012","2410015","2410028",\
               "2410030","2410042","2410052"]
student_names = ["Trần Thị Mai Phương","Phạm Thủy Nguyên","Lã Thanh An","Nguyễn Nhật An"\
,"Trần Hải An","Đặng Nguyên An","Hoàng Đỗ Quỳnh Anh","Hoàng Ngân Anh","Lê Hiền Anh",
"Nguyễn Trần Huyền Anh"]
student_dobs =["6/18/2006","5/20/2006","3/13/2006","4/29/2006","5/29/2006","9/9/2006",\
"3/7/2006","10/28/2006","6/8/2006", "1/2/2006"]

course_ids = ["MAT1.006","ICT2.003","ICT1.001"]
course_names = ["Discrete mathematics","Object-oriented programming","Introduction to Informatics"]

student_marks ={ 
    "MAT1.006": {"2410807": 18.0, "2410724": 13.3, "2410004": 14.2, "2410007": 17.0, "2410012": 18.6, 
                 "2410015": 12.0, "2410028": 12.4, "2410030": 11.2, "2410042": 16.0, "2410052": 11.0},
    "ICT2.003": {"2410807": 13.6, "2410724": 12.1, "2410004": 10.0, "2410007": 11.0, "2410012": 12.0,
                 "2410015": 14.0, "2410028": 13.1, "2410030": 10.1, "2410042": 12.3, "2410052": 18.1},
    "ICT1.001": {"2410807": 12.9, "2410724": 13.2, "2410004": 10.1, "2410007": 12.7, "2410012": 10.3,
                 "2410015": 11.9, "2410028": 16.6, "2410030": 11.9, "2410042": 14.8, "2410052": 17.5}
}

def show_student_marks():
    header_course = "| ".join(course_ids)
    print(f"{'Course ID':<10} | {'Student ID':<30} | {'Dob':<12} |{'Mark':<15} | header_course")

    for i in range(len(student_ids)):
        s_id= student_ids[i]
        name = student_names[i]
        dob = student_dobs[i]

        score_text="" 
        for c_id in course_ids:
            point = student_marks[c_id].get(s_id, "N/A")
            score_text += f"{c_id}: {point} | "
        print(f"{s_id:<10} | {name:<30} | {dob:<12} | {score_text:<8}")

show_student_marks()
