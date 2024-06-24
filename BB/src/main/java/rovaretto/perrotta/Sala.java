package rovaretto.perrotta;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sala {
    private Integer [] sala;
    private int i_sala;

    public Sala(Integer[] sala, int i_sala) {
        this.sala = sala;
        this.i_sala = Math.min(i_sala, sala.length);
    }

    public List<Integer> convertiInDurata(){
        int time = 0;
        ArrayList<Integer> durataCumulata = new ArrayList<>();
        for(int i = 0; i < i_sala; i++){
            time += sala[i];
            durataCumulata.add(i,time) ;
        }
        return durataCumulata;
    }


    public ArrayList<Sala> permNext() {
        ArrayList<Sala> permutations = new ArrayList<>();
        for(int j = i_sala; j < sala.length; j++){
            Integer [] newPerm = Arrays.copyOf(sala,sala.length);
            swap(newPerm, i_sala, j);
            Sala newSala = new Sala(newPerm,i_sala+1);
            permutations.add(permutations.size(),newSala);
        }

        if(permutations.isEmpty()){
            Integer [] newPerm = Arrays.copyOf(sala,sala.length);
            Sala newSala = new Sala(newPerm,i_sala+1);
            permutations.add(newSala);
        }

        return permutations;
    }

    public List<Sala> generaFoglie(){
        ArrayList<Sala> lvl_i = new ArrayList<>();
        ArrayList<Sala> lvl_i_1 = new ArrayList<>();

        lvl_i.add(this);
        while (!lvl_i.getFirst().completo()){
            for(Sala sala : lvl_i){
                lvl_i_1.addAll(sala.permNext());
            }
            lvl_i = new ArrayList<>(lvl_i_1);
            lvl_i_1.clear();
        }
        return lvl_i;
    }

    public Integer[] getSala() {
        return sala;
    }

    public int getI_sala() {
        return i_sala;
    }

    public void setI_sala(int i_sala) {
        this.i_sala = i_sala;
    }

    private static void swap(Integer[] soluzione, int i, int j) {
        int tmp = soluzione[i];
        soluzione[i] = soluzione[j];
        soluzione[j] = tmp;
    }

    @Override
    public String toString() {
        return "Sala{" +
                "sala=" + Arrays.toString(sala) +
                ", i_sala=" + i_sala +
                '}';
    }

    public boolean completo() {
        return sala.length == i_sala;
    }


    public int getDurataSuIndex() {
        return i_sala <= sala.length ? sala[i_sala - 1] : 0;
    }
}

