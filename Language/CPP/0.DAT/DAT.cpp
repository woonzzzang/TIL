#include<iostream>
using namespace std;

// 시간 복잡도
    // O(Q * N) (쿼리 개수 * 데이터 개수)
    // 중첩 반복문으로 해결 
    // 입력 : 
    /*
    3
    3
    4
    5
    */
   /*
   3 O
   4 O
   5 X
   */

// int main() {
//     //  quiz 1)
//     // 해당 숫자가 배열에 존재하는지 Query 개수만큼 확인하는 프로그램 작성
//     int arr[10] = { 3, 4, 6, 7, 9, 7, 6, 1, 2, 3 };
//     int Q = 0; // Query

//     cin >> Q; // Query 입력 받음

//     for(int i = 0; i < Q; i++) { 
//         // Query 개수 만큼 입력을 받아서 
//         int num = 0;
//         int flag = 0;
//         cin >> num; // 숫자 입력 받음 
//         for(int j = 0; j < 10; j++) { 
//             // 다만 배열에 있는 값들을 다 확인해야 됨 
//             if (num == arr[j]) {
//                 flag = 1;
//             }
//         }
//         if (flag)
//         cout << num << " : " << "O" << "\n";
//         else
//         cout << num << " : " << "X" << "\n";
//     }
// }

// DAT (Direct Access Table)
// 배열의 조회 속도가 빠른 이점을 살려서 사용. O(1)
// 조회가 빈번한 데이터인 경우, 
// 1) DATable에 기록해두고,
    // 어떻게 기록?
    // 배열의 인덱스에 의미를 부여해서 사용 
// 2) 접근해서 사용.
// 해당 값의 존재 유무 체크 (Exist)
// 해당 값의 개수 체크 (Counting)
// ex) 좌표 정보 처리 : 해당 좌표를 방문했는가?
// ex) 그래프 자료구조에서 해당 노드를 방문했는가? 

/*
int arr[10] = { 3, 4, 6, 7, 9, 7, 6, 1, 2, 3 };
// 원본 배열
index : 0 1 2 3 4 5 6 7 8 9
value : 3 4 6 7 9 7 6 1 2 3
// DATable 생성
index : 0 1 2 3 4 5 6 7 8 9
value : 0 1 1 2 1 0 2 2 1 1
// 의미 : 해당 인덱스 값이 원본 배열에 몇 개 존재하는가?
// ex) 3의 개수는? DATable[3] -> 2개
// ex) 5의 개수는? DATable[5] -> 0개
*/

/*
3 == arr[0]

DAT[arr[0]] = 1;
DAT[arr[1]] = 1;
*/

// int main() {
//     // 시간 복잡도
//     // O(Q + N) (쿼리 개수 + 데이터 개수)
//     int arr[10] = { 3, 4, 6, 7, 9, 7, 6, 1, 2, 3};
//     // 1. DAT에 기록
//     int DAT[10] = { 0, }; // index: 어떤 숫자, value : 존재 유무, 크기 : 숫자 범위
//     for (int i = 0; i < 10; i++) {
//         // DAT[arr[i]] = 1; // 어떤 숫자가 존재한다. (Exist)
//         DAT[arr[i]] += 1; // 어떤 숫자가 하나 더 존재한다. (Counting)
//     }

//     // 2. Query 만큼 처리
//     int Q = 0;
//     cin >> Q;
//     for (int i = 0; i < Q; i++) {
//         int num = 0;
//         cin >> num;
//         cout << num << " : " << DAT[num] << "\n";
//     }
// }

// quiz 2) DAT 정렬 

int main() {
    char str[10] = "ACEFDFSAS";

    // 출력
    // AACDEFFSS

    int DAT[100] = { 0, }; // 대문자 A ~ Z (65 ~ 90)
    // 1. DAT에 기록
    for (int i = 0; str[i]; i++) { // NULL 문자 만나기 전까지 하나씩 증가
        DAT[str[i]] += 1;
    }

    // 2. 'A'부터 DAT에 기록되어 있는 개수만큼 출력
    for (char a = 'A'; a <= 'Z'; a++) {
        for (int j = 0; j < DAT[a]; j++) {
            cout << a;
        }
    }
}