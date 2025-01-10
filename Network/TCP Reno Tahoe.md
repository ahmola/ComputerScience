<img src = "renotahoe.png">

처음에는 slow start를 통해 1개에서 시작하여 2배씩 늘려나가다가 ssthresh 값에 도달하면 additive increase로 바꿔 1씩 증가하는 방식으로 하고, 오류 발생 시 taeho는 1개로 줄여 기존 slow start로 다시 시작하여 ssthresh 값을 오류 발생시점의 절반에 해당하는 값으로 설정한다. reno는 기존 값의 절반으로 줄이고 additive increase를 사용하는 방식이다. 