# Here we do only project practice
 
# 1.student result system (10-05-2026)
name=str(input("Enter your name: "));
rollno=int(input("Enter your roll number: "));
# ask for name and roll number
print("Name: ",name);
print("Roll No: ",rollno);
# mark entering
print("enter the marks of these subjects: ");
maths=int(input("Maths: "));
english=int(input("English: "));
science=int(input("Science: "));
computer=int(input("Computer: "));
hindi=int(input("Hindi: "));
# print the marks
print("maths: ",maths);
print("english: ",english);
print("science: ",science);
print("computer: ",computer);
print("hindi: ",hindi);
# calculate total marks
total=maths+english+science+computer+hindi;
#print tolal marks
print("Total Marks: ",total);
# calculate percentage
percentage=(total/500)*100;
#print percentage
print("Percentage: ",percentage,"%");
# calculate grade
if percentage>=90:
    grade="A+" ; 
elif percentage>=80:
    grade="A";  
elif percentage>=70:
    grade="B";
elif percentage>=60:
    grade="C";
elif percentage>=33:
    grade="D";
else:
    grade="F";
#print grade
print("Grade: ",grade);
# result
if grade=="F":
    print("Result: Fail");
else:
    print("Result: Pass");


# updated student result system with more features(31-05-2026)
class student:
    def __init__(self,name,rollno,maths,english,science,computer,hindi):
        self.name=name;
        self.rollno=rollno;
        self.maths=maths;
        self.english=english;
        self.science=science;
        self.computer=computer;
        self.hindi=hindi;
    def total_marks(self):
        return self.maths+self.english+self.science+self.computer+self.hindi;
    def percentage(self):
        return (self.total_marks()/500)*100;
    def grade(self):
        if self.percentage()>=90:
            return "A+" ; 
        elif self.percentage()>=80:
            return "A";  
        elif self.percentage()>=70:
            return "B";
        elif self.percentage()>=60:
            return "C";
        elif self.percentage()>=33:
            return "D";
        else:
            return "F";
    def result(self):
        if self.grade()=="F":
            return "Fail";
        else:
            return "Pass";
# create student object
s1=student("John",1,85,90,80,95,88);
# print student details
print("Name: ",s1.name);
print("Roll No: ",s1.rollno);
print("Total Marks: ",s1.total_marks());
print("Percentage: ",s1.percentage(),"%");
print("Grade: ",s1.grade());
print("Result: ",s1.result());


# updated student result sysystem with more feature






