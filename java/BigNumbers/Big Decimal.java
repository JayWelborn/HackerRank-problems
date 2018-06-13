import java.math.BigDecimal;
import java.util.*;
class Solution{
    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();
        
                //Write your code here
        int swaps;
        BigDecimal b1, b2;
        do {
            swaps = 0;
            for (int i = 0; i < n - 1; i++) {
                b1 = new BigDecimal(s[i]);
                b2 = new BigDecimal(s[i+1]);
                if (b1.compareTo(b2) < 0) {
                    String temp = s[i];
                    s[i] = s[i+1];
                    s[i+1] = temp;
                    swaps++;
                }
            }
        } while (swaps != 0);
        
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}
