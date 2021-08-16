import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;


import java.lang.reflect.*;
import org.junit.jupiter.api.Test;

public class HierarchyTest {
    public static boolean classIsParent(String parent, String child) {
      // if parent is a super class of child returns true,
      // otherwise false
      try {
          return Class.forName(parent).isAssignableFrom(Class.forName(child));
      } catch (Exception e) {
          return false;
      }
  }

  @Test
  public void sandwichIsItem(){
      String parent = "Item";
      String child = "Sandwich";
      if (!classIsParent(parent, child)) {
          fail(child + " is not a subclass of " + parent);
      }
  }
  
  @Test
  public void snackIsItem(){
      String parent = "Item";
      String child = "Snack";
      if (!classIsParent(parent, child)) {
          fail(child + " is not a subclass of " + parent);
      }
  }
  
  @Test
  public void drinkIsItem(){
      String parent = "Item";
      String child = "Drink";
      if (!classIsParent(parent, child)) {
          fail(child + " is not a subclass of " + parent);
      }
  }

    
}
