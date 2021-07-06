import java.util.Scanner;

public class NumeroSuerte {

    public static void main(String[] args){
        //(12/07/1980) = 12+7+1980 = 1999 = 28
        var sc = new Scanner(System.in);
        System.out.println("Ingrese la fecha de nacimiento (dd/mm/yyyy): ");
        var fecha = sc.next();
        System.out.println(fecha);
        fecha= fecha.trim();
        fecha= fecha.replaceAll("/","");
        System.out.println(fecha);

        int dia = Integer.valueOf(fecha.substring(0,2));
        System.out.println(dia);
        
        int mes = Integer.valueOf(fecha.substring(2,4));
        System.out.println(mes);

        int año = Integer.valueOf(fecha.substring(4));
        System.out.println(año);
        
        int suma1 = dia + mes + año;
        System.out.println(suma1);

        int numeroSuerte = 0;

        while (suma1 != 0) {
            numeroSuerte += (suma1 % 10);
            suma1 /= 10;
        }
       
        System.out.println(numeroSuerte);

       
        }


    
}
