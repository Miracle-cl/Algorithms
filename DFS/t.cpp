// vector::begin/end
#include <iostream>
#include <vector>

int main ()
{
  std::vector<int> myvector;
  for (int i=1; i<=5; i++) myvector.push_back(i);

  std::cout << "myvector contains:";
  for (std::vector<int>::iterator it = myvector.begin() ; it != myvector.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';

  std::cout << "rerverse myvector contains:";
  for (std::vector<int>::reverse_iterator it = myvector.rbegin() ; it != myvector.rend(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  std ::cout << 0 % 2;

  return 0;
}
