import java.util.Scanner;

public class entero {
    public static void main(String[]args) {
        entraNumero();


    }

    public static void entraNumero(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        int a = sc.nextInt();
        int b = a * 10;
        System.out.println("Su número * 10 = " + b);
        sc.close();
    }
}
