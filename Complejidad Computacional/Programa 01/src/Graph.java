import java.util.List;
import java.util.LinkedList;

public class Graph {

  List<Arista> aristas;
  List<Nodo> vertices;

  public Graph(List<Integer> vList) {
    vertices = new LinkedList<>();
    for(Integer v: vList) {
      vertices.add(new Nodo(v));
    }
    aristas = new LinkedList<>();
  }

	class Arista {

	    public Nodo u;
	    public Nodo v;

	    public Arista(int u, int v) {
	      this.u = new Nodo(u);
	      this.v = new Nodo(v);
	    }

	    @Override
	    public boolean equals(Object other){
	      if (other == null) return false;
	      if (other == this) return true;
	      if (!(other instanceof Arista)) return false;
	      Arista e = (Arista)other;
	  	    if(u.num == e.u.num && v.num == e.v.num)
	        return true;
	      if(u.num == e.v.num && u.num == e.u.num)
	        return true;
	      return false;
	    }

	    public String getArista(){
	      String x = "("+this.v.getNum() +","+ this.u.getNum()+")";
	      return x;
	    }
	  }

	class Nodo {

	    public int num;

	    public Nodo(int num) {
	      this.num = num;
	    }


	    public int getNum(){
	      return this.num;
	    }
	  }

	public void addArista(int u, int v) {
	  aristas.add(new Arista(u, v));
	}

	public boolean hayArista(int u, int v) {
	  Arista e = new Arista(u, v);
	  Arista e2 = new Arista(v, u);
	  if(aristas.contains(e) || aristas.contains(e2)) {
	    return true;
	   }
	  return false;
	}

	public List<Arista> neighborhood(int u) {
	  List<Arista> list = new LinkedList<>();
	  Nodo auxV = vertices.get(vertices.indexOf(u));
	  for(Arista e : aristas) {
	      if(e.u.num == auxV.num || e.v.num == auxV.num)
	        list.add(e);
	    }
	  return  list;
	}
}
