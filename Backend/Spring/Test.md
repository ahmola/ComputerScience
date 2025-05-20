테스트들의 경우, 성공 케이스보다는 실패 케이스(예외, 검증 실패 등)가 더 중요하게 다뤄짐.
# Unit Test

하나의 Bean이나 클래스의 로직을 검증하기 위한 테스트

ex) userService.save()가 잘 작동하는지 테스트

Mock으로 의존 객체를 대신하여 Spring Context를 띄우지 않아서 매우 빠름.

@Mock, @MockBean, Mockito.mock() 등으로 객체를 대신함

    @ExtendWith(MockitoExtension.class) 
    class MemberServiceTest {
        
        @InjectMocks
        private MemberService memberService;

        @Mock
        private MemberRepository memberRepository;

        @Test
        void 회원가입_성공() {
            // given
            Member member = new Member("홍길동");
            when(memberRepository.save(any())).thenReturn(member);

            // when
            Member result = memberService.register(member);

            // then
            assertEquals("홍길동", result.getName());
        }
    }

@InjectMocks로 테스트를 진행할 클래스에 @Mock으로 설정된 클래스를 주입함.

간단하게 실제 db나 서버없이 로직 검사 가능

# Integration Test

여러 계층을 통합해서 실제처럼 동작하는지 검증하는 테스트

ex) controller + service + reposity + db까지 전체 흐름이 제대로 이뤄지는지 테스트

Spring Context를 실제로 가동함

Bean을 등록하고, DI, 트랜잭션 등을 실제 수행

    @SpringBootTest
    @AutoConfigureMockMvc
    class MemberControllerTest {

        @Autowired
        private MockMvc mockMvc;

        @Test
        void 회원_등록_성공() throws Exception {
            String body = "{\"name\":\"홍길동\"}";

            mockMvc.perform(post("/members")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(body))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("홍길동"));
        }
    }

- @SpringBootTest : 전체 컨텍스트 로딩

- @AutoConfigurationMockMvc : 실제 HTTP 요청처럼 동작하도록 함

- MockMvc : HTTP 요청 시뮬레이션

그러나 느리기 때문에, 핵심 시나리오 위주로 작성해야 함

## 자주 사용되는 어노테이션

- @SpringBootTest : 전체 애플리케이션 테스트

- @WebMvcTest(Controller.class) : 컨트롤러만 테스트함. 서비스와 레포지토리는 mock으로 대체

- @DataJpaTest : JPA Repository 테스트. 쿼리와 JPA 동작 확인

- @MockBean : Spring Bean을 Mock으로 대체. 특정 컴포넌트를 mock처리

- @Transactional : 테스트 데이터 롤백(기본적으로 붙어있음)