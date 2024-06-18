//****************************Template Begins****************************//

// Header Files
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<utility>
#include<set>
#include<unordered_set>
#include<list>
#include<iterator>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<bitset>
#include<random>
#include<map>
#include<unordered_map>
#include<stdio.h>
#include<complex>
#include<math.h>
#include<cstring>
#include<chrono>
#include<string>
#include "ext/pb_ds/assoc_container.hpp"
#include "ext/pb_ds/tree_policy.hpp"

// Header Files End

using namespace std;
using namespace __gnu_pbds;
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update> ;

template<class key, class value, class cmp = std::less<key>>
using ordered_map = tree<key, value, cmp, rb_tree_tag, tree_order_statistics_node_update>;
// find_by_order(k)  returns iterator to kth element starting from 0;
// order_of_key(k) returns count of elements strictly smaller than k;

#define HARI ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define ll long long
#define umap unordered_map
#define uset unordered_set
#define lb lower_bound
#define ub upper_bound
#define fo(i,a,b) for(i=a;i<=b;i++)
#define all(v) (v).begin(),(v).end()
#define all1(v) (v).begin()+1,(v).end()
#define allr(v) (v).rbegin(),(v).rend()
#define allr1(v) (v).rbegin()+1,(v).rend()
#define sort0(v) sort(all(v))
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;
#define sz(x) (ll)x.size()
#define pb push_back
#define ppb pop_back
#define mkp make_pair
#define inf 1000000000000000005
const ll mod = 1e9 + 7;

ll inv(ll i) {if (i == 1) return 1; return (mod - ((mod / i) * inv(mod % i)) % mod) % mod;}

ll mod_mul(ll a, ll b, ll m) {a = a % m; b = b % m; return (((a * b) % m) + m) % m;}

ll mod_add(ll a, ll b) {a = a % mod; b = b % mod; return (((a + b) % mod) + mod) % mod;}

ll gcd(ll a, ll b) { if (b == 0) return a; return gcd(b, a % b);}

ll ceil_div(ll a, ll b) {return a % b == 0 ? a / b : a / b + 1;}

ll pwr(ll a, ll b) {a %= mod; ll res = 1; while (b > 0) {if (b & 1) res = res * a % mod; a = a * a % mod; b >>= 1;} return res;}
//****************************Template Ends*******************************//
vll dy = {0,1,-1,0};
vll dx = {-1,0,0,1};
vector<char> op(4);
vll k(4);

ll cost(ll coins, ll dir)
{
    if(op[dir] == '+')
    {
        return coins + k[dir];
    }
    else if(op[dir] == '-')
    {
        return coins - k [dir];
    }
    else if(op[dir] == '*')
    {
        return coins*k[dir];
    }
    if(coins >= 0)
    {
        return coins/k[dir];
    }
    else
    {
        return -1*(ceil_div(abs(coins),k[dir]));
    }
}

int main() {
    HARI;
// #ifndef ONLINE_JUDGE
//     freopen("input.txt" , "r" , stdin);
//     freopen("output.txt", "w", stdout);
// #endif
    ll t, n, i, j, ans, temp, sum, T,p,m,ar,ac;
    string sans;
    t = 1;
    cin >> t;
    T = t;
    while (t--)
    {
        cout << "Case #" << T - t << ": ";
        sans = "NO";
        ans = temp = sum = 0;
        cin >> n>>p>>m>>ar>>ac;
        fo(i,0,3)
        {
            cin>>op[i];
            cin>>k[i];
        }
        vector<vll>pizza_no(n+1,vll(n+1,-1));
        vector<vll>coins_given(n+1,vll(n+1,-1));



        ll dp[n+2][n+2][m+2][(1<<p)];

        ll k,mask;
        fo(i,1,n)
        {
            fo(j,1,n)
            {
                fo(k,0,m)
                {
                    fo(mask,0,(1<<p)-1)
                    {
                        dp[i][j][k][mask] = -inf;
                    }
                }
            }
        }


        fo(i,0,p-1)
        {
            ll x,y,c;
            cin>>x>>y>>c;
            pizza_no[x][y] = i;
            coins_given[x][y] = c;
        }

        dp[ar][ac][0][0] = 0;

        fo(k,0,m-1)
        {
            fo(i,1,n)
            {
                fo(j,1,n)
                {
                    ll d;
                    fo(d,0,3)
                    {
                        ll x = i + dx[d];
                        ll y = j + dy[d];
                        if(x<1 or x>n or y<1 or y>n)continue;
                        fo(mask,0,(1<<p) - 1)
                        {
                            if(dp[i][j][k][mask] == -inf)continue;
                            ll new_coins = cost(dp[i][j][k][mask],d);
                            ll new_mask = mask;

                            dp[x][y][k+1][new_mask] = max(dp[x][y][k+1][new_mask] ,new_coins);


                            if(pizza_no[x][y] != -1)
                            {
                                if(!(mask&(1<<pizza_no[x][y])))
                                {
                                    new_mask|=(1<<pizza_no[x][y]);
                                    new_coins+=coins_given[x][y];
                                    dp[x][y][k+1][new_mask] = max(dp[x][y][k+1][new_mask] ,new_coins);
                                }
                            }
                        }
                    }
                }
            }
        }
        ans = -inf;
        fo(i,1,n)
        {
            fo(j,1,n)
            {
                fo(k,0,m)
                {
                    ans = max(ans,dp[i][j][k][(1<<p) - 1]);
                }
            }
        }
        if(ans == -inf)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        cout<<ans<<"\n";
    }
    return 0;
}











