import java.util.ArrayList;
import java.util.Collections;

public class Vectores {
    public static void main(String[] args) {
        // 1. Declarar una lista vacía
        ArrayList<String> listaVacia = new ArrayList<>();

        // 2. Declarar una lista con más de 5 elementos
        ArrayList<String> listaConElementos = new ArrayList<>();
        listaConElementos.add("Elemento1");
        listaConElementos.add("Elemento2");
        listaConElementos.add("Elemento3");
        listaConElementos.add("Elemento4");
        listaConElementos.add("Elemento5");
        listaConElementos.add("Elemento6");

        // 3. Encuentre la longitud de las dos listas creadas anteriormente.
        int longitudListaVacia = listaVacia.size();
        int longitudListaConElementos = listaConElementos.size();
        System.out.println("Longitud de lista vacía: " + longitudListaVacia);
        System.out.println("Longitud de lista con elementos: " + longitudListaConElementos);

        // 4. Obtener el primer elemento, el elemento central y el último elemento de la
        // lista.
        String primerElemento = listaConElementos.get(0);
        String elementoCentral = listaConElementos.get(listaConElementos.size() / 2);
        String ultimoElemento = listaConElementos.get(listaConElementos.size() - 1);
        System.out.println("Primer elemento: " + primerElemento);
        System.out.println("Elemento central: " + elementoCentral);
        System.out.println("Último elemento: " + ultimoElemento);

        // 5. Crear una lista llamada Datos_personales que contenga (nombre, edad,
        // altura, estado civil, dirección), y agrega datos utilizando la funcion add().
        ArrayList<String> datosPersonales = new ArrayList<>();
        datosPersonales.add("Felipe Chamorro");
        datosPersonales.add("40");
        datosPersonales.add("175cm");
        datosPersonales.add("Casado");
        datosPersonales.add("Turbaco Calle 67");

        // 6. Crea una lista llamada it_companies y asígnele los valores iniciales
        // Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
        ArrayList<String> itCompanies = new ArrayList<>();
        itCompanies.add("Facebook");
        itCompanies.add("Google");
        itCompanies.add("Microsoft");
        itCompanies.add("Apple");
        itCompanies.add("IBM");
        itCompanies.add("Oracle");
        itCompanies.add("Amazon");

        // 7. Añadir una empresa a la lista it_companies utilizando la función add().
        itCompanies.add("Xioami");

        // 8. Comprobar si una determinada empresa existe en la lista it_companies.
        boolean existeEmpresa = itCompanies.contains("Amazon");
        System.out.println("¿Existe Amazon en la lista? " + existeEmpresa);

        // 9. Ordena la lista con el método sort()
        Collections.sort(itCompanies);

        // 10. Invierte la lista en orden descendente utilizando el método reverse()
        Collections.reverse(itCompanies);

        // 11. Elimine la primera empresa informática de la lista utilizando el método
        // remove.
        itCompanies.remove(0);

        // 12. Eliminar todas las empresas de la lista it_companies.
        itCompanies.clear();
    }
}
