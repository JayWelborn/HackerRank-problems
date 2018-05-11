import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        ArrayList<String> tokens = new ArrayList<String>(Arrays.asList(s.split("[\\s+!,?._'@]")));
        tokens.removeAll(Arrays.asList(""));
        System.out.println(tokens.size());
        for(String token : tokens) {
            System.out.println(token);
        }
        scan.close();
    }
}
