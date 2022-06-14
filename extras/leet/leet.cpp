#include <iostream>
#include <string.h>

char str[] = "Fear  is\tthe\nmindkiller.\n";

int main(){

  std::cout << "Source string address: " << &str << std::endl;

  char delim[] = " \t\r\n\v\f";
  char *token = strtok(str, delim);
  while(token){
    std::cout << (void*)(token) << ": " << token << std::endl;
    token = strtok(nullptr, delim);
  }

  std::cout << "Complete.\n";
}