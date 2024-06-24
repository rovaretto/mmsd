package rovaretto.perrotta;

import java.util.List;
import java.util.ArrayList;

public class LiveNodeList {
    List<PermSale> liveNodes = new ArrayList<>();

    public void insert(PermSale permSale, int z) {
        if(permSale.getBII() < z){
            liveNodes.add(permSale);
        }
    }

    public void insert(List<PermSale> permSale, int z) {
        for(PermSale ps : permSale){
            if(ps.getBII() < z){
                liveNodes.add(ps);
            }
        }
    }

    public PermSale getENodes() {
        PermSale enode = liveNodes.get(0);
        liveNodes.remove(0);
        return enode;
    }

    public LiveNodeList(List<PermSale> liveNodes, int z) {
        insert(liveNodes,z);
    }


    public LiveNodeList(PermSale liveNodes, int z) {
        insert(liveNodes,z);
    }

    public boolean isEmpty() {
        return liveNodes.isEmpty();
    }
}
