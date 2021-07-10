#include <bits/stdc++.h>
using namespace std;

struct node {
    int x1, y1;
    int dist;
    node() {}
    node(int x1, int y1, int dist) : x1(x1), y1(y1), dist(dist)
    {
    }
};
 
// Utility method returns true if (x, y) lies
// inside Board
bool isInside(int x, int y, int N)
{
    if (x >= 1 && x <= N)
    {
        if( y >= 1 && y <= N)
        {
            return true;
        }
    }
    return false;
}
 
// Method returns minimum step
// to reach target position
int minStepToReachTarget(
    int knightPos[], int targetPos[],
    int N  ,  vector< pair <int,int> > vect)
{
    // x and y direction, where a knight can move
    int dx[] = { -2, -1, 1, 2, -2, -1, 1, 2 };
    int dy[] = { -1, -2, -2, -1, 1, 2, 2, 1 };
 
    // queue for storing states of knight in board
    queue<node> q;
 
    // push starting position of knight with 0 distance
    q.push(node(knightPos[0], knightPos[1], 0));
 
    node t;
    int x, y;
    bool visit[N + 1][N + 1];
 
    // make all cell unvisited
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            visit[i][j] = false;
 
    // visit starting state
    visit[knightPos[0]][knightPos[1]] = true;
 
    // loop untill we have one element in queue
    while (!q.empty()) {
        t = q.front();
        q.pop();
 
        // if current cell is equal to target cell,
        // return its distance
        if (t.x1 == targetPos[0] && t.y1 == targetPos[1])
            return t.dist;
 
        // loop for all reachable states
        for (int i = 0; i < 8; i++) {
            x = t.x1 + dx[i];
            y = t.y1 + dy[i];
 
            // If reachable state is not yet visited and
            // inside board, push that state into queue
            if (isInside(x, y, N) && !visit[x][y] && vect[i].first != x && vect[i].second != y ) {
                visit[x][y] = true;
                q.push(node(x, y, t.dist + 1));
            }
        }
    }
}
 
// Driver code to test above methods
int main()
{
    int N = 30 , x, y,s,r ;
 
cout <<"enter knightPos x \n";
cin>> x;
cout<<"enter knightPos y\n";
cin>> y ;
int knightPos[]={x,y};
cout <<"enter targetPos x \n";
cin>> s;
cerr<<"enter targetPos y\n";
cin>> r ;
int targetPos[]={s,r};
 
 vector< pair <int,int> > vect;
 
int ObstaclesN;
cout<<"Enter number of Obstacles \n";
cin>>ObstaclesN;
int ObstaclesX[ObstaclesN] , ObstaclesY[ObstaclesN];
 
for(int i = 0 ; i< ObstaclesN ; i++ )
{
    for(int j = 0 ; j< 1 ; j++ ){
    cout<<"Enter Obstacle X \n";
    cin>>ObstaclesX[i];
    cout<<"Enter Obstacle Y \n";
    cin>>ObstaclesY[i];
}
}
int n = sizeof(ObstaclesX)/sizeof(ObstaclesX[0]);
 
for (int i=0; i<n; i++)
        vect.push_back( make_pair(ObstaclesX[i],ObstaclesY[i]) );
   /* for (int i=0; i<n; i++)
    {
        cout << vect[i].first << " "
             << vect[i].second << endl;
    }*/
 
 
    cout<<"minimum number of steps to target = ";
    cout << minStepToReachTarget(knightPos, targetPos, N , vect );
    return 0;
}
 