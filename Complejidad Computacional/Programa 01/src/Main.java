import java.util.*;

public class Main {

  public static void main(String[] args) {

    List<Integer> list = new LinkedList<>();
    for(int i = 1; i <= 10; i++) {
      list.add(i);
    }

    Graph graph = new Graph(list);
    Random rng = new Random();
    int randomV1 = 0;
    int randomV2 = 0;
    int randomEdgeNum = 1 + rng.nextInt(30);
    int c = 0;

    //Generamos la gráfica aleatoria
    while(c < randomEdgeNum) {
      do {
        randomV1 = 1 + rng.nextInt(10);
        randomV2 = 1 + rng.nextInt(10);
        if(!graph.hayArista(randomV1, randomV2) && randomV1 != randomV2)
        graph.addArista(randomV1, randomV2);
      } while(randomV1 == randomV2);
      c++;
    }
    //Damos una k arbitraria
    Scanner s = new Scanner(System.in);
    System.out.println("Ingresa una k:");
    int k = s.nextInt();
    //Podemos descomentar las siguientes 2 lineas para tomar una k aleatoria
    //Random ran = new Random();
    //int k = 1+ ran.nextInt(10);

    System.out.println("Aristas de la gráfica:");
    System.out.print("[");
    for(int i=0; i<graph.aristas.size(); i++){
      System.out.print(graph.aristas.get(i).getArista()+",");
    }
    System.out.print("]"); 
    System.out.println("");
    //Fase adivinadora
    List<Integer> solucion = new LinkedList<>();
    while(solucion.size() < k) {
      int n = 1 + rng.nextInt(10);
      if(!solucion.contains(n)) {
        solucion.add(n);
      }
    }

    System.out.println("Un posible candidato a ser solución es el siguiente:");
    System.out.print("[");
    for (int i=0; i<solucion.size(); i++){
      System.out.print(solucion.get(i)+",");
    }
    System.out.print("]");
    System.out.println("");
    //Fase verificadora
    boolean isSolution = true;
    for(int i = 0; i < k; i++) {
      for (int j = i + 1 ; j < k; j++) {
        int u = solucion.get(i);
        int v = solucion.get(j);
        if(!graph.hayArista(u, v)) {
          isSolution = false;
        }
      }
    }

      if (isSolution){
        System.out.println("-El candidato es solución-");
      }else {
        System.out.println("-El candidato no es solución-");
      }
  }
}
