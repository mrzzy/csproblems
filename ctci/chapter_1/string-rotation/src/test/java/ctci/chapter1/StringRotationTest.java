package ctci.chapter1;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

/** Cracking the Coding Interview Chapter 1 String Rotation solution unit tests. */
public class StringRotationTest {
  private final StringRotation subject = new StringRotation();

  @Test
  public void shouldHandleSpecialCases() {
    assertFalse(subject.isRotation("", ""));
    assertTrue(subject.isRotation("a", "a"));
    assertFalse(subject.isRotation("abc", "ab"));
  }

  @Test
  public void shouldDetectRotations() {
    assertTrue(subject.isRotation("erbottlewat", "waterbottle"));
    assertTrue(subject.isRotation("test", "estt"));
    assertTrue(subject.isRotation("apple", "pleap"));
  }
}
