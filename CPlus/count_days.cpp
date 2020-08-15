#include <iostream>
#include <ctime>

using namespace std;

int callback()
{
   int a=0;

   cin >> a;

   if (a == 1)
       cout << "a is 1" << endl;
   else {
      int b =10;
      cout << "a is not 1" << endl;
      cout << "b is " << b << endl;
   }

   return 0;
}

int main()
{
   int day;
   char plus;
   int x,y,z;

   callback();
   return 0;

   cout << "Hello World" << endl;

   // current date/time based on current system
   time_t now = time(0);
   cout << "Number of sec since January 1,1970:" << now << endl;

   tm *ltm = localtime(&now);
   // print various components of tm structure.
   cout << "Year:" << 1900 + ltm->tm_year << endl;
   cout << "Month: "<< 1 + ltm->tm_mon<< endl;
   cout << "Day: "<<  ltm->tm_mday << endl;
   cout << "Time: "<< ltm->tm_hour << ":";
   cout << ltm->tm_min << ":";
   cout << ltm->tm_sec << endl;

   cout << "Input Mum's birthday like 2020-8-14:" << endl;
   tm first_ltm;
   cin >> x >> plus >> y >> plus >> z;
    if (plus!='-')
        cout << "\nError format. should like: 2020-08-14";
    else
       first_ltm.tm_year = x -1900;
       first_ltm.tm_mon = y - 1;
       first_ltm.tm_mday = z;


   cout << "Input my birthday like 2020-8-14:" << endl;
   tm sec_ltm ;
   cin>> x >> plus >> y >> plus >> z;
   if (plus!='-')
        cout << "\nError format. should like: 2020-08-14";
   else {
       sec_ltm.tm_year = x -1900;
       sec_ltm.tm_mon = y - 1;
       sec_ltm.tm_mday = z;
   }

   /*difftime*/
   double secs = difftime(mktime(&sec_ltm), mktime(&first_ltm));
   cout << "\nThe Diff days:" << secs / (3600*24)  << endl;

   return 0;
}
