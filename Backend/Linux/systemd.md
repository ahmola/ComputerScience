리눅스 초기화 시스템으로, 커널이 부팅이 완료된 직후 처음으로 실행되는 PID 1을 가지는 프로세스이다.

시스템이 종료될 때까지, 모든 서비스와 프로세스의 생성, 종료, 관리를 총괄하는 핵심 프로세스.

# initd

유닉스에서 유래된 전통적인 초기화 방식으로,

쉘 스크립트 기반으로 동작하며 `/etc/init.d/` 디렉터리에 저장된 스크립트들을 사용해 서비스를 제어.

시스템 상태를 Runlevel(0,1,3,5,6)로 나누어 관리한다.

- 0: halt, 즉 종료
- 1: single user, 단일 사용자 모드로 복구용
- 3: 다중 사용자 CLI 모드
- 5: 다중 사용자 GUI 모드
- 6: 시스템 재부팅

그러나, 이러한 구조에는 한계가 있었는데, 순차 실행으로 느린 부팅, 서비스 간 순서를 직접 지정해야줘야하는 복잡성, 

데몬 프로세스를 PID 파일에 의존하여 작업이 길어지게 되면, 히스토리가 늘어나게 되어 추적이 불가능해짐.

# systemd

시스템의 자원을 Unit이라는 단위로 추상화하여, 선언형 설정 파일(`.service`, `.target` 등)으로 관리

- `.service`: 백그라운드 데몬 프로세스(웹 서버, DB 등) 관리
- `.target`: 여러 유닛을 그룹화한 논리적 상태 (SysV의 Runlevel 대체)
- `.socket`: IPC 또는 네트워크 소켓을 관리하며, 요청 시 해당 서비스를 동적 실행
- `.timer`: 특정 시간에 작업을 수행하는 타이머 (기존 cron 역할 대체)
- `.mount`, `.automount`: 파일 시스템 마운트 지점 관리
- `.path`: 파일이나 디렉터리의 변경 상태를 감지하여 서비스 트리거

initd와의 호환성을 위해서 

    Runlevel 1 -> `rescue.target`
    
    Runlevel 3 -> `multi-user.target` 
    
    Runlevel 5 -> `graphical.target`
    
    Runlevel 6 -> `reboot.target`

로 시스템 상태를 호환시킴.

## 주요 기능 및 아키텍처

1. 병렬 부팅: 부팅 초기 단계에서, 필요한 모든 소켓을 미리 생성하여 수신 대기시켜놨다가 의존 관계에 있는 서비스들을 병렬 실행

2. cgroups(Control Group) 기반 프로세스 추적: 서비스마다 고유한 cgroup을 할당하여 부모 - 자식 프로세스가 동일한 cgroup내에 묶어 서비스 중지 시 모든 프로세스를 안전하게 종료

3. 통합 로깅 시스템(journald): `systemd-journald` 데몬으로 바이너리 로그 형식 사용, 각 서비스의 `stdout`/`stderr`출력을 통합 수집

## 사용 예제

- 서비스/시스템 제어
```bash
# 서비스 시작 / 중지 / 재시작
systemctl start nginx
systemctl stop nginx
systemctl restart nginx

# 서비스 상태 확인
systemctl status nginx

# 부팅 시 자동 실행 설정 / 해제
systemctl enable nginx
systemctl disable nginx

# 기본 Target 확인 및 변경 (GUI / CLI 전환)
systemctl get-default
systemctl set-default multi-user.target
```

- 로그 확인
```bash
# 특정 서비스의 로그 확인
journalctl -u nginx

# 실시간 로그 스트리밍 (tail -f 와 유사)
journalctl -f

# 현재 부팅 이후 발생한 로그만 확인
journalctl -b
```
