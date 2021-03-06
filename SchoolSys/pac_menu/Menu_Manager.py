#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pac_menu import Enum_Meun, Enum_School_Menu, Enum_Class_Menu, Enum_Student_Menu, Enum_Subject_Menu, Enum_Teacher_Menu
from pac_school import School, School_Manager
from pac_class import Class, Class_Manager
from pac_student import Student, Student_Manager
from pac_teacher import Teacher, Teacher_Manager
from pac_subject import Subject, Subject_Manager
class Menu:
    __slots__ = ('summary_menu', 'school_management_menu',
                 'class_management_menu', 'student_management_menu',
                 'subject_management_menu', 'teacher_management_menu',
                 '__objSchoolData','__objTeacherData','__objClassData',
                 '__objStudentData','__objSubjectData')

    def __init__(self):
        self.__objSchoolData = School_Manager.School_Manager()
        self.__objTeacherData = Teacher_Manager.Teacher_Manager()
        self.__objClassData = Class_Manager.Class_Manager()
        self.__objStudentData = Student_Manager.Student_Manager()
        self.__objSubjectData = Subject_Manager.Subject_Manager()

    def show_summary_menu(self):
        '显示总的系统菜单'
        print("*************************************")
        print("*    欢迎使用python版本教务管理系统     *")
        print("*  请根据菜单选择对应的模块进行系统管理   *")
        print("*     1.学校综合信息管理               *")
        print("*     2.班级管理                      *")
        print("*     3.学生管理                      *")
        print("*     4.课程管理                      *")
        print("*     5.教师管理                      *")
        print("*************************************")

    def select_summary_menu(self):
        '让用户对总的系统菜单进行选择'
        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input),int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_summary_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 5:
            print("请输入1〜5之间的书记进行菜单的选择")
            self.select_summary_menu()
            return
        if temp_menu == Enum_Meun.Enum_Summary_Menu.school_management.value:
            self.summary_menu = Enum_Meun.Enum_Summary_Menu.school_management
        elif temp_menu == Enum_Meun.Enum_Summary_Menu.class_management.value:
            self.summary_menu = Enum_Meun.Enum_Summary_Menu.class_management
        elif temp_menu == Enum_Meun.Enum_Summary_Menu.student_management.value:
            self.summary_menu = Enum_Meun.Enum_Summary_Menu.student_management
        elif temp_menu == Enum_Meun.Enum_Summary_Menu.subject_management.value:
            self.summary_menu = Enum_Meun.Enum_Summary_Menu.subject_management
        elif temp_menu == Enum_Meun.Enum_Summary_Menu.teacher_management.value:
            self.summary_menu = Enum_Meun.Enum_Summary_Menu.teacher_management


    def get_summary_menu(self):
        '返回当前用户选择的菜单'
        return self.summary_menu

    def show_sbu_menu(self, summary_menu):
        if summary_menu == Enum_Meun.Enum_Summary_Menu.school_management:
            self.show_school_menu()
        elif summary_menu == Enum_Meun.Enum_Summary_Menu.class_management:
            self.show_class_menu()
        elif summary_menu == Enum_Meun.Enum_Summary_Menu.student_management:
            self.show_student_menu()
        elif summary_menu == Enum_Meun.Enum_Summary_Menu.subject_management:
            self.show_subject_menu()
        elif summary_menu == Enum_Meun.Enum_Summary_Menu.teacher_management:
            self.show_teacher_menu()

    def show_school_menu(self):
        '显示总的系统菜单'
        print("*************************************")
        print("*     欢迎使用进入校园综合管理菜单       ")
        print("*     1.添加学校信息                  ")
        print("*     2.编辑学校信息                  ")
        print("*     3.查看学校信息                  ")
        print("*     4.删除学校信息                  ")
        print("*     5.从文件导入学校信息             ")
        print("*     6.保存学校信息到文件             ")
        print("*     7.退回上一层菜单                 ")
        print("*************************************")
        self.select_school_menu()

    def select_school_menu(self):
        '让用户对校园管理菜单进行选择'
        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input), int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_school_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 7:
            print("请输入1〜7之间的数字进行菜单的选择")
            self.select_school_menu()
            return
        if temp_menu == Enum_School_Menu.School_Menu.add_school.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.add_school
            self.add_school()
            self.show_school_menu()
        elif temp_menu == Enum_School_Menu.School_Menu.edit_school.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.edit_school
            self.edit_school()
            self.show_school_menu()
        elif temp_menu == Enum_School_Menu.School_Menu.show_school.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.show_school
            self.show_school()
            self.show_school_menu()
        elif temp_menu == Enum_School_Menu.School_Menu.delete_school.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.delete_school
            self.delete_school()
        elif temp_menu == Enum_School_Menu.School_Menu.save_school_file.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.save_school_file
            self.save_school_to_file()
        elif temp_menu == Enum_School_Menu.School_Menu.import_school_file.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.import_school_file
            self.import_school_file()
        elif temp_menu == Enum_School_Menu.School_Menu.return_back.value:
            self.school_management_menu = Enum_School_Menu.School_Menu.return_back
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)

    '添加学校信息'
    def add_school(self):
        print("********************************")
        print("欢迎进入学校录入界面")
        code = input("请输入学校代码:")
        name = input("请输入学校名称:")
        address = input("请输入学校地址:")

        save = input("学校信息录入完毕，是否存入内存数据库？y/n")
        if save.upper() == "Y":
            objSchool = School.School()
            objSchool.code = code
            objSchool.name = name
            objSchool.address = address
            if self.__objSchoolData.is_exist(code) == True:
                print("您输入的学校代码已经存在，请重新输入！")
                self.add_school()
            else:
                self.__objSchoolData.add_school(objSchool)
                print("恭喜您，学校信息已保存到内存数据库！")
                print("您输入的学校信息如下：")
                print("学校代码：" + code)
                print("学校名称：" + name)
                print("学校地址：" + address)


        self.show_school_menu()

    '编辑学校信息'
    def edit_school(self):
        code = input("请输入你要编辑的学校代码:")
        if self.__objSchoolData.is_exist(code) == False:
            print("您输入的学校不存在，请从新输入！")
            self.edit_school()
        else:
            print("您即将为学校代码为：" + code + "的学校进行信息的编辑")
            name = input("请输入您要更改的学校名称：")
            address = input("请输入您要更改的学校地址")
            obj = self.__objSchoolData.get_school_by_code(code)
            obj.name = name
            obj.address = address
            self.__objSchoolData.edit_school(code, obj)
            print("学校信息更新完毕！")

    '查看学校信息'
    def show_school(self):
        int_menu = input("请输入菜单查看学校信息：1表示查看全部学校的信息；2表示根据学校代码查看指定学校信息:")
        if int_menu == '1':
            self.__objSchoolData.show_all_school()
        elif int_menu == '2':
            school_code = input("请输入学校代码：")
            self.__objSchoolData.show_school(school_code)


    def delete_school(self):
        code = input("请输入您要删除的学校代码：")
        if self.__objSchoolData.search_school(code) == False:
            print("您输入的学校代码不存在！")
        else:
            self.__objSchoolData.delete_school(code)
        self.select_school_menu()


    '用户选择保存内存数据到文件'
    def save_school_to_file(self):
        if self.__objSchoolData.is_empty() == True:
            print("您还没有录入学校信息，请先录入或者导入学校信息！")
            self.select_school_menu()
        else:
            self.__objSchoolData.save_school_to_file()
            print("学校数据已经保存到school.txt文件！")
        self.show_school_menu()

    '用户选择了从文件导入学校数据'
    def import_school_file(self):
        result = self.__objSchoolData.import_from_file()
        if result == False:
            print("系统中还没有学校数据存储在文件中，请先录入学校数据！")
        else:
            print("学校数据导入成功，数据如下：")
            # self.__objSchoolData.set_data(result)
            self.__objSchoolData.show_all_school()
        self.show_school_menu()


    '显示班级菜单'
    def show_class_menu(self):

        print("*************************************")
        print("*     欢迎进入班级管理菜单             *")
        print("*     1.添加班级信息                  *")
        print("*     2.编辑班级信息                  *")
        print("*     3.查看班级信息                  *")
        print("*     4.删除班级信息                  *")
        print("*     5.退回上一层菜单                *")
        print("*************************************")
        self.select_class_menu()

    '让用户对班级管理菜单进行选择'
    def select_class_menu(self):

        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input), int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_class_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 5:
            print("请输入1〜5之间的书记进行菜单的选择")
            self.select_class_menu()
            return
        if temp_menu == Enum_Class_Menu.Class_Menu.add_class.value:
            self.class_management_menu = Enum_Class_Menu.Class_Menu.add_class
            self.add_class()
            self.show_class_menu()
        elif temp_menu == Enum_Class_Menu.Class_Menu.edit_class.value:
            self.class_management_menu = Enum_Class_Menu.Class_Menu.edit_class
            self.edit_class()
            self.show_class_menu()
        elif temp_menu == Enum_Class_Menu.Class_Menu.show_class.value:
            self.class_management_menu = Enum_Class_Menu.Class_Menu.show_class
            self.show_class()
            self.show_class_menu()
        elif temp_menu == Enum_Class_Menu.Class_Menu.delete_class.value:
            self.class_management_menu = Enum_Class_Menu.Class_Menu.return_back.delete_class
            self.delete_class()
            self.show_class_menu()
        elif temp_menu == Enum_Class_Menu.Class_Menu.return_back.value:
            self.class_management_menu = Enum_Class_Menu.Class_Menu.return_back
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)


    '添加班级信息'
    def add_class(self):
        if self.__objSchoolData.is_empty() == True:
            print("系统还没有录入学校信息，请先录入学校信息，再录入班级信息！")
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)
        else:
            self.__objSchoolData.show_all_school()
            school_code = input("请输入班级所属学校代码：")
            class_code = input("请输入班级代码：")
            name = input("请输入班级名称：")
            address = input("请输入班级地址：")
            '初始化一个班级对象，用于接收用户的输入'
            obj_class = Class.Class()
            obj_class.name = name
            obj_class.code = class_code
            obj_class.school_code = school_code
            obj_class.address = address
            '根据用户输入的学校代码，获取对应的学校实例'
            obj_school = self.__objSchoolData.search_school(school_code)
            '把班级对象实例添加到对应的学校实例数据库'
            obj_school.add_class(obj_class)
            '更新添加了班级信息的学校数据到学校列表数据库'
            self.__objSchoolData.edit_school(school_code, obj_school)
        self.__objSchoolData.show_all_school()
        school_code = input("请输入班级所属学校代码：")
        class_code = input("请输入班级代码：")
        name = input("请输入班级名称：")
        address = input("请输入班级地址：")
        '初始化一个班级对象，用于接收用户的输入'
        obj_class = Class.Class()
        obj_class.name = name
        obj_class.code = class_code
        obj_class.school_code = school_code
        obj_class.address = address
        '根据用户输入的学校代码，获取对应的学校实例'
        obj_school = self.__objSchoolData.search_school(school_code)
        '把班级对象实例添加到对应的学校实例数据库'
        obj_school.add_class(obj_class)
        '更新添加了班级信息的学校数据到学校列表数据库'
        self.__objSchoolData.edit_school(school_code, obj_school)

    def edit_class(self):
        if self.__objSchoolData.is_empty() == True:
            print("系统还没有录入学校信息，请先录入学校信息，再录入班级信息！")
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)
        else:
            if self.__objSchoolData.is_empty() == False:
                self.__objSchoolData.show_all_school()
                school_code = input("请输入班级所属学校代码：")
                school = self.__objSchoolData.search_school(school_code)
                school.show_all_class()
                class_code = input("请输入班级代码：")
                obj_class = school.search_class(class_code)
                name = input("请输入班级名称：")
                address = input("请输入班级地址")
                obj_class.name = name
                obj_class.address = address
                school.edit_school(class_code,obj_class)

    '显示班级信息'
    def show_class(self):
        if self.__objSchoolData.is_empty() == True:
            print("系统还没有录入学校信息，请先录入学校信息，再录入班级信息！")
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)
        else:
            self.__objSchoolData.show_all_school()
            school_code = input("请输入班级所属学校代码：")
            school = self.__objSchoolData.search_school(school_code)
            school.show_all_class()

    '删除班级信息'
    def delete_class(self):
        if self.__objSchoolData.is_empty() == True:
            print("系统还没有录入学校信息，无法进行班级的删除操作!")
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)
        else:
            self.__objSchoolData.show_all_school()
            school_code = input("请输入班级所属学校代码：")
            school = self.__objSchoolData.search_school(school_code)
            school.show_all_class()
            class_code = input("请输入你想删除的班级代码：")
            if school.is_exist(class_code) == True:
                school.delete_class(class_code)
            else:
                '进行班级代码不存在情况下的处理操作'
                print("你输入的班级代码不存在，请重新输入！")
                pass



