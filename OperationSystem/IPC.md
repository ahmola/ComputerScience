IPC(Inter-Process Communication) : 프로세스가 다른 프로세스와 데이터를 주고받는 통신. 네트워크로 연결된 다른 컴퓨터의 프로세스와의 통신도 포함됨.

    프로세스 내부 데이터 통신 : 한 프로세스 내 2개 이상의 스레드가 존재할 때의 통신. 전역 변수나 파일을 사용하여 데이터 통신

    프로세스 간 데이터 통신 : 같은 컴퓨터 내 동시 실행되고 있는 여러 프로세스끼리 통신. 공용 파일 또는 운영체제의 파이프를 사용함.

    네트워크를 이용한 데이터 통신 : 소켓을 사용하여 여러 컴퓨터가 네트워크 내에서 통신(네트워킹). 다른 컴퓨터의 함수를 호출하는 원격 프로시저 호출도 해당됨.

통신 방향에 따라 양방향 통신, 반양방향 통신(동시 전송 불가), 단방향 통신(전역 변수)이 있다.

단향향 통신 시에는 계속해서 전역 변수를 체크해야 하므로 반복문을 무한 실행하는 busy waiting을 해야한다. 이를 해결하기 위해 데이터의 도착을 알리는 동기화(synchronization)을 사용한다. 

파일을 사용한 통신 : 파일 입출력은 open, read/write, close로 구성된다. open()을 통해 파일 유무와 읽기/쓰기 권한을 확인하여 준비하는 단계이다. 정상 사용이 가능하면 fd(file descriptor, 정수형 식별자)반환. 이를 얻어서 read()/write() 함수로 작업을 하고 끝나면 close()함수로 fd를 반환한다.

파이프를 사용한 통신 : 운영체제가 제공. open()함수로 fd를 얻고 작업 후 close()로 fd반환. 단방향 통신이지만 파이프2개를 사용하면 양방향 통신가능. 한 프로세스가 다른 프로세스에 대한 작업이 진행 중이면 해당 작업이 끝날 때까지 대기 상태로 있다가 동기화가 이루어져 그 다음 작업을 할 수 있다. 파이프에는 named pipe와 anonymous pipe가 존재한다.

소켓 : IPC를 위한 네트워크 프로그래밍에서 사용되는 추상적인 인터페이스이다. 데이터를 주고받고 로컬 또는 원격 시스템 간의 연결을 관리한다. file descriptor의 한 종류로 open() 함수로 파일을 열듯, 네트워크를 열고 닫을 수 있다. 통신의 endpoint역할을 한다. IP주소와 포트 번호를 기반으로 서로를 식별하고 연결함.

    서버 측에서는 socket()으로 소켓을 생성하고 bind()로 IP주소와 포트 번호를 통해 서버를 열어 listen()을 통해 클라이언트의 연결 요청을 대기한다. accept()로 연결 요청을 받아서 새로운 소켓을 생성하여 recv()/send()로 데이터를 주고받는다. close()를 통해 소켓을 닫고 리소스를 해제한다.

    클라이언트 측에서 socket()으로 서버와 통신할 소켓을 생성하고, connect()로 서버의 ip와 포트에 연결을 요청한다. 요청이 성공하면 recv()/send()로 데이터를 주고받고, close()로 소켓을 닫는다.


소켓을 사용한 통신 : 여러 컴퓨터의 프로세스 간 통신. 다른 컴퓨터의 함수를 호출하는 것을 원격 프로시저 호출이라고 하며 이러한 호출은 소켓을 통해 구현한다. 통신을 위해서 다른 컴퓨터의 위치를 파악하고 해당 컴퓨터의 어떤 프로세스와 통신할지도 결정해야 한다.
쓰기 연산 시에는 데이터를 전송하고 읽기 연산 시 데이터를 받게 된다. 소켓은 프로세스 동기화를 지원하며 파이프 하나로 양방향 통신을 한다.