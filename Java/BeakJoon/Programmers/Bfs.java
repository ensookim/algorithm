public class Bfs{

    static Map<Integer, List<Integer>> graph = new HashMap<>();
    static Set<Integer> visited = new HashSet<>();

    public static void bfs(int startNode){
        // 시작점 예약하고
        Queue<Integer> queue = new LinkedList<>();
        queue.add(startNode);
        visited.add(startNode); // 방문처리

        //q가 비어있을 때 까지 반복
        while (!queue.isEmpty()){
            //현재 노드 방문 처리
            int curNode = queue.remove();

            //다음 노드 예약
            for (int nextNode: graph.get(curNode)){
                if (!visited.contains(nextNode)){
                    queue.add(nextNode);
                    visited.add(nextNode);
                }
            }
        }



    }

    public static void main(String[] args) {
        make
    }

}