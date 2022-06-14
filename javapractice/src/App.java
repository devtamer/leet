import java.util.Scanner;
import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Enter the number of dice: ");
        Scanner input = new Scanner(System.in);
        int numofDice = input.nextInt();
        System.out.println("The number of dice you have is: " + numofDice);

        Random rand = new Random();
        int randNum = 0;
        int total = 0;
        for (int i = 0; i < numofDice; i++) {
            randNum = rand.nextInt(6) + 1;
        }

    }
}
