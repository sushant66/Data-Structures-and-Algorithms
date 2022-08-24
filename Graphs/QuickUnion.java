public class QuickUnion {
    private int[] id;

    public QuickUnion(int N)
    {
        id = new int[N];
        for(int i=0;i<N;i++){
            id[i]=i;
        }
    }

    private int root(int i)
    {
        while(i != id[i]) i = id[i];
        return i;
    }

    public boolean connected(int p, int q)
    {
        return root(p) == root(q); 
    }


    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        id[i] = j;

    }

    public static void main(String args[]){
            QuickFindAlgorithm a = new QuickFindAlgorithm(5);
            a.union(3,4);
            a.union(1, 2);
            System.out.println(a.connected(1, 4));

    }   
}