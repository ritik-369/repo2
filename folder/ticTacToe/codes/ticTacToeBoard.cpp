#define INF 1000000007
class ticTacToeBoard
{
   private:
   public:
      int sizeOfBoard,tokenWidth,cellWidth,sideGap;
      string players[3];
      vector<vector<string>>board;
      vector<vector<int>>marked;
      vector<string>result={"Draw","Nothing","Player A wins","Player B Wins"};

      ticTacToeBoard(int,string,string);
      void showBoard();
      void printNumberOfTimes(string,int);
      string onCell(int,int);
      void markBoard(int,int,int);
      void unMarkBoard(int,int);
      int checkWinner();
      bool checkResult();
      pair<int,int>randomCell();
};

ticTacToeBoard::ticTacToeBoard(int size,string playerA="X",string playerB="O")
{
   this->sizeOfBoard=size;
   this->tokenWidth=max(playerA.size(),playerB.size());
   playerA.resize(tokenWidth,' ');playerB.resize(tokenWidth,' ');
   this->players[1]=playerA;
   this->players[2]=playerB;
   string gap=" ";
   gap.resize(tokenWidth,' ');
   this->players[0]=gap;
   this->sideGap=2;
   this->cellWidth=(tokenWidth+2*sideGap);
   board=vector<vector<string>>(size+2,vector<string>(size+2));
   marked=vector<vector<int>>(size+2,vector<int>(size+2,0));
}

string ticTacToeBoard::onCell(int row,int column)
{
   return players[marked[row][column]];
}

pair<int,int>ticTacToeBoard::randomCell()
{
   vector<pair<int,int>>cells;
   for(int i=1;i<=sizeOfBoard;i++)
      for(int j=1;j<=sizeOfBoard;j++)
         if(marked[i][j]==0)
            cells.push_back({i,j});
   int idx=randint(0,cells.size()-1);
   return cells[idx];
}


void ticTacToeBoard::printNumberOfTimes(string str,int times)
{
   for(int i=1;i<=times;i++)
      cout<<str;
}

bool ticTacToeBoard::checkResult()
{
   int res=checkWinner();
   if(res!=0)
   {
      cout<<result[res+1]<<endl;
      cout.flush();
   }
   return (res!=0);
}


void ticTacToeBoard::markBoard(int row,int column,int player)
{
   marked[row][column]=player;
}


void ticTacToeBoard::unMarkBoard(int row,int column)
{
   marked[row][column]=0;
}

void ticTacToeBoard::showBoard()
{
   for(int i=1;i<=sizeOfBoard;i++)
      cout<<" ",printNumberOfTimes("_",(cellWidth));

   cout<<endl;
   for(int k=1;k<=sizeOfBoard;k++)
   {
      for(int i=1;i<=3;i++)
      {
         for(int j=1;j<=sizeOfBoard+1;j++)
         {
            cout<<"|";
            if(i==1)
               printNumberOfTimes(" ",cellWidth);
            if(i==2 and j<=sizeOfBoard)
               printNumberOfTimes(" ",sideGap),cout<<onCell(k,j),printNumberOfTimes(" ",sideGap);
            if(i==3 and j<=sizeOfBoard)
               printNumberOfTimes("_",cellWidth);
         }
         cout<<endl;
      }
   }
}


/**
 * 1=for player A
 * 2=for player B
 * 0=for nothing
 * -1=for draw
 **/

int ticTacToeBoard::checkWinner()
{
   int empty=0;
   int playerA=1,playerB=1;
   for(int row=1;row<=sizeOfBoard;row++)
   {
      playerA=playerB=1;
      for(int column=1;column<=sizeOfBoard;column++)
      {
         if(marked[row][column]==0)
            empty=1;
         playerA&=(marked[row][column]==1);
         playerB&=(marked[row][column]==2);
      }
      if(playerA)return 1;
      if(playerB)return 2;
   }
   for(int column=1;column<=sizeOfBoard;column++)
   {
      playerA=playerB=1;
      for(int row=1;row<=sizeOfBoard;row++)
      {
         playerA&=(marked[row][column]==1);
         playerB&=(marked[row][column]==2);
      }
      if(playerA)return 1;
      if(playerB)return 2;
   }
   playerA=playerB=1;
   for(int diag=1;diag<=sizeOfBoard;diag++)
   {
      int row,column;
      row=column=diag;
      playerA&=(marked[row][column]==1);
      playerB&=(marked[row][column]==2);
   }

   if(playerA)return 1;
   if(playerB)return 2;


   playerA=playerB=1;
   for(int diag=1;diag<=sizeOfBoard;diag++)
   {
      int row,column;
      row=diag;
      column=sizeOfBoard+1-row;
      playerA&=(marked[row][column]==1);
      playerB&=(marked[row][column]==2);
   }

   if(playerA)return 1;
   if(playerB)return 2;

   if(!empty)
      return -1;

   return 0;
}


