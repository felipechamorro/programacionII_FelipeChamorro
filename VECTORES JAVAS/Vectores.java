import java.util.ArrayList;
import java.util.Collections;

public class Vectores {
    public static void main(String[] args) {
        
        ArrayList<String> listaVacia = new ArrayList<>();

        
        ArrayList<String> listaConElementos = new ArrayList<>();
        listaConElementos.add("Elemento1");
        listaConElementos.add("Elemento2");
        listaConElementos.add("Elemento3");
        listaConElementos.add("Elemento4");
        listaConElementos.add("Elemento5");
        listaConElementos.add("Elemento6");

        
        int longitudListaVacia = listaVacia.size();
        int longitudListaConElementos = listaConElementos.size();
        System.out.println("Longitud de lista vacía: " + longitudListaVacia);
        System.out.println("Longitud de lista con elementos: " + longitudListaConElementos);

        
        String primerElemento = listaConElementos.get(0);
        String elementoCentral = listaConElementos.get(listaConElementos.size() / 2);
        String ultimoElemento = listaConElementos.get(listaConElementos.size() - 1);
        System.out.println("Primer elemento: " + primerElemento);
        System.out.println("Elemento central: " + elementoCentral);
        System.out.println("Último elemento: " + ultimoElemento);

        
        ArrayList<String> datosPersonales = new ArrayList<>();
        datosPersonales.add("Felipe Chamorro");
        datosPersonales.add("40");
        datosPersonales.add("175cm");
        datosPersonales.add("Casado");
        datosPersonales.add("Turbaco Calle 67");

        
        ArrayList<String> itCompanies = new ArrayList<>();
        itCompanies.add("Facebook");
        itCompanies.add("Google");
        itCompanies.add("Microsoft");
        itCompanies.add("Apple");
        itCompanies.add("IBM");
        itCompanies.add("Oracle");
        itCompanies.add("Amazon");

      
        itCompanies.add("Xioami");

        
        boolean existeEmpresa = itCompanies.contains("Amazon");
        System.out.println("¿Existe Amazon en la lista? " + existeEmpresa);

        
        Collections.sort(itCompanies);

        
        Collections.reverse(itCompanies);

        
        itCompanies.remove(0);

        
        itCompanies.clear();
    }
}
