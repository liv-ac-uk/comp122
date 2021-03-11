public class Person {
    private String name;
    private String email;

    public String greet() {
        return "sendto: " + email + "Hi " + name + ",\n";
    }

    public void setName(String new_name) {
        name = new_name;
    }

    public String getName() {
        return name;
    }

    public void setEmail(String new_email) {
        email = new_email;
    }

    public String getEmail() {
        return email;
    }
}
