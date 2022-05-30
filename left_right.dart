void main() {
  int a = 2;
  int b = 64;
  if (left_to_right(a, b) == right_to_left(a, b)) {
    print('Всё верно');
  } else {
    print('Не верно');
  }

  //print(left_to_right(2,64));
  right_to_left(2, 64);
  left_to_right(2, 64);
}

int left_to_right(int a, int b) {
  String m = b.toRadixString(2);
  int res = 1;
  for (int i = 0; i < (m.length); i++) {
    if (m[i] == '1') {
      res = (res * res) * a;
    } else {
      res = res * res;
    }
  }
  return res;
}

int right_to_left(int a, int b) {
  String m = b.toRadixString(2);
  int res = 1;
  int z = a;
  for (int i = m.length - 1; i + 1 > 0; i--) {
    if (m[i] == '1') {
      res = res * z;
      z = z * z;
    } else {
      z = z * z;
    }
  }
  return res * z;
}