package rovaretto.perrotta;

public class GenPair<A, B> {
    private A first;
    private B second;

    public GenPair(A r, B c) {
        this.first = r;
        this.second = c;
    }

    public A pi0() {
        return this.first;
    }

    public B pi1() {
        return this.second;
    }

    public String toString() {
        return "(" + pi0() + "," + pi1() + ")";
    }
}
