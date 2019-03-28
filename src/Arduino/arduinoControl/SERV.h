class SERV {
  public:
    int leftRPM, rightRPM;
    SERV (int,int);
};

SERV::SERV (int a, int b) {
  leftRPM = a;
  rightRPM = b;
}
