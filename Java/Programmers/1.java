import jave.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        // 정렬하기
        Arrays.sort(d);
        
        // 예산 떨어질때 까지 인덱스 올리면서 카운트 ++
        for (int i= 0; i < d.length;  i++){
            if (budget - d[i] >= 0){
                budget -=d[i];
                anser +=1;
            }
            else {
                break;
            }
            
        }
        // 리턴
        
        return answer;
    }

    public static void main(String[] args) {

    }
}