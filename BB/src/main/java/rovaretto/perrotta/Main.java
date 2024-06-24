package rovaretto.perrotta;

import java.util.ArrayList;
import java.util.List;

public class Main {


    public static PermSale threads (int soglia){
        Sala salaA = new Sala(new Integer[]{52, 93, 56, 53, 62, 22, 98, 44}, 8);
        Sala salaB = new Sala(new Integer[]{100, 24, 131, 121, 104}, 5);
        Sala salaC = new Sala(new Integer[]{66, 72, 98, 42, 166, 36}, 6);
        Sala salaD = new Sala(new Integer[]{51, 74, 32, 104, 74, 99, 46}, 0);

        PermutazioniIterFIFO.z = soglia;
        PermSale psIniziale = new PermSale(salaA,salaB,salaC,salaD);
        LiveNodeList permSaleList = new LiveNodeList(psIniziale.getFigli(),PermutazioniIterFIFO.z);

        List<Thread> threads = new ArrayList<>();
        for (PermSale ps : permSaleList.liveNodes) {
            LiveNodeList radice = new LiveNodeList(ps, PermutazioniIterFIFO.z);
            Thread t = new Thread(()-> PermutazioniIterFIFO.risposte(radice));
            threads.add(t);
        }
        PermutazioniIterFIFO.numThread = threads.size();

        for (Thread t : threads) {
            t.start();
        }

        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        for (Thread t : PermutazioniIterFIFO.threadList) {
            try {
                t.join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        return PermutazioniIterFIFO.risultato;
    }

    public static void iterative_deepening(){
        PermSale result = null;
        int i = 27;
        while(result == null){
            result = threads(i);
            i++;
            System.out.println("indice" + i);
        }
    }

    public static void main(String[] args) {
        iterative_deepening();
        test();
    }


    public static void test(){
        System.out.println(PermutazioniIterFIFO.z);
        PermSale p = PermutazioniIterFIFO.risultato;

        List<Integer> a = p.getSalaA().convertiInDurata();
        List<Integer> b = p.getSalaB().convertiInDurata();
        List<Integer> c = p.getSalaC().convertiInDurata();
        List<Integer> d = p.getSalaD().convertiInDurata();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);

        System.out.println(p.getSalaA());
        System.out.println(p.getSalaB());
        System.out.println(p.getSalaC());
        System.out.println(p.getSalaD());

        ArrayList<Integer> ordinamentoOp = new ArrayList<>();
        ordinamentoOp.addAll(a);
        ordinamentoOp.addAll(b);
        ordinamentoOp.addAll(c);
        ordinamentoOp.addAll(d);

        ordinamentoOp.sort(Integer::compareTo);
        System.out.println(ordinamentoOp);
        for (int j = 0; j < ordinamentoOp.size() - 1; j++) {
            int actualBII  = ordinamentoOp.get(j + 1) - ordinamentoOp.get(j);
            System.out.println(actualBII);
        }
    }
}


/*
        LUNEDI 35
        Sala salaA = new Sala(new Integer[]{64, 135, 62, 66, 80, 73}, 0);
        Sala salaB = new Sala(new Integer[]{107, 135, 221, 17}, 0);
        Sala salaC = new Sala(new Integer[]{29, 129, 88, 234}, 0);
        Sala salaD = new Sala(new Integer[]{130, 36, 61, 29, 68, 81, 75}, 0);

        MARTEDI --
        Sala salaA = new Sala(new Integer[]{22, 53, 56, 44, 62, 52, 93, 98}, 0);
        Sala salaB = new Sala(new Integer[]{100, 131, 104, 121, 24}, 0);
        Sala salaC = new Sala(new Integer[]{42, 166, 66, 36, 98, 72}, 0);
        Sala salaD = new Sala(new Integer[]{51, 74, 32, 104, 74, 99, 46}, 0);

        MERCOLEDI 33
        Sala salaA = new Sala(new Integer[]{243, 45, 67, 61, 64}, 0);
        Sala salaB = new Sala(new Integer[]{141, 21, 44, 112, 133, 29}, 0);
        Sala salaC = new Sala(new Integer[]{100, 38, 146, 34, 162}, 0);
        Sala salaD = new Sala(new Integer[]{37, 104, 66, 47, 96, 47, 83}, 0);

        GIOVEDI 34
        Sala salaA = new Sala(new Integer[]{238, 43, 95, 104}, 0);
        Sala salaB = new Sala(new Integer[]{63, 169, 47, 34, 167}, 0);
        Sala salaC = new Sala(new Integer[]{263, 53, 89, 42, 33}, 0);
        Sala salaD = new Sala(new Integer[]{82, 94, 61, 79, 56, 47, 61}, 0);

        VENERDI 35
        Sala salaA = new Sala(new Integer[]{68, 197, 107, 108}, 0);
        Sala salaB = new Sala(new Integer[]{141, 35, 112, 131, 61}, 0);
        Sala salaC = new Sala(new Integer[]{174, 45, 130, 108, 23}, 0);
        Sala salaD = new Sala(new Integer[]{85, 70, 76, 47, 34, 42, 56, 70}, 0);
*/