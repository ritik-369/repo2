using namespace std;
#include "ticTacToeBoard.cpp"
#include "optimise.cpp"
class ticTacToeGame:public ticTacToeBoard 
{
   private:
      int playerA,playerB,endOfGame,levelAI1,levelAI2;    //1 for AI and 2 for Human
      chrono::duration<long double> timeDelayForAI=0.6s;
      string symbolForplayerA="X",symbolForplayerB="O";
      vector<int>scores={-1,1}; //for loose,win
      memoize data;
      int maxDepth;
   public:
      ticTacToeGame(int);
      pair<int,int> moveAI(int);
      void moveHuman(int);
      int moveTurn(int,int);
      void moveRandom(int);
      int decision(int); //0 for random and 1 for optimal
};

ticTacToeGame::ticTacToeGame(int sizeOfBoard):ticTacToeBoard(sizeOfBoard,"X","O")
{
   maxDepth=(sizeOfBoard*sizeOfBoard)+10;
   if(sizeOfBoard>3)maxDepth=3;
   cout<<"Choose First Player (X)"<<endl;
   cout<<"1. AI"<<endl;
   cout<<"2. Human"<<endl;
   cin>>playerA;
   if(playerA==1)
   {
      cout<<"Enter Level For AI 1(1-11)=";
      cin>>levelAI1;
   }
   cout<<endl;

   cout<<"Choose Second Player (O)"<<endl;
   cout<<"1. AI"<<endl;
   cout<<"2. Human"<<endl;
   cin>>playerB;
   if(playerB==1)
   {
      cout<<"Enter Level For AI 2(1-11)=";
      cin>>levelAI2;
   }



   endOfGame=0;

   system("cls");
   int turn=0;
   showBoard();
   while(!endOfGame)
   {
      turn++;
      if((turn)%2)moveTurn((turn%2),playerA);
      else moveTurn((turn%2),playerB);
      int res=checkResult();
      if(res!=0)
         endOfGame=1;
   }



}

pair<int,int> ticTacToeGame::moveAI(int playerNO)
{
   int original=playerNO;

   function<int(int,int,int)>minimax=[&](int playerNO,int maximize,int depth){
      if(data.isPresent(marked))return data.fetchData(marked);
      int resultOfGame=checkWinner();
      if(resultOfGame==-1)return 0;
      if(resultOfGame!=0)return scores[original==resultOfGame];
      int optimal=((maximize)?-INF:INF);
      int nextPLayerNO=(3-playerNO);
      for(int row=1;row<=sizeOfBoard;row++)
      {
         for(int column=1;column<=sizeOfBoard;column++)
         {
            if(marked[row][column]!=0)continue;
            marked[row][column]=nextPLayerNO;
            optimal=((maximize)?max(optimal,minimax(nextPLayerNO,maximize^1,depth+1)):min(optimal,minimax(nextPLayerNO,maximize^1,depth+1)));
            marked[row][column]=0;

            ///////////////////////////////////////////////OPTIMIZATION 0/////////////////////////////////////////////
            // if(maximize==1 && optimal==1)return 1;
            // if(maximize==0 and optimal==-1)return -1;

            
            ///////////////////////////////////////////////OPTIMIZATION 1/////////////////////////////////////////////
            // if(maximize && optimal==1)return 1;
            // if(maximize==0 and optimal==-1)return -1;
            // if(maximize && optimal==0)return 0;
            // if(maximize==0 and optimal==0)return 0;

            

            ///////////////////////////////////////////////OPTIMIZATION 2/////////////////////////////////////////////
            if(depth>=maxDepth)
            {
               if(maximize && optimal==1)return 1;
               if(maximize==0 and optimal==-1)return -1;
               if(maximize && optimal==0)return 0;
               if(maximize==0 and optimal==0)return 0;
            }

            ///////////////////////////////////////////////OPTIMIZATION 3/////////////////////////////////////////////
            // if(depth>=maxDepth)
            // {
            //    if(maximize && optimal==1)return 1;
            //    if(maximize==0 and optimal==-1)return -1;
            //    return -1;
            // }


         }
      }
      data.storeData(marked,optimal);
      return optimal;
   };

   int optimal=-INF;
   pair<int,int>res; 
   for(int row=1;row<=sizeOfBoard;row++)
   {
      for(int column=1;column<=sizeOfBoard;column++)
      {
         if(marked[row][column]!=0)continue;
         marked[row][column]=playerNO; 
         int newScore=minimax(playerNO,0,0);
         marked[row][column]=0;
         if(newScore>optimal)
         {
            optimal=newScore;
            res={row,column};
         }
      }
   }
   return res;
}

/**
 * optimal is ((level-1)*p)% more than random
 * then random+optimal=total ---(1)
 * ((optimal-random)/random)*100 = (level)
 * 100*(optimal-random)=level*random
 * 100*(total-2*random)=level*random
 * 100*total=200*random+level*random
 * random=(100*total)/(200+level)
 * replace level by (level-1)*p
 * 
 * random= (100*total)/(200+(level-1)*p);
 * Total Level=(1,11);
 */
int ticTacToeGame::decision(int level)
{
   vector<int>res;
   int total=1000, percent=20;
   int random=(100*total)/(200+(level-1)*percent);
   int optimal=total-random;
   for(int i=1;i<=random;i++)
      res.push_back(0);
   for(int j=1;j<=optimal;j++)
      res.push_back(1);
   shuffle(res.begin(),res.end(),rng);
   return (res[randint(0,total-1)]);
}

void ticTacToeGame::moveRandom(int playerNO)
{
   auto cell=randomCell();
   marked[cell.first][cell.second]=playerNO;
}

int ticTacToeGame::moveTurn(int turn,int playerType)
{
   int playerNO=(turn)?1:2;


   if(playerNO==1)
      cout<<"Player A Turn";
   else
      cout<<"Player B Turn";

   cout<<endl;
   if(playerType==1) 
   {
      if(sizeOfBoard<=3)this_thread::sleep_for(timeDelayForAI);
      int level=((playerNO==1)?levelAI1:levelAI2);
      if(decision(level)==0)
      {
         moveRandom(playerNO);
      }
      else
      {
         auto location=moveAI(playerNO);
         marked[location.first][location.second]=playerNO;
      }
   }
   else 
   {
      moveHuman(playerNO); //firt or second player
   }
   system("cls");
   cout<<endl;
   showBoard();
   return 1;
}


void ticTacToeGame::moveHuman(int player)
{
   int row,column;
   while(1)
   {
      cout<<"Enter Row and Column\n";
      cout.flush();
      cin>>row>>column;
      if(marked[row][column]!=0 or (row<0 or column<0) or (row>sizeOfBoard or column>sizeOfBoard))
      {
         cout<<"\nInvalid Move\n";
         continue;
      }
      break;
   }
   markBoard(row,column,player);
}