#TODO 学生

    def show_student_menu(self):
        '显示总的系统菜单'
        print("*************************************")
        print("*     欢迎使用进入校园综合管理菜单       ")
        print("*     1.添加学生信息                  ")
        print("*     2.编辑学生信息                  ")
        print("*     3.查看学生信息                  ")
        print("*     4.删除学生信息                  ")
        print("*     5.退回上一层菜单                 ")
        print("*************************************")
        self.select_student_menu()

    def select_student_menu(self):

        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input), int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_student_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 5:
            print("请输入1〜5之间的书记进行菜单的选择")
            self.select_student_menu()
            return
        if temp_menu == Enum_Student_Menu.Student_Menu.add_student.value:
            self.student_management_menu = Enum_Student_Menu.Student_Menu.add_student
            self.add_student()
            self.show_student_menu()
        elif temp_menu == Enum_Student_Menu.Student_Menu.edit_student.value:
            self.student_management_menu = Enum_Student_Menu.Student_Menu.edit_student
            self.edit_student()
            self.show_student_menu()
        elif temp_menu == Enum_Student_Menu.Student_Menu.show_student.value:
            self.student_management_menu = Enum_Student_Menu.Student_Menu.show_student
            self.show_student()
            self.show_student_menu()
        elif temp_menu == Enum_Student_Menu.Student_Menu.delete_student.value:
            self.student_management_menu = Enum_Student_Menu.Student_Menu.return_back.delete_student
            self.delete_student()
            self.show_student_menu()
        elif temp_menu == Enum_Student_Menu.Student_Menu.return_back.value:
            self.student_management_menu = Enum_Student_Menu.Student_Menu.return_back
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)

    '添加学生信息'
    def add_student(self):
        print("********************************")
        print("欢迎进入学生录入界面")
        code = input("请输入学生代码:")
        name = input("请输入学生名称:")
        sex = input("请输入学生性别:")
        age = input("请输入学生年龄:")
        class_code = input("请输入学生班级代码:")
        school_code = input("请输入学生学校代码:")

        save = input("学生信息录入完毕，是否存入内存数据库？y/n")
        if save.upper() == "Y":
            objStudent = Student.Student()
            objStudent.code = code
            objStudent.name = name
            objStudent.sex = sex
            objStudent.age = age
            objStudent.class_code = class_code
            objStudent.school_code = school_code
            if self.__objStudentData.is_exist(code) == True:
                print("您输入的学生代码已经存在，请重新输入！")
                self.add_student()
            else:
                self.__objStudentData.add_student(objStudent)
                print("恭喜您，学生信息已保存到内存数据库！")
                print("您输入的学生信息如下：")
                print("学生代码：" + code)
                print("学生名称：" + name)
                print("学生性别：" + sex)
                print("学生年龄：" + age)
                print("学生班级代码：" + class_code)
                print("学生学校代码：" + school_code)


        self.show_student_menu()

    '编辑学生信息'
    def edit_student(self):
        code = input("请输入你要编辑的学生代码:")
        if self.__objStudentData.is_exist(code) == False:
            print("您输入的学生不存在，请从新输入！")
            self.edit_student()
        else:
            print("您即将为学生代码为：" + code + "的学生进行信息的编辑")
            name = input("请输入您要更改的学生名称：")
            sex = input("请输入学生性别:")
            age = input("请输入学生年龄:")
            class_code = input("请输入学生班级代码:")
            obj = self.__objStudentData.get_student_by_code(code)
            obj.name = name
            obj.sex = sex
            obj.age = age
            obj.class_code = class_code
            self.__objStudentData.edit_student(code, obj)
            print("学生信息更新完毕！")

    '查看学生信息'
    def show_student(self):
        int_menu = input("请输入菜单查看学生信息：1表示查看全部学生的信息；2表示根据学生代码查看指定学生信息:")
        if int_menu == '1':
            self.__objStudentData.show_all_student()
        elif int_menu == '2':
            student_code = input("请输入学生代码：")
            self.__objStudentData.show_student(student_code)


    def delete_student(self):
        code = input("请输入您要删除的学生代码：")
        if self.__objStudentData.search_student(code) == False:
            print("您输入的学生代码不存在！")
        else:
            self.__objStudentData.delete_student(code)
        self.select_student_menu()

