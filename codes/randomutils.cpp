mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define seed_rng() rng.seed(chrono::steady_clock::now().time_since_epoch().count());
#define uid(from,to) uniform_int_distribution<int>(from,to)
#define urd(from,to) uniform_real_distribution<double>(from,to)
int randint(int from=0,int to=1000000000){return uid(from,to)(rng);};
double randfloat(int from=0,int to=1000000000){return urd(from,to)(rng);};