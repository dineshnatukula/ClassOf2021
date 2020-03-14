import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int i = 0; i < t; i++) {
            int l = scan.nextInt();
            int n = scan.nextInt();
            int half = l/2;
            int m1 = 0, m2 = 0;
            for (int j = 0; j < n; j++) {
                int distAnt = scan.nextInt();
                if (distAnt < half) {
                    if (m1 < distAnt) {
                        m1 = distAnt;
                    }
                    if (m2 < (l - distAnt)) {
                        m2 = (l - distAnt);
                    }
                } else {
                    if (m1 < (l - distAnt)) {
                        m1 = (l - distAnt);
                    }
                    if (m2 < distAnt) {
                        m2 = distAnt;
                    }
                }
            }
            System.out.println(m1 + " " + m2);
        }
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}