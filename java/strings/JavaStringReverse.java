import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {     
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        System.out.println(isPalindrome(A));
    }
    
    public static String isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return "No";
            }
        }
        return "Yes";
    }
}


