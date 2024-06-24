package rovaretto.perrotta;
/** Genera tutte le permutazioni di una collezione di elementi
 * con un processo iterativo, producendo uno spazio degli stati
 * in accordo con una visita in ampiezza dell'albero che lo
 * rappresenta.
 *
 * La visita in ampiezza segue dall'accodare (politica FIFO)
 * tutti i figli di un eNode alla coda dei liveNodes.         */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PermutazioniIterFIFO {

    public static PermSale risultato;

    public static int z;

    public static int numThread = 0;

    public static List<Thread> threadList = new ArrayList<>();

    public static synchronized void setResult(PermSale permutazione, int z_nuovo) {
        if(z_nuovo < z) {
            z = z_nuovo;
            risultato = permutazione;
            System.out.println(z);
        }
    }

    public static synchronized void decrementThread(){
        numThread--;
    }

    public static synchronized void incrementThread(){
        numThread++;
    }

    /* Visita iterativamente l'elenco dei liveNodes, finche'
     * non si vuota. La terminazione e' assicurata dalla finitezza
     * dello spazio degli stati. Si assume un elenco iniziale di
     * liveNodes composto da un nodo che corrisponde alla radice
     * dello spazio degli stati.                                    */
    public static void risposte(LiveNodeList liveNodeList) {
        incrementThread();

        while (!liveNodeList.isEmpty()) {
            PermSale eNode = liveNodeList.getENodes();

//            while(numThread < 500 && liveNodes.size() > 50){
//                List <PermSale> radice = new ArrayList<>();
//                radice.add(eNode(liveNodes));
//                Thread t = new Thread(() -> PermutazioniIterFIFO.risposte(radice));
//                t.start();
//                threadList.add(t);
//            }


            if (!completo(eNode)) {
                if (!rifiuta(eNode)) {
                    espande(eNode, liveNodeList);
                }
            } else {
                if (accetta(eNode)) {
                    setResult(eNode, eNode.getBII());
                }
            }
        }
        decrementThread();

    }

    /* Preleva sempre il primo elemento disponibile nello spazio
     * degli stati.                                                */
    private static PermSale eNode(List<PermSale> spazioStati) {
        PermSale eNode = spazioStati.getFirst();
        spazioStati.removeFirst();
        return eNode;
    }

    /* Un eNode corrisponde and una soluzione completa se, la
     * sua componente, corrispondente ad una soluzione, e',
     * appunto, completa.                                        */
    private static boolean completo(PermSale eNode) {
        return eNode.completo();
    }

    /* Generando tutto lo spazio delle permutazioni, non
     * si rifiuta mai . */
    private static boolean rifiuta(PermSale eNode) {
        return eNode.getBII() >= z;
    }

    /* Implementa l'invariante di una visita in ampiezza dello spazio
     * degli stati. In particolare, tratta l'elenco dei liveNodes
     * come una coda, accodando i figli dell'attuale eNode.          */
    private static void espande(PermSale eNode,
                                          LiveNodeList liveNodes) {
        List<PermSale> figli = eNode.getFigli();
        liveNodes.insert(figli,z);
    }

    /* Generando tutto lo spazio delle permutazioni, non appena
     * una soluzione e' completa non possiamo far altro che accettare. */
    private static boolean accetta(PermSale eNode) {
        return eNode.getBII() < z;
    }
}