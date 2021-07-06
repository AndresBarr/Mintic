import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class holamundo {

    public static void main(String[] args) throws IOException {
        holaMundo();
        datoBuffer();
        datoBuffertry();
        dataScan();
    }


    public static void holaMundo()  {
        var hola = "Hola mundo";
        System.out.println("Mi primer " + hola);
    }   

    public static void datoBuffer() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Por favor ingrese su nombre");
        String nombre = br.readLine();
        System.out.println( "Hola " + nombre);
        //br.close();
    }

    public static void datoBuffertry()  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Por favor ingrese su nombre");
        String nombre = null;
        try {
            nombre = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println( "Hola " + nombre);
    }

    public static void dataScan()   {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese su nombre");
        String nombre2 = sc.nextLine();
        System.out.println("Su nombre es: "+ nombre2);
        sc.close();
    }
}