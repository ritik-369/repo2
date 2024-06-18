#include<bits/stdc++.h>
using namespace std;
#define MAXIT 10000
#define debug(x) ""
#define shield(x) ""
#define forp(x) for(x)
#define Case(test)cout<<"Case #"<<test<<": "; 
#define ll long long
// #define int long long
#define INF 1000000007
#define y second
#define x first
#define all(x) x.begin(),x.end()
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
ll read(){ll var;cin>>var;return var;}
string reads(){string var;cin>>var;return var;}
ll max(ll a,ll b){return ((a>=b)?a:b);}
ll min(ll a,ll b){return ((a<=b)?a:b);}
int maxself(int &var1,int var2){var1=max(var1,var2);return var1;}
int minself(int &var1,int var2){var1=min(var1,var2);return var1;}
vector<string>_out={"NO\n","YES\n"};

//VERIFICATION= https://www.spoj.com/status/ns=30550729
template<typename T=long long>         // [(num^(pow))%mod]
T fastpow(T num,T pow,T mod_num=(T)(1e9+7))
{
   T res=1;
   while(pow>0)
   {
      if(pow&1)
      {
         res*=num;
         res%=mod_num;
      }
      num*=num;
      num%=(mod_num);
      pow>>=1;
   }
   res%=mod_num;
   return res;
}

string temp;
string s;
int n,len;
vector<vector<int>>dp;
int call(int idx,int p)
{
   if(len==p)
      return 0;
   if(idx==n)
   {
      // debug(temp);
      return 1;
   }
   int &ans=dp[idx][p];
   if(ans!=-1)
      return ans;
   ans=0;
   for(int i='A';i<='Z';i++)
   {
      if(s[p]==i)
      {
         temp.push_back(i);
         ans+=call(idx+1,p+1);
      }
      else
      {
         temp.push_back(i);
         ans+=call(idx+1,0);
      }
      temp.pop_back();
      ans%=INF;
   }
   ans%=INF;
   return ans;
}


ll solve(int tt,int t)
{
   dp=vector<vector<int>>(1001,vector<int>(101,-1));
   cin>>n>>s;
   //temp=s;
   len=s.length();
   int ans=fastpow<ll>(26,n,INF);
   ans-=call(0,0);
   ans+=INF;
   ans%=INF;
   cout<<ans<<endl;

   
   
   
   return 0;
}





int main()
{

    freopen("io_files/input.txt","r",stdin);
    freopen("io_files/output_main_code.txt","w",stdout);

   
   ll t=1,tt;
   cin>>t;
   tt=t;
   while(t--)
   {
      solve(tt,t);
   }
   
   
   return 0;
}

