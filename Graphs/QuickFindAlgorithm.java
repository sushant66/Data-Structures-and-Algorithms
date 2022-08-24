public class QuickFindAlgorithm{
    private int[] id;

    public QuickFindAlgorithm(int N)
    {
        id = new int[N];
        for(int i=0;i<N;i++){
            id[i]=i;
        }
    }

    public boolean connected(int p, int q)
    {
        return id[p] == id[q]; 
    }


    public void union(int p, int q)
    {
        int pid = id[p];
        int qid = id[q];
        for(int i=0;i<id.length;i++){
            if(id[i] == pid) id[i] = qid;
        }

    }

    public static void main(String args[]){
            QuickFindAlgorithm a = new QuickFindAlgorithm(5);
            a.union(3,4);
            a.union(1, 3);
            System.out.println(a.connected(1, 4));

    }   
}