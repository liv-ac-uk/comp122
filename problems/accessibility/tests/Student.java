public class Student {
    // Replace the question marks with working code
    private boolean[] hasSubmitted = {false, false, false};
    private int[] finalGrades = {0, 0, 0};

    public boolean[] getHasSubmitted() {
        return hasSubmitted;
    }

    public int[] getGrades() {
        return finalGrades;
    }

    public int getTotalGrade() {
           int total = 0;
           for (int i=0;i<finalGrades.length;i++) {
               total += finalGrades[i];
           }
         return total;
    }

    public void updateGrade(int assignment, int grade) {
         // ensure a valid index has been inputted by the user

        if (assignment < 0 || assignment > 3) {
            System.out.println("Enter an assignment number from 0-2");
            return;
        }

        // ensure a valid grade has been entered
        if (grade < 0 || grade > 30) {
            System.out.println("Enter a grade from 0-30");
            return;
        }

        // Update grade
        hasSubmitted[assignment] = true;
        finalGrades[assignment] = grade;

        return;
     }
}