#TODO 教师

    def show_teacher_menu(self):
        '显示总的系统菜单'
        print("*************************************")
        print("*     欢迎使用进入校园综合管理菜单       ")
        print("*     1.添加教师信息                  ")
        print("*     2.编辑教师信息                  ")
        print("*     3.查看教师信息                  ")
        print("*     4.删除教师信息                  ")
        print("*     5.退回上一层菜单                 ")
        print("*************************************")
        self.select_teacher_menu()

    def select_teacher_menu(self):

        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input), int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_teacher_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 5:
            print("请输入1〜5之间的书记进行菜单的选择")
            self.select_teacher_menu()
            return
        if temp_menu == Enum_Teacher_Menu.Teacher_Menu.add_teacher.value:
            self.teacher_management_menu = Enum_Teacher_Menu.Teacher_Menu.add_teacher
            self.add_teacher()
            self.show_teacher_menu()
        elif temp_menu == Enum_Teacher_Menu.Teacher_Menu.edit_teacher.value:
            self.teacher_management_menu = Enum_Teacher_Menu.Teacher_Menu.edit_teacher
            self.edit_teacher()
            self.show_teacher_menu()
        elif temp_menu == Enum_Teacher_Menu.Teacher_Menu.show_teacher.value:
            self.teacher_management_menu = Enum_Teacher_Menu.Teacher_Menu.show_teacher
            self.show_teacher()
            self.show_teacher_menu()
        elif temp_menu == Enum_Teacher_Menu.Teacher_Menu.delete_teacher.value:
            self.teacher_management_menu = Enum_Teacher_Menu.Teacher_Menu.return_back.delete_teacher
            self.delete_teacher()
            self.show_teacher_menu()
        elif temp_menu == Enum_Teacher_Menu.Teacher_Menu.return_back.value:
            self.teacher_management_menu = Enum_Teacher_Menu.Teacher_Menu.return_back
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)


    '添加教师信息'
    def add_teacher(self):
        print("********************************")
        print("欢迎进入教师录入界面")
        code = input("请输入教师代码:")
        name = input("请输入教师名称:")
        school_code = input("请输入教师所在学校代码:")
        

        save = input("教师信息录入完毕，是否存入内存数据库？y/n")
        if save.upper() == "Y":
            objTeacher = Teacher.Teacher()
            objTeacher.code = code
            objTeacher.name = name
            objTeacher.school_code = school_code
            if self.__objTeacherData.is_exist(code) == True:
                print("您输入的教师代码已经存在，请重新输入！")
                self.add_teacher()
            else:
                self.__objTeacherData.add_teacher(objTeacher)
                print("恭喜您，教师信息已保存到内存数据库！")
                print("您输入的教师信息如下：")
                print("教师代码：" + code)
                print("教师名称：" + name)
                print("教师所在学校代码：" + school_code)


        self.show_teacher_menu()

    '编辑教师信息'
    def edit_teacher(self):
        code = input("请输入你要编辑的教师代码:")
        if self.__objTeacherData.is_exist(code) == False:
            print("您输入的教师不存在，请从新输入！")
            self.edit_teacher()
        else:
            print("您即将为教师代码为：" + code + "的教师进行信息的编辑")
            name = input("请输入您要更改的教师名称：")
            school_code = input("请输入教师所在学校代码:")
            obj = self.__objTeacherData.get_teacher_by_code(code)
            obj.name = name
            obj.school_code = school_code
            self.__objTeacherData.edit_teacher(code, obj)
            print("教师信息更新完毕！")

    '查看教师信息'
    def show_teacher(self):
        int_menu = input("请输入菜单查看教师信息：1表示查看全部教师的信息；2表示根据教师代码查看指定教师信息:")
        if int_menu == '1':
            self.__objTeacherData.show_all_teacher()
        elif int_menu == '2':
            teacher_code = input("请输入教师代码：")
            self.__objTeacherData.show_teacher(teacher_code)


    def delete_teacher(self):
        code = input("请输入您要删除的教师代码：")
        if self.__objTeacherData.search_teacher(code) == False:
            print("您输入的教师代码不存在！")
        else:
            self.__objTeacherData.delete_teacher(code)
        self.select_teacher_menu()


