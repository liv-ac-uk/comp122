public class Student {
    private String name;
    private String email;
    private int yearOfBirth;

    private int enrolmentYear;
    private int studentId;

    public Student() {

    }

    public Student(String studentName) {
        name = studentName;
    }

    // Change this constructor to take in more parameters
    // public Student(?) {
    //     name = studentName;
    //     ?
    // }

    // Add a new constructor below to take in fewer parameters
    // public Student(?) {
    //     name = studentName;
    //     ?
    // }

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
