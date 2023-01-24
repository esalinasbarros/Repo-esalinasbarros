#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

void abrir_archivo(string ruta) {
    string texto;
    ifstream read_file(ruta);
    while (getline (read_file, texto)) {
        cout << texto << '\n';
    }    
    read_file.close();
}

int main() {
    string ruta;
    //cout << "Escribe la ruta del archivo: ";
    //cin >> ruta;
    return 0;
}