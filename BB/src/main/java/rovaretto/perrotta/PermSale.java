package rovaretto.perrotta;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/** Quadrupla, essenzialmente per permutazioni con ripetizione FIFO. */

public class PermSale {

    private Sala salaA;
    private Sala salaB;
    private Sala salaC;
    private Sala salaD;
    private int BII;

    private int dA;
    private int dB;
    private int dC;
    private int dD;

    private List<Integer> ordinamento;

    private List<Integer> listaOp = new ArrayList<>();


    public PermSale(Sala salaA, Sala salaB, Sala salaC, Sala salaD) {
        this.salaA = salaA;
        this.salaB = salaB;
        this.salaC = salaC;
        this.salaD = salaD;
//        BII = calcolaBII();

        this.dA = 0;
        this.dB = 0;
        this.dC = 0;
        this.dD = 0;

        this.BII = 0;
        this.ordinamento = new ArrayList<>();
        this.ordinamento.add(0);

        this.listaOp = new ArrayList<>();
        this.listaOp.addAll(List.of(salaA.getSala()));
        this.listaOp.addAll(List.of(salaB.getSala()));
        this.listaOp.addAll(List.of(salaC.getSala()));
        this.listaOp.addAll(List.of(salaD.getSala()));
        this.listaOp.sort(Integer::compareTo);
    }

    public PermSale(Sala salaA, Sala salaB, Sala salaC, Sala salaD,PermSale fatherPS) {
        this.salaA = salaA;
        this.salaB = salaB;
        this.salaC = salaC;
        this.salaD = salaD;
        this.BII = fatherPS.BII;
        this.dA = fatherPS.dA;
        this.dB = fatherPS.dB;
        this.dC = fatherPS.dC;
        this.dD = fatherPS.dD;
        this.listaOp = new ArrayList<>(fatherPS.listaOp);
        nuovoCalcolaBII(new ArrayList<>(fatherPS.ordinamento));
//        BII = calcolaBII();
    }

    private void nuovoCalcolaBII(List<Integer> ordinamento) {
        dA += salaA.getDurataSuIndex();
        dB += salaB.getDurataSuIndex();
        dC += salaC.getDurataSuIndex();
        dD += salaD.getDurataSuIndex();

        this.listaOp.remove((Integer) salaA.getDurataSuIndex());
        this.listaOp.remove((Integer) salaB.getDurataSuIndex());
        this.listaOp.remove((Integer)salaC.getDurataSuIndex());
        this.listaOp.remove((Integer)salaD.getDurataSuIndex());

        int min_sale = dA;
        min_sale = Math.min(min_sale,dB);
        min_sale = Math.min(min_sale,dC);
        min_sale = Math.min(min_sale,dD);

        ordinamento.add(dA);
        ordinamento.add(dB);
        ordinamento.add(dC);
        ordinamento.add(dD);
        ordinamento.sort(Integer::compareTo);

        int actual_BII;
        int i = 0;
        for (; ordinamento.get(i) <  min_sale; i++) {
            actual_BII = ordinamento.get(i+1) - ordinamento.get(i);
            if(actual_BII > this.BII) {
                this.BII = actual_BII;
            }
        }

        int gap = ordinamento.get(i+1) - ordinamento.get(i);
        if (gap > this.BII && gap > this.listaOp.getFirst()){
            this.BII = gap;
        }

        this.ordinamento = new ArrayList<>();
        for(; i < ordinamento.size(); i++) {
            this.ordinamento.add(ordinamento.get(i));
        }




    }

    public int calcolaBII(){
        if(salaA.getI_sala() == 0 || salaB.getI_sala() == 0 || salaC.getI_sala() == 0 || salaD.getI_sala() == 0) return 0;


        ArrayList<Integer> ordinamentoOp = new ArrayList<>();
        List<Integer> durataSalaA = salaA.convertiInDurata();
        List<Integer> durataSalaB = salaB.convertiInDurata();
        List<Integer> durataSalaC = salaC.convertiInDurata();
        List<Integer> durataSalaD = salaD.convertiInDurata();

        ordinamentoOp.addAll(durataSalaA);
        ordinamentoOp.addAll(durataSalaB);
        ordinamentoOp.addAll(durataSalaC);
        ordinamentoOp.addAll(durataSalaD);

        ordinamentoOp.sort(Integer::compareTo);

        int maxA = durataSalaA.getLast();
        int maxB = durataSalaB.getLast();
        int maxC = durataSalaC.getLast();
        int maxD = durataSalaD.getLast();

        int tmp = Math.min(maxA, maxB);
        tmp = Math.min(tmp, maxC);
        tmp = Math.min(tmp, maxD);

        if (ordinamentoOp.isEmpty()) return 0;

        int BII = ordinamentoOp.getFirst();
        for (int i = 0; i < ordinamentoOp.size() - 1 && ordinamentoOp.get(i) < tmp; i++) {
            int actualBII  = ordinamentoOp.get(i + 1) - ordinamentoOp.get(i);
            if (actualBII > BII) {
                BII = actualBII;
            }
        }

        return BII;
    }

    public List<PermSale> getFigli(){
        List<PermSale> figli = new ArrayList<>();

        for (Sala salaA_perm :  this.salaA.permNext()){
            for (Sala salaB_perm : this.salaB.permNext()){
                for (Sala salaC_perm : this.salaC.permNext()) {
                    for (Sala salaD_perm: this.salaD.permNext()) {
                        PermSale ps = new PermSale(salaA_perm,
                                                    salaB_perm,
                                                    salaC_perm,
                                                    salaD_perm, this);
                        figli.add(ps);
                    }
                }
            }
        }

        return figli;
    }

    public boolean completo() {
        return salaA.completo() &&
                salaB.completo() &&
                salaC.completo() &&
                salaD.completo();
    }

    @Override
    public String toString() {
        return "PermSale{" +
                "salaA=" + salaA +
                ", salaB=" + salaB +
                ", salaC=" + salaC +
                ", salaD=" + salaD +
                ", BII=" + BII +
                ", dA=" + dA +
                ", dB=" + dB +
                ", dC=" + dC +
                ", dD=" + dD +
                ", ordinamento=" + ordinamento +
                '}';
    }

    public int getBII() {
        return BII;
    }

    public Sala getSalaA() {
        return salaA;
    }

    public Sala getSalaB() {
        return salaB;
    }

    public Sala getSalaC() {
        return salaC;
    }

    public Sala getSalaD() {
        return salaD;
    }
}

