#include <iostream>
using namespace std;

int main()
{
   /* String functions (built-ins) */

   string frase = "El lobo estaba muerto";

   cout << frase.length() << endl;
   cout << frase[8] << endl;
   cout << frase.find("lobo", 0) << endl; /* El segundo numero es la posicion donde se quiere partir a buscar */
   cout << frase.substr(3, 13) << endl; /* Funciona igual qeu el slice en python 'frase[3: 13]' */
   cout << frase << endl;
   cout << frase << endl;
   cout << frase << endl;
   cout << frase << endl;
   /* Los index, funcionan igual que python y java */
}