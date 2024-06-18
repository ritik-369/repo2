class memoize
{
   private:
   public:
      map<vector<vector<int>>,int>data;
      bool isPresent(vector<vector<int>>&);
      void storeData(vector<vector<int>>&,int);
      int fetchData(vector<vector<int>>&);
};


bool memoize::isPresent(vector<vector<int>>&elem)
{
   return (!(data.find(elem)==data.end()));
}

void memoize::storeData(vector<vector<int>>&elem,int result)
{
   data[elem]=result;
}

int memoize::fetchData(vector<vector<int>>&elem)
{
   return data[elem];
}