#TODO 课程

    def show_subject_menu(self):
        '显示总的系统菜单'
        print("*************************************")
        print("*     欢迎使用进入校园综合管理菜单       ")
        print("*     1.添加课程信息                  ")
        print("*     2.编辑课程信息                  ")
        print("*     3.查看课程信息                  ")
        print("*     4.删除课程信息                  ")
        print("*     5.退回上一层菜单                 ")
        print("*************************************")
        self.select_subject_menu()



    def select_subject_menu(self):

        user_input = input('请输入菜单序号:')
        if isinstance(eval(user_input), int) == False:
            print("请重新输入数字进行菜单的选择!")
            self.select_subject_menu()
            return

        temp_menu = eval(user_input)
        if int(temp_menu) <= 0 or int(temp_menu) > 5:
            print("请输入1〜5之间的书记进行菜单的选择")
            self.select_subject_menu()
            return
        if temp_menu == Enum_Subject_Menu.Subject_Menu.add_subject.value:
            self.subject_management_menu = Enum_Subject_Menu.Subject_Menu.add_subject
            self.add_subject()
            self.show_subject_menu()
        elif temp_menu == Enum_Subject_Menu.Subject_Menu.edit_subject.value:
            self.subject_management_menu = Enum_Subject_Menu.Subject_Menu.edit_subject
            self.edit_subject()
            self.show_subject_menu()
        elif temp_menu == Enum_Subject_Menu.Subject_Menu.show_subject.value:
            self.subject_management_menu = Enum_Subject_Menu.Subject_Menu.show_subject
            self.show_subject()
            self.show_subject_menu()
        elif temp_menu == Enum_Subject_Menu.Subject_Menu.delete_subject.value:
            self.subject_management_menu = Enum_Subject_Menu.Subject_Menu.return_back.delete_subject
            self.delete_subject()
            self.show_subject_menu()
        elif temp_menu == Enum_Subject_Menu.Subject_Menu.return_back.value:
            self.subject_management_menu = Enum_Subject_Menu.Subject_Menu.return_back
            self.show_summary_menu()
            self.select_summary_menu()
            summary_menu = self.get_summary_menu()
            '根据用户的选择，显示对应的子菜单'
            self.show_sbu_menu(summary_menu)

    '添加课程信息'
    def add_subject(self):
        print("********************************")
        print("欢迎进入课程录入界面")
        code = input("请输入课程代码:")
        name = input("请输入课程名称:")

        save = input("课程信息录入完毕，是否存入内存数据库？y/n")
        if save.upper() == "Y":
            objSubject = Subject.Subject()
            objSubject.code = code
            objSubject.name = name
            if self.__objSubjectData.is_exist(code) == True:
                print("您输入的课程代码已经存在，请重新输入！")
                self.add_subject()
            else:
                self.__objSubjectData.add_subject(objSubject)
                print("恭喜您，课程信息已保存到内存数据库！")
                print("您输入的课程信息如下：")
                print("课程代码：" + code)
                print("课程名称：" + name)


        self.show_subject_menu()

    '编辑课程信息'
    def edit_subject(self):
        code = input("请输入你要编辑的课程代码:")
        if self.__objSubjectData.is_exist(code) == False:
            print("您输入的课程不存在，请从新输入！")
            self.edit_subject()
        else:
            print("您即将为课程代码为：" + code + "的课程进行信息的编辑")
            name = input("请输入您要更改的课程名称：")
            obj = self.__objSubjectData.get_subject_by_code(code)
            obj.name = name
            self.__objSubjectData.edit_subject(code, obj)
            print("课程信息更新完毕！")

    '查看课程信息'
    def show_subject(self):
        int_menu = input("请输入菜单查看课程信息：1表示查看全部课程的信息；2表示根据课程代码查看指定课程信息:")
        if int_menu == '1':
            self.__objSubjectData.show_all_subject()
        elif int_menu == '2':
            subject_code = input("请输入课程代码：")
            self.__objSubjectData.show_subject(subject_code)


    def delete_subject(self):
        code = input("请输入您要删除的课程代码：")
        if self.__objSubjectData.search_subject(code) == False:
            print("您输入的课程代码不存在！")
        else:
            self.__objSubjectData.delete_subject(code)
        self.select_subject_menu()



















