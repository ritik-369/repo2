#include<bits/stdc++.h>
using namespace std;
#define print(t) cout<<"Case #"<<t<<": " 
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define pi 3.14159265359
#define endl "\n"
#define ms(a,x) memset(a,x,sizeof(a))
#define memo(n,type,start) vector<type>memo(n,start)
#define vll(v,n) vector<ll>v(n)
#define rep0(i,n) for(ll i=0;i<=n;i++)
#define read(v) for(auto &a:v)cin>>a
#define bidirinput(v,a,b) v[a].push_back(b);v[b].push_back(a)
#define parity(x)  (x%2)
#define mods(n,mod) (long(n)%long(mod))
#define freq(v,val) count(v.begin(),v.end(),val)
#define reverse_till_end(v) reverse(v.begin(),v.end())
#define sort_till_end(v)  sort(v.begin(),v.end())
#define ll long long
struct triple{ll first,second,third;void assign(ll a,ll b,ll c){first=a;second=b;third=c;}};
ll min(ll a,ll b);
ll max(ll a,ll b);
void printv(vector<ll>v,char end_with);





int main()
{
  fastio;
  ll t,n,a,tt,p,m,b;
  string s,s1,s2,ans;
  freopen("../io_files/json.txt","w",stdout);
  while(1)
  {
     s1.clear();
     getline(cin,s);
     if(s=="ok")break;         //write ok in end
     for(auto a:s)
     {
        if(a=='"'||a=='\\')s1+='\\';
        s1+=a;
     }
     s=s1;
     if(s=="")s="\\n";
     ans="\""+s+"\",";
     cout<<ans<<endl;
     cout.flush();
  }

   return 0;
}


























































ll min(ll a,ll b)
{
   if(a>=b)return b;
   return a;
}



ll max(ll a,ll b)
{
   if(a<=b)return b;
   return a;
}


// push_back  pop_back  vector  INT_MAX  IMPOSSIBLE  POSSIBLE length size