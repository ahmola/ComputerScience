# Jenkins

- Java 기반 오픈소스 CI/CD 자동화 서버
- 플러그인 기반, 모든 툴과 연동 가능
- 자체 서버 필요(온프레미스)
- 스크립트(Jenkinsfile)로 파이프라인 정의

## 동작 원리

- jenkins master가 파이프라인들을 관리함
- build agent에서 빌드/테스트 실행
- jenkinsfile에 정의된 각 파이프라인(stage)를 실행

## jenkinsfile.yml

    pipeline {
        agent any

        tools {
            gradle 'gradle-7.5' // Jenkins에 사전 설치된 Gradle 이름
        }

        environment {
            IMAGE_NAME = 'myapp'
            REGISTRY = 'docker.io/username'
        }

        stages {
            stage('Clone') {
                steps {
                    git 'https://github.com/username/my-springboot-app.git'
                }
            }
            stage('Build') {
                steps {
                    sh './gradlew clean build'
                }
            }
            stage('Test') {
                steps {
                    sh './gradlew test'
                }
            }
            stage('Docker Build') {
                steps {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
            stage('Deploy') {
                steps {
                    // 예: 컨테이너 재시작
                    sh "docker stop myapp || true"
                    sh "docker rm myapp || true"
                    sh "docker run -d -p 8080:8080 --name myapp $IMAGE_NAME"
                }
            }
        }
    }