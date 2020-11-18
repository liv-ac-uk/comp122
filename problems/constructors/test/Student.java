public class Student {
    private String name;
    private String email;
    private int yearOfBirth;

    private int enrolmentYear;
    private int studentId;

    public Student() {

    }


    // Change this method to take in more parameters
    // public Student(String studentName) {
    //     name = studentName;
    // }


    public Student(String studentName, String new_email, int new_dob, int stud_enrolmentYear, int new_studentId) {
        name= studentName;
        email=new_email;
        yearOfBirth=new_dob;

        enrolmentYear=stud_enrolmentYear;
        studentId=new_studentId;
    }

    public Student(String studentName, String new_email, int new_dob) {
        name= studentName;
        email=new_email;
        yearOfBirth=new_dob;

    }

    public Student(String studentName, String new_email, String new_dob) {
        name= studentName;
        email=new_email;
        yearOfBirth=Integer.parseInt(new_dob.split("/")[2]);
    }

    public void setName(String studentName) {
        name = studentName;
    }

    public void setEmail(String emailAddress) {
        email = emailAddress;
    }

    public void setYearOfBirth(int year) {
        yearOfBirth = year;
    }

    public void setEnrolmentYear(int year) {
        enrolmentYear = year;
    }

    public void setStudentId(int id) {
        studentId = id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public int getYearOfBirth() {
        return yearOfBirth;
    }

    public int getEnrolmentYear() {
        return enrolmentYear;
    }

    public int getStudentId() {
        return studentId;
    }
}
