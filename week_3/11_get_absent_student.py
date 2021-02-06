all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# for all_student in all_students: O(N^2) 의 복잡도
#     for present_student in present_students:

def get_absent_student(all_array, present_array): # 시간복잡도를 낮추지만 공간을 대신 사용하는 자료구조
    student_dict = {}
    for key in all_array:# 공간복잡도도 O(N^2)만큼 걸린다
        student_dict[key] = True#(True자리에 아무값이나 넣어도 댐 그냥 키를 이용해서 저장하고 삭제한 것이기 때문, 그냥 키의 값임)
    for key in present_array:
        del student_dict[key]
    for key in student_dict.keys():
        return key


print(get_absent_student(all_students, present_students))