import java.util.Scanner;

public class rec_reverse {
    public static String rreverse(String s) {
        if (s.equals("")) {
            return s;
        } else {
            return rreverse(s.substring(1)) + s.charAt(0);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter paragraph: ");
        String s = input.nextLine();
        String[] words = s.split(" ");
        for (String word : words) {
            System.out.print(rreverse(word) + " ");
        }
    }
}
