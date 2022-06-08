void main() {
  int a = 1;
  int p = 3;

  print(legandra(1, 3));
}

int legandra(int a, int p) {

    if (a == 1) {
      return 1;
    }
    if (a % 2 == 0){
      return legandra(a ~/ 2, p) * (-1) ** ((p ** 2 - 1) ~/ 8);
    }
    if (a % 2 != 0 && a != 1){
        return legandra(p % a, a) * (-1) ** (((a - 1) * (p - 1)) ~/ 4);
    }
}