import java.util.Scanner;

public class Ejercicios {

    public static void main(String[] args) {

    //elsaludo();
    //preguntaEntero();
    //duploTriple();
    //aFahrenheit();
    //parImpar();

    }

    public static void elsaludo() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor ingrese el nombre: ");
        var nombre = sc.nextLine();
        var resultado = saludo(nombre);
        System.out.println(resultado);
        
    }    
    
    public static String saludo (String nombre) {
        return "Hola" + nombre + "!";
    }

    public static void preguntaEntero() {
        var sc = new Scanner(System.in);
        System.out.println("Introduzca un número de dos o más cifras: ");
        var numero = sc.nextInt();
        var digitos = numeroDigitos (numero);
        System.out.println( "El número digitado tiene " + digitos + " cifras");
    }

    private static Object numeroDigitos (int numero) {
    var cifras = 0;
    while (numero !=0) {
        numero /= 10;
        cifras++;
    }
    return cifras;
    }

    private static void duploTriple() {
        var entre = new Scanner(System.in);
        System.out.println("Introduzca un número entero: ");
        int numero = entre.nextInt();
        System.out.println("Su número " + numero
                + " si lo duplicamos nos da " + (numero * 2)
                + " y si lo triplicamos nos da " + (numero * 3));
    }

    private static void aFahrenheit() {
        var scan = new Scanner(System.in);
        System.out.println("Introduca la temperatura en Grados Centígrados: ");
        var gc = scan.nextDouble();
        var fahrenh = pasoGrados(gc);
        System.out.println("Sus grados Centígrados: " + gc + ", pasados a Fahrenheint dan: "+ fahrenh + "");
    }

    private static Object pasoGrados(Double gc) {
        var fahr = 32 + (9 * gc / 5);
        return fahr;
    }

    @SuppressWarnings("unused")
    private static void parImpar() {
        var entrada = new Scanner(System.in);
        System.out.println("Introduzca un número entero: ");
        var numero = entrada.nextInt();
        System.out.println( "Su numero: " + numero + ((numero % 2 == 0) ? ",es un numero Par" : ", es un numero Impar"));
    }

    
}
